from scraper import get_page
from parser import extract_jobs


url = "https://example.com"

soup = get_page(url)


if soup:
    jobs = extract_jobs(soup)
    print(jobs)