import requests
import re
from html.parser import HTMLParser
from bs4 import BeautifulSoup

url = 'https://academicaffairs.kennesaw.edu/'
response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, 'lxml')

print(soup.find('div', { 'class' : 'content' }).find('p', recursive=False))