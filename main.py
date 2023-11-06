import requests
from bs4 import BeautifulSoup

try:
    response = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
    response.raise_for_status()  # Raise an exception for HTTP errors
    html = response.text

    # Use BeautifulSoup to parse the HTML and extract text content
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()

    print(text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
