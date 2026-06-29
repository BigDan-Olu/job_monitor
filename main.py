from scraper import get_page


def main():
    url = "https://example.com"
    soup = get_page(url)
    print(soup.title.text)


if __name__ == "__main__":
    main()
