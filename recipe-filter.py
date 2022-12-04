import json
from pathlib import Path

recipes = json.loads(Path('recipes-import.json').read_text())

data = {}
for item in recipes:
    data[item['name'].upper().replace('-', '_')] = [
        i['name'].upper().replace('-', '_') for i in item['ingredients']
    ]

with open('recipes.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=4, sort_keys=True))
