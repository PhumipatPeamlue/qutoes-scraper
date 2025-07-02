"""
Module for saving web page content to a local HTML file.
"""
import requests

def save_page_to_file(url: str, filename: str) -> None:
    """
    Fetches the HTML content from the given URL and saves it to a file.

    Args:
        url (str): The URL to fetch.
        filename (str): The base filename (without extension) to save the HTML content.
    """
    response = requests.get(url)
    html_content = response.text

    path = f"{filename}.html"
    with open(path, "w") as file:
        file.write(html_content)
