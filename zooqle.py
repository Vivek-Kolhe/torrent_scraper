import requests
from bs4 import BeautifulSoup
import pprint

query = input("Search something? ").replace(" ", "+")
url = "https://zooqle.unblockit.top/search?q=" + query
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
tr = soup.select("div.panel-body tr")[1:]
titles = [item.a.text for item in tr]
magnets = soup.find_all(title = "Magnet link")
size = soup.find_all(class_ = "progress-bar prog-blue prog-l")
seeders = soup.find_all(class_ = "progress-bar smaller prog-green prog-l")
leechers = soup.find_all(class_ = "progress-bar smaller prog-yellow prog-r")
data = []

for i in range(len(tr)):
    data.append({"Index": i+1, "Title": titles[i], "Size": size[i].text, "Seeders / Leechers": seeders[i].text + " / " + leechers[i].text, "Magnet": magnets[i]["href"]})

pprint.pprint(data)