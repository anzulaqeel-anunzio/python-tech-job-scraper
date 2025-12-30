# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import pandas as pd
from job_scraper.scraper import scrape_jobs
import time

def main():
    print("Starting Tech Job Board Scraper...")
    
    try:
        jobs = scrape_jobs()
        
        if not jobs:
            print("No jobs found.")
            return

        df = pd.DataFrame(jobs)
        filename = f"jobs_{int(time.time())}.csv"
        df.to_csv(filename, index=False)
        
        print(f"Successfully scraped {len(jobs)} jobs.")
        print(f"Saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
