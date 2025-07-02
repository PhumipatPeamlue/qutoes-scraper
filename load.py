"""
Module for loading web page content using requests.
"""
import requests

def load_page(url: str) -> str:
    """
    Fetches the HTML content of the given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the page.
    """
    response = requests.get(url)
    html_content = response.text
    return html_content
