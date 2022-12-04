import json

import requests
from bs4 import BeautifulSoup

r = requests.get('https://wiki.factorio.com/Materials_and_recipes')

soup = BeautifulSoup(r.text, 'html.parser')

icons = {}
for img in soup.find_all('img'):
    try:
        img_url = f"https://wiki.factorio.com{img['src']}"
        icons[img_url.split('/')[-1].split('px-')[-1].upper()[:-4]] = img_url
    except KeyError:
        pass

    with open('icons.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(icons, indent=4, sort_keys=True))
