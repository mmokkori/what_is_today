import requests
from bs4 import BeautifulSoup

url = "https://www.nnh.to/08/10.html"

r = requests.get(url)

soup = BeautifulSoup(r.content,features="html.parser")

h4_tags = soup.find_all("h4",class_="holiday")

print(h4_tags[0])