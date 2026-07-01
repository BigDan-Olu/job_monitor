import requests
from bs4 import BeautifulSoup

from config import HEADERS, TIMEOUT


def get_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)

        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        return soup
    except requests.exceptions.RequestException:
        print("Failed to download {url}")
        print(error)
        return None
    soup = get_page(url)
