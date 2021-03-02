import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }

url = 'https://store.steampowered.com/'
content = requests.get(url, headers=headers)
soup = BeautifulSoup(content.text, 'html.parser')
steam = soup.findAll('div', attrs={'class':'carousel_items'})
for steams in steam:
    print(steams)
#print(content)

