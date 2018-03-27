import requests
from bs4 import BeautifulSoup


r = requests.get('http://www.hanwenbo.top')

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.find(id='content-masonry').header.h2.a.get('href'))


