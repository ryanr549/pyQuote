"""scraping functions"""
import re
import time
import random
import requests
from bs4 import BeautifulSoup

def scrap_quotes(subject):
    """subject: topic you'd like to search in wikiquote site"""
    # headers = {'user-agent':
    #           'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'}
    # specify header as linux mozilla firefox browser
    url = 'https://en.wikiquote.org/wiki/' + subject
    print(url)
    r = requests.get(url)
    bs = BeautifulSoup(r.text)
    # locate the quotes using their parent element
    div = bs.find("div", {"class": "mw-parser-output"})
    # if the keyword is improper(no quote is found), return None
    if type(div) == type(None):
        return None
    quotes = div.find("h2", recursive=False).parent
    lines = quotes.findAll("ul", recursive=False)
    return lines

def scrap_unsplash(keyword):
    """keyword: used to find pics on unsplash.com"""
    # headers = {'user-agent':
    #            'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'}
    # specify header as linux mozilla firefox browser
    url = 'https://unsplash.com/s/photos/' + keyword + '?orientation=landscape&color=black'
    bs = BeautifulSoup(requests.get(url).text)
    search = bs.find("div", {"data-test": "search-photos-route"})
    images = search.findAll("figure", {"itemprop": "image"})[0:16]
    if not len(images):
        # if no image is found
        url = 'https://unsplash.com/s/photos/' + keyword + '?orientation=landscape&color=black_and_white'
        bs = BeautifulSoup(requests.get(url).text)
        search = bs.find("div", {"data-test": "search-photos-route"})
        images = search.findAll("figure", {"itemprop": "image"})
    image_list = []
    for image in images:
        # find images source url in the search result page
        srcset = image.find("img")['srcset']
        # use regular expression to extract a 2k image source url
        pattern = re.compile(r'https?:\/\/[\w.\/\-?=&%]+\s2[0-9][0-9][0-9]w')
        src, _, _ = pattern.search(srcset).group().partition(' ')
        # extract image_url from the string using partition() method
        image_list.append(src)
        # control the request frequency to mimic a normal browser user
    return image_list
