import wikipediaapi
import requests
import urllib.parse
from bs4 import BeautifulSoup


def get_page(language):
    wiki_wiki = wikipediaapi.Wikipedia(str(language))
    url = f"https://{language}.wikipedia.org/wiki/Special:Random"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'lxml')
    title = soup.find(class_="firstHeading").text
    page = wiki_wiki.page(title)
    page_url = page.fullurl
    if language == 'ru':
        page_url = urllib.parse.unquote(page_url)
    return f'{title}\n{page_url}'

