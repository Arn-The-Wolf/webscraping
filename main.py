import requests
from bs4 import BeautifulSoup
import pandas as pandas

url = "https://books.toscrape.com/catalogue/page-1.html"

page = requests.get(url)

print(page.text)

soup = BeautifulSoup(page.text, "html.parser")

print(soup.title.text)