# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

# Configuration for the scraper
# Developed for Anunzio International by Anzul Aqeel

TARGET_URL = "https://remoteok.com"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# CSS Selectors (specific to RemoteOK for this demo)
SELECTORS = {
    "job_row": "tr.job",
    "title": "h2[itemprop='title']",
    "company": "h3[itemprop='name']",
    "location": "div.location",
    "salary": "div.location" # Sometimes salary is mixed in location divs in this specific site structure
}

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
