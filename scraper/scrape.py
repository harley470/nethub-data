import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime


DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "nethub.json")


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


BASE_URL = "https://supernetball.com.au"




def get_soup(url):
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")




def scrape_ladder():
    try:
        soup = get_soup(f"{BASE_URL}/ladder")
        ladder = []
        rows = soup.select("table tbody tr, .ladder-row, [class*='ladder'] tr")
        for i, row in enumerate(rows):
            cols = row.find_all(["td", "th"])
            if len(cols) < 5:
                continue
            texts = [c.get_text(strip=True) for c in cols]
