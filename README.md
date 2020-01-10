# pagescraper
Python script that scrapes a web page for all its URLs and presents them in a text file

Feel free to change the URL in scraper.py by changing the url variable
```
url = "YOUR URL HERE"
website = requests.get(url) # 200 if successful
page = BeautifulSoup(website.text, "html.parser")
```

Or use the default website, which is tanjoshua.github.io
