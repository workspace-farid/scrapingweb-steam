from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def top_sellers():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
        }
    link = 'https://store.steampowered.com/games/TopSellers#p=0&tab=TopSellers'

    request = requests.get(link, headers=headers)
    # print(request)
    soup = BeautifulSoup(request.text, 'html.parser')
    top_sellers = soup.findAll('a', attrs={'class': 'tab_item'})

    return render_template('grid_template.html', top_sellers=top_sellers)

if __name__== '__main__':
    app.run(debug=True)
