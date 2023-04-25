#! python3
# downloadXkcd.py - Downloads every single XKCD comic.


import requests, os, bs4


url = 'https://xkcd.com'            # starting url
os.mkdirs('xkcd', exist_ok=True)    # store comics in ./xkcd

while not url.endswith('#'):
    # download the page
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # TODO: find the url of the comic image


    # TODO: download the image


    # TODO: save the image to ./xkcd


    # TODO: get the prev button's url


print('Done.')