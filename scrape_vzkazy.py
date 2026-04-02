#!/usr/bin/env python3
"""Scrape all 744 pages of vzkazy from cervenytrpaslik.cz"""

import re
import sys
import time
import logging
import urllib3
from pathlib import Path

import requests
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "http://www.cervenytrpaslik.cz/"
DELAY = 2
USER_AGENT = "RedDwarfFanClub-KnowledgeBase/1.0"
OUTPUT_DIR = Path.home() / "red-dwarf-skill" / "raw" / "vzkazy"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S", stream=sys.stderr)
log = logging.getLogger("vzkazy")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Remove old bad files
for f in OUTPUT_DIR.glob("vzkazy_page_*.txt"):
    f.unlink()

fetched = 0
failed = 0

for page in range(1, 745):
    if page == 1:
        url = f"{BASE_URL}index.php?id=vzkazy&mnu=0"
    else:
        url = f"{BASE_URL}index.php?id=vzkazy&mnu=0&page={page}"

    try:
        resp = requests.get(url, headers={"User-Agent": USER_AGENT}, verify=False, timeout=30)
        resp.raise_for_status()

        for enc in ["utf-8", "windows-1250", "iso-8859-2", "latin-1"]:
            try:
                html = resp.content.decode(enc)
                if "í" in html or "á" in html:
                    break
            except UnicodeDecodeError:
                continue
        else:
            html = resp.text

        soup = BeautifulSoup(html, "html.parser")
        for tag in soup.find_all(["script", "style", "noscript"]):
            tag.decompose()

        main_td = soup.find("td", attrs={"width": "633"})
        text = (main_td or soup).get_text(separator="\n", strip=False)
        text = re.sub(r"[ \t]+", " ", text)
        lines = [line.strip() for line in text.split("\n")]
        text = "\n".join(lines)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = text.strip()

        path = OUTPUT_DIR / f"vzkazy_page_{page:04d}.txt"
        path.write_text(text, encoding="utf-8")
        fetched += 1

        if page % 50 == 0:
            log.info(f"Page {page}/744 ({fetched} ok, {failed} fail)")

    except Exception as e:
        log.error(f"Page {page}: {e}")
        failed += 1

    time.sleep(DELAY)

log.info(f"DONE: {fetched} fetched, {failed} failed")
