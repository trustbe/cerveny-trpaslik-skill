#!/usr/bin/env python3
"""
Red Dwarf Fan Club Knowledge Base Scraper
Scrapes cervenytrpaslik.cz — gently, with love.
"""

import os
import re
import sys
import time
import logging
import urllib3
from pathlib import Path
from urllib.parse import urljoin, parse_qs, urlparse, quote

import requests
from bs4 import BeautifulSoup

# Suppress SSL warnings (expired cert)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "http://www.cervenytrpaslik.cz/"
DELAY = 2  # seconds between requests
USER_AGENT = "RedDwarfFanClub-KnowledgeBase/1.0"
OUTPUT_DIR = Path.home() / "red-dwarf-skill" / "raw"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
log = logging.getLogger("scraper")

# Stats
stats = {"fetched": 0, "failed": 0, "bytes": 0, "files_written": 0}


def fetch(url: str) -> str | None:
    """Fetch a URL, try multiple encodings, return text or None."""
    headers = {"User-Agent": USER_AGENT}
    try:
        resp = requests.get(url, headers=headers, verify=False, timeout=30)
        resp.raise_for_status()

        # Try encodings
        for enc in ["utf-8", "windows-1250", "iso-8859-2", "latin-1"]:
            try:
                text = resp.content.decode(enc)
                if "í" in text or "á" in text or "ě" in text or "<" in text:
                    stats["fetched"] += 1
                    stats["bytes"] += len(resp.content)
                    return text
            except (UnicodeDecodeError, UnicodeError):
                continue

        stats["fetched"] += 1
        stats["bytes"] += len(resp.content)
        return resp.text

    except Exception as e:
        log.error(f"Failed to fetch {url}: {e}")
        stats["failed"] += 1
        return None


