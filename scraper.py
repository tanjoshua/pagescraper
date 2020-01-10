import requests # for making HTTP requests
import urllib.request
from bs4 import BeautifulSoup # for parsing html

url = "https://tanjoshua.github.io/"
website = requests.get(url) # 200 if successful
page = BeautifulSoup(website.text, "html.parser")

# gets all links
all_urls = []
for link in page.find_all("a"):
  all_urls.append(link.get('href'))

# creates document
doc = open("contents", "w")

# writes each url to the list
doc.write("URLs\n")
for link in all_urls:
  doc.write(link + "\n")
doc.close()