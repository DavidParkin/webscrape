#!/usr/bin/env python
# encoding: utf-8

import os
import argparse
import pickle
import pprint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'http://www.theguardian.com/crosswords/crosswords+profile/rufus'


browser = None


def main():
    doneList = ['26616', '26598']
    pprint.pprint(doneList)

    parser = argparse.ArgumentParser(description="Select and display "
                                     "or print Guardian crosswords")
    parser.add_argument('--setter', dest='setter', required=True)
    parser.add_argument('--count', default=5, dest='count', type=int, help="n"
                        "number of crosswords")
    args = parser.parse_args()
    print (args.setter)

    pkl_file = open('xwordDone.txt', 'rb')

    doneList = pickle.load(pkl_file)
    pprint.pprint(doneList)
    global browser
    browser = webdriver.Firefox()
    browser.get(url)
    links = browser.find_elements_by_partial_link_text('Cryptic crossword No')
    pages = []
    for link in links:
        if args.count == 0:
            break
        print('before get href')
        href = (link.get_attribute('href'))
        print(href)
        xwordNumber = os.path.basename(link.get_attribute('href'))
        if xwordNumber not in doneList:
            print(xwordNumber)
            #href = displayXword(link.get_attribute('href'))
            pages.append(href)
            print('return')
            args.count = args.count - 1
        else:
            links.remove(link)

    for page in pages:
        displayXword(page)

    output = open('xwordDone.txt', 'wb')
    pickle.dump(doneList, output)


def displayXword(url):
    #global browser
    print('display')
    print(url)
    browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
    browser.get(url)


if __name__ == "__main__":
    main()
