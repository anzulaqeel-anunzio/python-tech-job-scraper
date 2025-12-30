# Tech Job Board Scraper (Python)

A Python web scraper designed to extract job listings from a mock tech job board.

> [!NOTE]
> This project is designed for educational purposes. It targets a mock HTML structure common to job boards like "Remote OK" or "Hacker News Hiring". Always respect `robots.txt` and Terms of Service when scraping real sites.

## Features

-   **Job Extraction**: Parses job titles, companies, locations, and timestamps.
-   **CSV Export**: Saves scrapped data to a structured CSV file.
-   **Rate Limiting**: Includes delay to be polite to servers.
-   **BeautifulSoup**: Robust HTML parsing.

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python run_scraper.py
```

## Configuration

Edit `job_scraper/config.py` to change the target URL and selectors (currently set to scrape `remoteok.com` as an example demo).

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
