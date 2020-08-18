import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.thehindu.com/real-estate/")
r2 = requests.get("https://www.99acres.com/articles/hyderabad-property-news")
soup = BeautifulSoup(r.content, 'html.parser')
headings = soup.find_all('h3')
soup1 = BeautifulSoup(r2.content, 'html.parser')
headings1 = soup1.find_all('h3')