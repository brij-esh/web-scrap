import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/B"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

text=''
for paragraph in soup.find_all('p'):
    print(paragraph.text)
