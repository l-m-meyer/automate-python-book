#! python3
# savingDownloadedFiles.py


import requests


res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')     # need to write binary data to maintain unicode encoding of text

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()