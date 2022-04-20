"""scraping functions"""
import re
import time
import random
import requests
from bs4 import BeautifulSoup

def scrap_quotes(subject):
    """subject: topic you'd like to search in wikiquote site"""
    headers = {'user-agent':
               'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'}
    url = 'https://en.wikiquote.org/wiki/' + subject
    print(url)
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text)
    quotes = bs.find("div", {"id": "bodyContent"}).find("h2").parent
    lines = quotes.findAll("ul", recursive=False)
    for line in lines:
        print(line.get_text())
        print('\n')
    return lines

def scrap_unsplash(keyword):
    """keyword: used to find pics on unsplash.com"""
    headers = {'user-agent':
               'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'}
    url = 'https://unsplash.com/s/photos/' + keyword +'?orientation=landscape'
    bs = BeautifulSoup(requests.get(url, headers=headers).text)
    search = bs.find("div", {"data-test": "search-phtos-route"})
    images = search.findAll("figure", {"itemprop": "image"})[0:16]
    image_list = []
    for image in images:
        # find images source url in the search result page
        href = image.find("a", {"itemprop": "contentUrl"})['href']
        src_page_url = 'https://unsplash.com' + href
        src_bs = BeautifulSoup(requests.get(src_page_url, headers=headers).text)
        photo_panel = src_bs.find("div", {"data-test": "photos-route"})
        # since the image link is next to the only jscript in the page
        # first find the script then use parent attribute to locate
        # the high-resolution image url
        srcset = photo_panel.find("script").parent.find("img")['srcset']
        # use regular expression to extract a 2k image source url
        pattern = re.compile(r'https?:\/\/[\w.\/\-?=&]+\s2[0-9]+w')
        src = pattern.search(srcset).group()
        image_list.append(src)
        #
        time.sleep(random.random() * 0.1)
    return image_list
