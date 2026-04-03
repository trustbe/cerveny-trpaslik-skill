#!/usr/bin/env python3
"""
Scraper pro cervenytrpaslik.eu — série IX-XII + doplňkový obsah.
"""

import re
import sys
import time
import logging
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE = "https://www.cervenytrpaslik.eu"
DELAY = 2
UA = "RedDwarfFanClub-KnowledgeBase/1.0"
OUT = Path.home() / "red-dwarf-skill" / "raw"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S", stream=sys.stderr)
log = logging.getLogger("scrape_eu")

stats = {"ok": 0, "fail": 0, "files": 0}


def fetch(url):
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=30)
        r.raise_for_status()
        stats["ok"] += 1
        return r.text
    except Exception as e:
        log.error(f"FAIL {url}: {e}")
        stats["fail"] += 1
        return None


def extract(html):
    """Extract main content from WordPress page."""
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["script", "style", "noscript", "nav", "header", "footer", "aside"]):
        tag.decompose()

    # WordPress: try .entry-content first, then article, then main
    content = soup.find(class_="entry-content")
    if not content:
        content = soup.find("article")
    if not content:
        content = soup.find("main")
    if not content:
        content = soup

    text = content.get_text(separator="\n", strip=False)
    text = re.sub(r"[ \t]+", " ", text)
    lines = [l.strip() for l in text.split("\n")]
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def save(text, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    stats["files"] += 1
    log.info(f"  Saved: {path.name} ({len(text)} chars)")


def fetch_save(url, path):
    html = fetch(url)
    if html:
        text = extract(html)
        if len(text) > 200:
            save(text, path)
        else:
            log.warning(f"  Too short ({len(text)} chars): {path.name}")
    time.sleep(DELAY)


def main():
    log.info("=" * 50)
    log.info("Scraping cervenytrpaslik.eu — série IX-XII")
    log.info("=" * 50)

    # === 1. SCÉNÁŘE ===
    log.info("=== SCÉNÁŘE (CZ, série IX-XII) ===")

    scenare = [
        # Série IX
        ("ix-rada-scenare/se09e01", "53_Zpatky_na_Zemi_1"),
        ("ix-rada-scenare/se09e02", "54_Zpatky_na_Zemi_2"),
        ("ix-rada-scenare/se09e03", "55_Zpatky_na_Zemi_3"),
        # Série X
        ("x-rada-scenare/se10e01", "56_Trojan"),
        ("x-rada-scenare/se10e02", "57_Fathers_and_Suns"),
        ("x-rada-scenare/se10e03", "58_Lemons"),
        ("x-rada-scenare/se10e04", "59_Entangled"),
        ("x-rada-scenare/se10e05", "60_Dear_Dave"),
        ("x-rada-scenare/se10e06", "61_The_Beginning"),
        # Série XI
        ("xi-rada-scenare/se11e01", "62_Twentica"),
        ("xi-rada-scenare/se11e02", "63_Samsara"),
        ("xi-rada-scenare/se11e03", "64_Give_and_Take"),
        ("xi-rada-scenare/se11e04", "65_Officer_Rimmer"),
        ("xi-rada-scenare/se11e05", "66_Krysis"),
        ("xi-rada-scenare/se11e06", "67_Can_of_Worms"),
        # Série XII
        ("xii-rada-scenare/se12e01", "68_Cured"),
        ("xii-rada-scenare/se12e02", "69_Siliconia"),
        ("xii-rada-scenare/se12e03", "70_Timewave"),
        ("xii-rada-scenare/se12e04", "71_Mechocracy"),
        ("xii-rada-scenare/se12e05", "72_M-Corp"),
        ("xii-rada-scenare/se12e06", "73_Skipper"),
    ]

    for url_path, name in scenare:
        url = f"{BASE}/scenare/{url_path}/"
        log.info(f"  {name}")
        fetch_save(url, OUT / "scenare_cz_eu" / f"{name}.txt")

    # === 2. DETAILY EPIZOD ===
    log.info("=== EPIZODY (detaily IX-XII + TPL) ===")

    epizody = [
        # Série IX
        ("ix-rada/s09e01", "53_Zpatky_na_Zemi_1"),
        ("ix-rada/s09e02", "54_Zpatky_na_Zemi_2"),
        ("ix-rada/s09e03", "55_Zpatky_na_Zemi_3"),
        # Série X
        ("x-rada/s10e01", "56_Trojan"),
        ("x-rada/s10e02", "57_Fathers_and_Suns"),
        ("x-rada/s10e03", "58_Lemons"),
        ("x-rada/s10e04", "59_Entangled"),
        ("x-rada/s10e05", "60_Dear_Dave"),
        ("x-rada/s10e06", "61_The_Beginning"),
        # Série XI
        ("xi-rada/s11e01", "62_Twentica"),
        ("xi-rada/s11e02", "63_Samsara"),
        ("xi-rada/s11e03", "64_Give_and_Take"),
        ("xi-rada/s11e04", "65_Officer_Rimmer"),
        ("xi-rada/s11e05", "66_Krysis"),
        ("xi-rada/s11e06", "67_Can_of_Worms"),
        # Série XII
        ("xii-rada/s12e01", "68_Cured"),
        ("xii-rada/s12e02", "69_Siliconia"),
        ("xii-rada/s12e03", "70_Timewave"),
        ("xii-rada/s12e04", "71_Mechocracy"),
        ("xii-rada/s12e05", "72_M-Corp"),
        ("xii-rada/s12e06", "73_Skipper"),
        # The Promised Land
        ("the-promised-land", "74_The_Promised_Land"),
    ]

    for url_path, name in epizody:
        url = f"{BASE}/seznam-dilu/{url_path}/"
        log.info(f"  {name}")
        fetch_save(url, OUT / "epizody_eu" / f"{name}.txt")

    # === 3. HNIDOPICH ===
    log.info("=== HNIDOPICH (IX-XII) ===")

    for serie in ["ix-rada", "x-rada", "xi-rada", "xii-rada"]:
        url = f"{BASE}/hnidopich/{serie}/"
        log.info(f"  {serie}")
        fetch_save(url, OUT / "hnidopich_eu" / f"{serie}.txt")

    # === 4. SEKCE ===
    log.info("=== SEKCE ===")

    sekce = [
        ("zajimavosti/vite-ze", "vite_ze"),
        ("slovnik-pojmu", "slovnik"),
        ("slovnik-pojmu/nadavky", "nadavky"),
        ("postavy-herci/seznam-vsech-postav", "postavy"),
        ("kucharka/kucharka", "kucharka"),
        ("co-se-jinam-neveslo/sex-kdo-s-kym", "sex"),
        ("co-se-jinam-neveslo/kalendar", "kalendar"),
        ("zajimavosti/ze-zakulisi", "zakulisi"),
    ]

    for url_path, name in sekce:
        url = f"{BASE}/{url_path}/"
        log.info(f"  {name}")
        fetch_save(url, OUT / "sections_eu" / f"{name}.txt")

    # === STATS ===
    log.info("=" * 50)
    log.info(f"DONE: {stats['ok']} fetched, {stats['fail']} failed, {stats['files']} files")
    log.info("=" * 50)


if __name__ == "__main__":
    main()
