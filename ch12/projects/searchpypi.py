#! python3
# searchpypi.py - Opens several search results.


import requests, sys, webbrowser, bs4


print('Searching...')       # display text while downloading the search result page
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()


# TODO: retrieve top search result links


# TODO: open a browser tab for each result