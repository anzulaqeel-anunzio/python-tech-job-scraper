# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import requests
from bs4 import BeautifulSoup
import time
import random
from .config import TARGET_URL, USER_AGENT, SELECTORS

def scrape_jobs():
    headers = {
        "User-Agent": USER_AGENT
    }

    print(f"Scraping from: {TARGET_URL}")
    response = requests.get(TARGET_URL, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to load page: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    job_rows = soup.select(SELECTORS["job_row"])
    
    jobs = []
    
    print(f"Found {len(job_rows)} job listings.")

    for row in job_rows[:20]: # Limit to first 20 for demo
        try:
            title = row.select_one(SELECTORS["title"]).text.strip()
            company = row.select_one(SELECTORS["company"]).text.strip()
            
            # Location parsing might vary, grabbing raw text for now
            locations = [loc.text.strip() for loc in row.select(SELECTORS["location"])]
            location_str = ", ".join(locations)

            jobs.append({
                "title": title,
                "company": company,
                "location": location_str
            })
        except AttributeError:
            continue
            
    return jobs

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
