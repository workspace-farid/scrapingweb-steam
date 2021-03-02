import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
           }
link = 'https://store.steampowered.com/games/TopSellers#p=0&tab=TopSellers'

request = requests.get(link, headers=headers)
#print(request)
soup = BeautifulSoup(request.text, 'html.parser')
top_seller = soup.findAll('a', attrs={'class':'tab_item'})


for top_seller in top_seller:
    print('Judul: ', top_seller.find('div', attrs={'class':'tab_item_name'}).text)
    print('Gambar: ', top_seller.find('div', attrs={'class': 'tab_item_cap'}).find('img'))
    print('Tag_name: ', top_seller.find('div', attrs={'class': 'tab_item_top_tags'}).text)



