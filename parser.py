def extract_jobs(soup):
    jobs = []

    job_cards = soup.find_all("article", class_="job")
    BASE_URL = "https://jobs.workable.com"
    link = BASE_URL + card.find("a")["href"]
    

    jobs = extract_jobs(soup)
    jobs = soup.find_all("div", class_="job_card")
    for job in jobs:
        title = job.find("h2").text
        location = job.find("span").text
        link = job.find("a")["href"]
        
        job_data.append(
            "title": title,
            "location": location,
            "link": link
        )
    return jobs