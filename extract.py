"""
Module for extracting quotes from HTML content using BeautifulSoup.
"""
from bs4 import BeautifulSoup, Tag
from typing import Tuple

def extract_quotes(html_content: str, domain: str) -> list:
    """
    Extracts quotes from the provided HTML content.

    Args:
        html_content (str): The HTML content of the page.
        domain (str): The base domain to construct author links.

    Returns:
        list: A list of dictionaries, each representing a quote.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    quotes_list = []

    # Find all quote blocks in the HTML using CSS selectors
    for quote_div in soup.select("div.quote"):
        text_elem = quote_div.select_one("span.text")
        author_name_elem = quote_div.select_one("small.author")
        author_link_elem = quote_div.select_one("a")
        tags = [tag.text for tag in quote_div.select("a.tag")]

        text = text_elem.text if text_elem else ""
        author_name = author_name_elem.text if author_name_elem else ""
        author_link = author_link_elem["href"] if author_link_elem and author_link_elem.has_attr("href") else ""
        author_link_str = author_link.lstrip("/") if isinstance(author_link, str) else ""

        quotes_list.append({
            "text": text,
            "author": {
                "name": author_name,
                "link": f"{domain}/{author_link_str}" if author_link_str else ""
            },
            "tags": tags,
        })

    return quotes_list
