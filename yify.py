import requests
from bs4 import BeautifulSoup
import pyperclip
import pprint

query = input("Search Movie: \n").replace(" ", "-")
response = requests.get("https://yts.mx/movies/" + query)
soup = BeautifulSoup(response.text, "html.parser")
data = soup.select(".magnet")
size = soup.select(".quality-size")
qs = [i.getText(".quality-size") for i in size]
qua, si = qs[::2], qs[1::2]
torrents = []

def getTorrent(data, size):
    for index, item in enumerate(data):
        title = item.get("title")[9:]
        magnet = item.get("href")
        quality = qua[index]
        size = si[index]
        torrents.append({"Index" : index ,"Title" : title, "Magnet" : magnet, "Quality" : quality, "Size" : size})
    return torrents

pprint.pprint(getTorrent(data, size))

ind = int(input("\nEnter the index of magnet you want to copy:\n"))
try:
    pyperclip.copy(torrents[ind]["Magnet"])
    print("\nCopied magnet to your clipboard. :)")
except Exception:
    print("Check index again.")
