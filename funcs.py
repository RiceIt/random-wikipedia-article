import wikipediaapi
import requests
from bs4 import BeautifulSoup


def get_page(language):
    wiki_wiki = wikipediaapi.Wikipedia(str(language))
    url = f"https://{language}.wikipedia.org/wiki/Special:Random"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'lxml')
    title = soup.find(class_="firstHeading").text
    page = wiki_wiki.page(title) 
    return f'{title}\n{page.fullurl}'

