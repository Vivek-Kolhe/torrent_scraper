import requests
import re
from bs4 import BeautifulSoup
import pyperclip
import pprint

def torrent1337x(query):
	USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
	headers = {"user-agent": USER_AGENT}
	response = requests.post("https://1337x.proxyserver.gq/sort-search/" + query + "/seeders/desc/1/", headers = headers)
	some_data = BeautifulSoup(response.content, "html.parser")
	tab = some_data.find("table", attrs = {"class" : "table-list table table-responsive table-striped"})
	data, link = [], []

	rows = tab.find_all("tr")
	for row in rows:
	    columns = row.find_all("td", attrs = {"class" : "coll-1 name"})
	    for column in columns:
	        links = column.find_all("a", class_ = None, href = True)
	        for l in links:
	            link.append("https://1337x.proxyserver.gq" + l["href"])

	for index, l in enumerate(link):
	    new_response = requests.post(l, headers = headers)
	    new_soup = BeautifulSoup(new_response.content, "html.parser")
	    title = new_soup.find("div", attrs = {"class" : "box-info-heading clearfix"}).get_text()
	    seeds = new_soup.find("span", attrs = {"class" : "seeds"}).get_text()
	    leeches = new_soup.find("span", attrs = {"class" : "leeches"}).get_text()
	    size = new_soup.find("span", class_ = None, text = re.compile(r"([0-9].[0-9] [A-Z])")).get_text()
	    magnet = new_soup.find("a", href=re.compile(r'[magnet]([a-z]|[A-Z])\w+'), class_=True).attrs["href"]
	    data.append({"Index" : index+1, "Title" : title[1:-2], "Magnet" : magnet, "Size" : size, "Seeders" : seeds, "Leechers" : leeches})
	return data