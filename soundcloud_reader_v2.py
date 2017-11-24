import urllib.request as urllib
from bs4 import BeautifulSoup
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def readWebpageOld(url):

    webpage = web.urlopen(url)
    for line in webpage:
        line = line.decode('utf-8')
        print(line)

def readWebpageNew(url):
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r, "html.parser")
    print(type(soup))
    print(soup.prettify())

def readWebpageNew2(url):
    browser = webdriver.Chrome("C:/Users/Ben Liepert/AppData/Local/Microsoft/Windows/FileHistory/Data/693/C/Users/Ben Liepert/Desktop/chromedriver_win32")

    browser.get(url)
    time.sleep(1)

    elem = browser.find_element_by_tag_name("body")

    no_of_pagedowns = 20

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1

    post_elems = browser.find_elements_by_class_name("post-item-title")

    for post in post_elems:
        print(post.text)

        


def main():
    url = 'https://soundcloud.com/benliepert/sets/cruise-tunes'
    #readWebpageOld('https://soundcloud.com/benliepert/sets/cruise-tunes')
    #readWebpageNew(url)
    readWebpageNew2(url)
main()
