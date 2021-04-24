#from telebot.credentials import bot_token, bot_user_name, URL
#import telegram
#from flask import Flask, request
import re
import wikipediaapi
import requests
from bs4 import BeautifulSoup


def get_page():
    wiki_wiki = wikipediaapi.Wikipedia('en')
    url = "https://en.wikipedia.org/wiki/Special:Random"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'lxml')
    title = soup.find(class_="firstHeading").text
    page = wiki_wiki.page(title) 
    return f'{title}\n{page.fullurl}'
