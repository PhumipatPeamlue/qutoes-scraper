"""
Main script for scraping quotes from quotes.toscrape.com and saving them to a JSON file.
"""
import json
import load
import extract
import time

if __name__ == "__main__":
    domain = "https://quotes.toscrape.com"
    all_quotes = []

    # Scrape quotes from the first 10 pages
    for page_index in range(10):
        page_number = page_index + 1
        print(f"Scraping quotes from page {page_number}...")

        url = f"{domain}/page/{page_number}/"
        html_content = load.load_page(url)
        quotes = extract.extract_quotes(html_content, domain)

        print(f"  {len(quotes)} quotes scraped from page {page_number}.")
        all_quotes.extend(quotes)

        print("  Sleeping for 5 seconds to be polite to the server...")
        time.sleep(5)

    # Save all quotes to a JSON file
    with open("quotes.json", "w") as file:
        json.dump(all_quotes, file, indent=4)

    print(f"Successfully saved {len(all_quotes)} quotes to 'quotes.json'.")

