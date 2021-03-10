import requests, json

link = 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=440&count=3&maxlength=300&format=json'

r = requests.get(link).json()
#print(r)
users = r['appnews']['newsitems']
for users in users:
    print(users['appid'])
    print(users['title'])
    print(users['url'])


