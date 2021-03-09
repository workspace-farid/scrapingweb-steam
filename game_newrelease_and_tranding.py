from uu import encode
import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}

link = 'https://store.steampowered.com/'
r = requests.get(link, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

new_releases = soup.findAll('a', attrs={'class':'tab_item'})
file = open('steamweb.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['Title', 'Price', 'Tags'])

for new_releases in new_releases:
    if(new_releases.find('div', attrs={'class':'tab_item_name'}) !=None):
        title = new_releases.find('div', attrs={'class':'tab_item_name'}).text
    else:
        title = ''
    if(new_releases.find('div', attrs={'class':'discount_final_price'}) !=None):
        price = new_releases.find('div', attrs={'class':'discount_final_price'}).text
    else:
        price = ''
    if(new_releases.find('div', attrs={'class':'tab_item_top_tags'}) !=None):
        tags = new_releases.find('div', attrs={'class':'tab_item_top_tags'}).text
    else:
        tags = ''

    file = open('steamweb.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([title, price, tags])
    file.close()


