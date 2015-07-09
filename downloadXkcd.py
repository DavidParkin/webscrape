#! /usr/bin/env python
# downloadXkcd.py - Downloads every single XKCD comic.

import requests
import os
import bs4
import sys

url = 'http://xkcd.com'         # starting url
os.makedirs('xkcd', exist_ok=True)      # store comics in ./xkcd
while not url.endswith('#'):
    # TODO: Download the page
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # TODO: Find the URL of the comic image.
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        print(comicUrl)
        comicUrl = 'http:' + comicUrl
        print(comicUrl)
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        try:
            res = requests.get(comicUrl)
        except Exception as badurl:
            print('Malformed Url: %s' % (badurl))
            sys.exit()
        try:
            res.raise_for_status()
        except Exception as exc:
            print('There was a problem: %s' % (exc))

    # TODO: Download the image

    # TODO: Save the image to ./xkcd.
    # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # TODO: Get the Prev button's url.
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

    boll = True


print('Done.')