def extract_main_content(html: str) -> str:
    """Extract only the main content area (width=633 td), skip navigation."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove script, style, noscript
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()

    # Try to find the main content td (width=633)
    main_td = soup.find("td", attrs={"width": "633"})
    if not main_td:
        # Try wider content area
        for td in soup.find_all("td"):
            w = td.get("width", "")
            if w and int(w) > 500 if w.isdigit() else False:
                main_td = td
                break

    if main_td:
        text = main_td.get_text(separator="\n", strip=False)
    else:
        # Fallback: get all text but try to skip menu
        text = soup.get_text(separator="\n", strip=False)

    # Clean up
    text = re.sub(r"[ \t]+", " ", text)
    lines = [line.strip() for line in text.split("\n")]
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_script_content(html: str) -> str:
    """Extract script content from .htm scenario files (MS Word format)."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove script, style
    for tag in soup.find_all(["script", "style", "noscript", "head"]):
        tag.decompose()

    # Find Section1 div (MS Word export format)
    section = soup.find("div", class_="Section1")
    if section:
        text = section.get_text(separator="\n", strip=False)
    else:
        # Fallback: just get body text
        body = soup.find("body")
        text = (body or soup).get_text(separator="\n", strip=False)

    # Clean up
    text = re.sub(r"[ \t]+", " ", text)
    lines = [line.strip() for line in text.split("\n")]
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def save(text: str, path: Path):
    """Save text to file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    stats["files_written"] += 1
    log.info(f"  Saved: {path.name} ({len(text)} chars)")


def fetch_and_save(url: str, path: Path, extractor=None) -> str | None:
    """Fetch URL, extract content, save, return HTML."""
    html = fetch(url)
    if html:
        if extractor:
            text = extractor(html)
        else:
            text = extract_main_content(html)
        if len(text) > 100:  # Skip near-empty pages
            save(text, path)
        else:
            log.warning(f"  Skipping {path.name} (only {len(text)} chars)")
        time.sleep(DELAY)
        return html
    time.sleep(DELAY)
    return None


def get_page_url(section_id: str, mnu: int = 0) -> str:
    return f"{BASE_URL}index.php?id={section_id}&mnu={mnu}"


# ═══════════════════════════════════════════════════════════
# SCENÁŘE — direct .htm files
# ═══════════════════════════════════════════════════════════

# Complete list of all 52 episodes with their .htm filenames
SCENARE_CZ = [
    # Série I (1988)
    ("CZ-01-1_Konec.htm", "01_Konec"),
    ("CZ-02-1_Ozveny_budoucnosti.htm", "02_Ozveny_budoucnosti"),
    ("CZ-03-1_Rovnovaha_sil.htm", "03_Rovnovaha_sil"),
    ("CZ-04-1_Cekani_na_boha.htm", "04_Cekani_na_boha"),
    ("CZ-05-1_Sebevedomi_a_mindrak.htm", "05_Sebevedomi_a_mindrak"),
    ("CZ-06-1_Ja_na_druhou.htm", "06_Ja_na_druhou"),
    # Série II (1988)
    ("CZ-07-2_Kryton.htm", "07_Kryton"),
    ("CZ-08-2_Lepsi_nez_zivot.htm", "08_Lepsi_nez_zivot"),
    ("CZ-09-2_Diky_za_tu_vzpominku.htm", "09_Diky_za_tu_vzpominku"),
    ("CZ-10-2_Skvira_ve_stazi.htm", "10_Skvira_ve_stazi"),
    ("CZ-11-2_Queeg.htm", "11_Queeg"),
    ("CZ-12-2_Paralelni_vesmir.htm", "12_Paralelni_vesmir"),
    # Série III (1989)
    ("CZ-13-3_Pozpatku.htm", "13_Pozpatku"),
    ("CZ-14-3_Trosecnici.htm", "14_Trosecnici"),
    ("CZ-15-3_Polymorf.htm", "15_Polymorf"),
    ("CZ-16-3_Vymena_tel.htm", "16_Vymena_tel"),
    ("CZ-17-3_Fotostroj_casu.htm", "17_Fotostroj_casu"),
    ("CZ-18-3_Posledni_den.htm", "18_Posledni_den"),
    # Série IV (1991)
    ("CZ-19-4_Kamila.htm", "19_Kamila"),
    ("CZ-20-4_DNA.htm", "20_DNA"),
    ("CZ-21-4_Spravedlnost.htm", "21_Spravedlnost"),
    ("CZ-22-4_Bila_dira.htm", "22_Bila_dira"),
    ("CZ-23-4_Jina_dimenze.htm", "23_Jina_dimenze"),
    ("CZ-24-4_Roztaveni.htm", "24_Roztaveni"),
    # Série V (1992)
    ("CZ-25-5_Hololod.htm", "25_Hololod"),
    ("CZ-26-5_Inkvizitor.htm", "26_Inkvizitor"),
    ("CZ-27-5_Psychoteror.htm", "27_Psychoteror"),
    ("CZ-28-5_Karantena.htm", "28_Karantena"),
    ("CZ-29-5_Demoni_a_andele.htm", "29_Demoni_a_andele"),
    ("CZ-30-5_Navrat_do_reality.htm", "30_Navrat_do_reality"),
    # Série VI (1993)
    ("CZ-31-6_Psireny.htm", "31_Psireny"),
    ("CZ-32-6_Legie.htm", "32_Legie"),
    ("CZ-33-6_Pistolnici_z_Apokalypsy.htm", "33_Pistolnici_z_Apokalypsy"),
    ("CZ-34-6_Polymorf-II-Emocuc.htm", "34_Polymorf_II_Emocuc"),
    ("CZ-35-6_Rimmerosvet.htm", "35_Rimmerosvet"),
    ("CZ-36-6_Mimo_realitu.htm", "36_Mimo_realitu"),
    # Série VII (1997)
    ("CZ-37-7_Pekelne_ostry_vylet.htm", "37_Pekelne_ostry_vylet"),
    ("CZ-38-7_Nachystejte_kvetinace.htm", "38_Nachystejte_kvetinace"),
    ("CZ-39-7_Uroboros.htm", "39_Uroboros"),
    ("CZ-40-7_Zkouska_kanalem.htm", "40_Zkouska_kanalem"),
    ("CZ-41-7_Stesk.htm", "41_Stesk"),
    ("CZ-42-7_Zadna_legrace.htm", "42_Zadna_legrace"),
    ("CZ-43-7_Epidem.htm", "43_Epidem"),
    ("CZ-44-7_Nanarchie.htm", "44_Nanarchie"),
    # Série VIII (1999)
    ("CZ-45-8_Zpatky_v_Cervenem-1.htm", "45_Zpatky_v_Cervenem_1"),
    ("CZ-46-8_Zpatky_v_Cervenem-2.htm", "46_Zpatky_v_Cervenem_2"),
    ("CZ-47-8_Zpatky_v_Cervenem-3.htm", "47_Zpatky_v_Cervenem_3"),
    ("CZ-48-8_Kassandra.htm", "48_Kassandra"),
    ("CZ-49-8_Televize_Kryton.htm", "49_Televize_Kryton"),
    ("CZ-50-8_Pete-I.htm", "50_Pete_I"),
    ("CZ-51-8_Pete-II.htm", "51_Pete_II"),
    ("CZ-52-8_Jenom_sympataci.htm", "52_Jenom_sympataci"),
]

SCENARE_EN = [
    ("EN-01-1_The_End.htm", "01_The_End"),
    ("EN-02-1_Future_Echoes.htm", "02_Future_Echoes"),
    ("EN-03-1_Balance_Of_Power.htm", "03_Balance_Of_Power"),
    ("EN-04-1_Waiting_For_God.htm", "04_Waiting_For_God"),
    ("EN-05-1_Confidence_And_Paranoia.htm", "05_Confidence_And_Paranoia"),
    ("EN-06-1_Me2.htm", "06_Me2"),
    ("EN-07-2_Kryten.htm", "07_Kryten"),
    ("EN-08-2_Better_Than_Life.htm", "08_Better_Than_Life"),
    ("EN-09-2_Thanks_For_The_Memory.htm", "09_Thanks_For_The_Memory"),
    ("EN-10-2_Stasis_Leak.htm", "10_Stasis_Leak"),
    ("EN-11-2_Queeg.htm", "11_Queeg"),
    ("EN-12-2_Parallel_Universe.htm", "12_Parallel_Universe"),
    ("EN-13-3_Backwards.htm", "13_Backwards"),
    ("EN-14-3_Marooned.htm", "14_Marooned"),
    ("EN-15-3_Polymorph.htm", "15_Polymorph"),
    ("EN-16-3_Bodyswap.htm", "16_Bodyswap"),
    ("EN-17-3_Timeslides.htm", "17_Timeslides"),
    ("EN-18-3_The Last Day.htm", "18_The_Last_Day"),
    ("EN-19-4_Camille.htm", "19_Camille"),
    ("EN-20-4_DNA.htm", "20_DNA"),
    ("EN-21-4_Justice.htm", "21_Justice"),
    ("EN-22-4_White_Hole.htm", "22_White_Hole"),
    ("EN-23-4_Dimension_Jump.htm", "23_Dimension_Jump"),
    ("EN-24-4_Meltdown.htm", "24_Meltdown"),
    ("EN-25-5_Holoship.htm", "25_Holoship"),
    ("EN-26-5_Inquisitor.htm", "26_Inquisitor"),
    ("EN-27-5_Terrorform.htm", "27_Terrorform"),
    ("EN-28-5_Quarantine.htm", "28_Quarantine"),
    ("EN-29-5_Demons_And_Angels.htm", "29_Demons_And_Angels"),
    ("EN-30-5_Back_To_Reality.htm", "30_Back_To_Reality"),
    ("EN-31-6_Psirens.htm", "31_Psirens"),
    ("EN-32-6_Legion.htm", "32_Legion"),
    ("EN-33-6_Gunmen_of_the_Apocalypse.htm", "33_Gunmen_of_the_Apocalypse"),
    ("EN-34-6_Emohawk.htm", "34_Emohawk"),
    ("EN-35-6_Rimmeroworld.htm", "35_Rimmeroworld"),
    ("EN-36-6_Out_of_time.htm", "36_Out_of_time"),
    ("EN-37-7_Tikka_to_Ride.htm", "37_Tikka_to_Ride"),
    ("EN-38-7_Stoke_Me_A_Clipper.htm", "38_Stoke_Me_A_Clipper"),
    ("EN-39-7_Ouroboros.htm", "39_Ouroboros"),
    ("EN-40-7_Duct_Soup.htm", "40_Duct_Soup"),
    ("EN-41-7_Blue.htm", "41_Blue"),
    ("EN-42-7_Beyond_A_Joke.htm", "42_Beyond_A_Joke"),
    ("EN-43-7_Epideme.htm", "43_Epideme"),
    ("EN-44-7_Nanarchy.htm", "44_Nanarchy"),
    ("EN-45-8_Back_in_the_Red_I.htm", "45_Back_in_the_Red_I"),
    ("EN-46-8_Back_in_the_Red_II.htm", "46_Back_in_the_Red_II"),
    ("EN-47-8_Back_in_the_Red_III.htm", "47_Back_in_the_Red_III"),
    ("EN-48-8_Cassandra.htm", "48_Cassandra"),
    ("EN-49-8_Krytie_TV.htm", "49_Krytie_TV"),
    ("EN-50-8_Pete_I.htm", "50_Pete_I"),
    ("EN-51-8_Pete_II.htm", "51_Pete_II"),
    ("EN-52-8_Only_the_Good.htm", "52_Only_the_Good"),
]


def scrape_scenare():
    """Scrape all 52 Czech + 52 English scripts from .htm files."""
    log.info("=== SCÉNÁŘE (CZ — 52 epizod) ===")
    for filename, save_name in SCENARE_CZ:
        url = f"{BASE_URL}scenare/{filename}"
        log.info(f"  {save_name}")
        fetch_and_save(url, OUTPUT_DIR / "scenare_cz" / f"{save_name}.txt", extractor=extract_script_content)

    log.info("=== SCÉNÁŘE (EN — 52 epizod) ===")
    for filename, save_name in SCENARE_EN:
        # Handle URL-encoded space in "The Last Day"
        url = f"{BASE_URL}scenare/{quote(filename, safe='/')}"
        log.info(f"  {save_name}")
        fetch_and_save(url, OUTPUT_DIR / "scenare_en" / f"{save_name}.txt", extractor=extract_script_content)


# ═══════════════════════════════════════════════════════════
# SECTION SCRAPERS
# ═══════════════════════════════════════════════════════════


def scrape_sections():
    """Scrape all main sections (content only, no nav)."""
    log.info("=== SEKCE ===")
    sections = [
        ("posadka", 1), ("epizody", 0), ("nadavky", 0), ("postrehy", 0),
        ("direktivy", 0), ("havarky", 0), ("nabozenstvi", 0), ("vesmir", 4),
        ("slovnik", 0), ("dabing", 13), ("zakulisi", 12), ("hnidopich", 3),
        ("texty", 5), ("sex", 10), ("kucharka", 6), ("kalendar", 0),
        ("nsfaq", 0), ("dodatky", 0), ("kostymy", 0), ("fantazie", 14),
        ("film", 8), ("herci", 2), ("hudba", 5), ("mobil", 16),
        ("merchandising", 0), ("kontakty", 0), ("srazy", 0),
        ("quiz", 0), ("filmoteka", 0), ("uvod", 0), ("download", 9),
    ]

    for section_id, mnu in sections:
        log.info(f"  Section: {section_id}")
        url = get_page_url(section_id, mnu)
        html = fetch_and_save(url, OUTPUT_DIR / "sections" / f"{section_id}.txt")

        if html and section_id in ("hnidopich", "herci", "fantazie", "kucharka", "epizody", "texty", "hudba"):
            scrape_subpages(html, section_id, url)


def scrape_subpages(html: str, section_id: str, base_url: str):
    """Scrape sub-pages linked from a section."""
    soup = BeautifulSoup(html, "html.parser")
    # Only look in main content area
    main_td = soup.find("td", attrs={"width": "633"})
    search_area = main_td if main_td else soup

    sub_links = []
    seen = {base_url}

    for a in search_area.find_all("a", href=True):
        href = a["href"]
        if href.startswith("javascript:") or href.startswith("#"):
            continue
        full_url = urljoin(base_url, href)
        if "cervenytrpaslik.cz" in full_url and full_url not in seen:
            # Check it's a sub-page of this section
            parsed = urlparse(full_url)
            params = parse_qs(parsed.query)
            link_id = params.get("id", [""])[0]
            if link_id and link_id != section_id:
                seen.add(full_url)
                text = a.get_text(strip=True)
                sub_links.append({"url": full_url, "text": text})

    if sub_links:
        log.info(f"    {len(sub_links)} sub-pages for {section_id}")
        subdir = OUTPUT_DIR / section_id
        for i, link in enumerate(sub_links[:60], 1):
            safe_name = re.sub(r'[^\w\-]', '_', link['text'][:40]).strip('_') or f"sub_{i}"
            log.info(f"    Sub {i}: {link['text'][:40]}")
            fetch_and_save(link["url"], subdir / f"{safe_name}.txt")


def scrape_posadka():
    """Scrape character detail pages."""
    log.info("=== POSÁDKA (detaily) ===")
    main_chars = ["lister", "rimmer", "cat", "kryten", "holly", "kochanski"]

    url = get_page_url("posadka", 1)
    html = fetch(url)
    if not html:
        return
    time.sleep(DELAY)

    for char in main_chars:
        for pattern in [
            f"index.php?id={char}&mnu=1",
            f"index.php?id={char}&mnu=0",
        ]:
            char_url = urljoin(BASE_URL, pattern)
            log.info(f"  Character: {char}")
            char_html = fetch(char_url)
            if char_html and len(char_html) > 2000:
                text = extract_main_content(char_html)
                save(text, OUTPUT_DIR / "posadka" / f"{char}.txt")
                time.sleep(DELAY)
                break
            time.sleep(DELAY)


def scrape_nsfaq():
    """Scrape all NSFAQ entries."""
    log.info("=== NSFAQ (kompletní) ===")
    url = get_page_url("nsfaq", 0)
    html = fetch(url)
    if not html:
        return

    text = extract_main_content(html)
    save(text, OUTPUT_DIR / "nsfaq" / "nsfaq_page_001.txt")
    time.sleep(DELAY)

    # Discover pagination from the page
    soup = BeautifulSoup(html, "html.parser")
    page_links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "nsfaq" in href and "str=" in href:
            full_url = urljoin(BASE_URL, href)
            page_links.add(full_url)

    # Extract max page number
    max_page = 1
    for link in page_links:
        params = parse_qs(urlparse(link).query)
        for v in params.get("str", []):
            try:
                max_page = max(max_page, int(v))
            except ValueError:
                pass

    log.info(f"  Found pagination links, max page: {max_page}")

    # If we found pagination, follow it
    if max_page > 1:
        for page in range(2, max_page + 1):
            page_url = f"{BASE_URL}index.php?id=nsfaq&str={page}&mnu=0"
            log.info(f"  NSFAQ page {page}/{max_page}")
            fetch_and_save(page_url, OUTPUT_DIR / "nsfaq" / f"nsfaq_page_{page:03d}.txt")
    else:
        # Try brute-force pagination
        log.info("  Trying brute-force NSFAQ pagination...")
        empty_streak = 0
        for page in range(2, 200):
            page_url = f"{BASE_URL}index.php?id=nsfaq&str={page}&mnu=0"
            log.info(f"  NSFAQ page {page}")
            page_html = fetch(page_url)
            if page_html:
                page_text = extract_main_content(page_html)
                if len(page_text) > 500:
                    save(page_text, OUTPUT_DIR / "nsfaq" / f"nsfaq_page_{page:03d}.txt")
                    empty_streak = 0
                else:
                    empty_streak += 1
            else:
                empty_streak += 1

            if empty_streak >= 3:
                log.info(f"  Stopping NSFAQ at page {page} (3 empty pages)")
                break
            time.sleep(DELAY)


def scrape_vzkazy():
    """Scrape all vzkazy (14864 messages)."""
    log.info("=== VZKAZY (kompletní archiv) ===")
    url = get_page_url("vzkazy", 0)
    html = fetch(url)
    if not html:
        return

    text = extract_main_content(html)
    save(text, OUTPUT_DIR / "vzkazy" / "vzkazy_page_0001.txt")
    time.sleep(DELAY)

    # Discover pagination
    soup = BeautifulSoup(html, "html.parser")
    page_links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "vzkazy" in href and "str=" in href:
            full_url = urljoin(BASE_URL, href)
            page_links.add(full_url)

    max_page = 1
    for link in page_links:
        params = parse_qs(urlparse(link).query)
        for v in params.get("str", []):
            try:
                max_page = max(max_page, int(v))
            except ValueError:
                pass

    log.info(f"  Pagination: max page = {max_page}")

    if max_page > 1:
        for page in range(2, max_page + 1):
            page_url = f"{BASE_URL}index.php?id=vzkazy&str={page}&mnu=0"
            log.info(f"  Vzkazy page {page}/{max_page}")
            fetch_and_save(page_url, OUTPUT_DIR / "vzkazy" / f"vzkazy_page_{page:04d}.txt")
    else:
        # Brute-force — 14864 messages, ~20 per page = ~743 pages
        log.info("  Brute-force pagination...")
        empty_streak = 0
        for page in range(2, 1000):
            page_url = f"{BASE_URL}index.php?id=vzkazy&str={page}&mnu=0"
            if page % 50 == 0:
                log.info(f"  Vzkazy page {page}")
            page_html = fetch(page_url)
            if page_html:
                page_text = extract_main_content(page_html)
                if len(page_text) > 300:
                    save(page_text, OUTPUT_DIR / "vzkazy" / f"vzkazy_page_{page:04d}.txt")
                    empty_streak = 0
                else:
                    empty_streak += 1
            else:
                empty_streak += 1

            if empty_streak >= 5:
                log.info(f"  Stopping vzkazy at page {page}")
                break
            time.sleep(DELAY)


def scrape_epizody_detail():
    """Scrape individual episode detail pages."""
    log.info("=== EPIZODY (detaily) ===")
    url = get_page_url("epizody", 0)
    html = fetch(url)
    if not html:
        return
    time.sleep(DELAY)

    # Extract links from main content only
    soup = BeautifulSoup(html, "html.parser")
    main_td = soup.find("td", attrs={"width": "633"})
    search_area = main_td if main_td else soup

    ep_links = []
    seen = set()
    for a in search_area.find_all("a", href=True):
        href = a["href"]
        if href.startswith("javascript:") or href.startswith("#"):
            continue
        full_url = urljoin(url, href)
        parsed = urlparse(full_url)
        params = parse_qs(parsed.query)
        link_id = params.get("id", [""])[0]
        if link_id.startswith("epizod") and full_url not in seen and full_url != url:
            seen.add(full_url)
            text = a.get_text(strip=True)
            ep_links.append({"url": full_url, "text": text})

    log.info(f"  Found {len(ep_links)} episode detail links")
    for i, link in enumerate(ep_links, 1):
        safe_name = re.sub(r'[^\w\-]', '_', link['text'][:40]).strip('_') or f"ep_{i}"
        log.info(f"  Episode {i}: {link['text'][:40]}")
        fetch_and_save(link["url"], OUTPUT_DIR / "epizody" / f"{i:02d}_{safe_name}.txt")


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

def main():
    log.info("=" * 60)
    log.info("Red Dwarf Fan Club Scraper v2 — START")
    log.info(f"Output: {OUTPUT_DIR}")
    log.info("=" * 60)

    # Phase 1: Main sections (quick)
    scrape_sections()

    # Phase 2: Scripts — direct .htm files (CZ + EN)
    scrape_scenare()

    # Phase 3: Character details
    scrape_posadka()

    # Phase 4: Episode detail pages
    scrape_epizody_detail()

    # Phase 5: NSFAQ (full)
    scrape_nsfaq()

    # Phase 6: Vzkazy (full archive — this takes a while)
    scrape_vzkazy()

    # Final stats
    log.info("=" * 60)
    log.info("SCRAPING COMPLETE")
    log.info(f"  Pages fetched:  {stats['fetched']}")
    log.info(f"  Pages failed:   {stats['failed']}")
    log.info(f"  Files written:  {stats['files_written']}")
    log.info(f"  Total bytes:    {stats['bytes']:,}")
    log.info(f"  Total MB:       {stats['bytes'] / 1024 / 1024:.1f}")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
