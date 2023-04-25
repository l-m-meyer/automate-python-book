#! python3
# downloadXkcd.py - Downloads every single XKCD comic.


import requests, os, bs4


url = 'https://xkcd.com'            # starting url
os.mkdirs('xkcd', exist_ok=True)    # store comics in ./xkcd

while not url.endswith('#'):
    # TODO: download the page


    # TODO: find the url of the comic image


    # TODO: download the image


    # TODO: save the image to ./xkcd


    # TODO: get the prev button's url


print('Done.')