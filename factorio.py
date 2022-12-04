import json
from pathlib import Path

diagram = []

icons = json.loads(Path('icons.json').read_text())
relational_data = json.load(open('relationship.json'))

for icon, url in icons.items():
    if icon in (
            'STONE',
            'WOOD',
            'IRON_ORE',
            'COPPER_ORE',
            'URANIUM_ORE',
    ):
        diagram.append(fr"{fr'{icon}(( ':30}<img src='{url:100}' /> ))")
for icon in relational_data.keys():
    diagram.append(fr"{fr'{icon}(( ':30}<img src='{icons[icon]:100}' /> ))")

diagram.append('\n\n')

for parent, children in relational_data.items():
    for child in children:
        diagram.append(f'{child:30} --> {parent}')

with open('factorio.md', 'w') as f:
    f.write('```mermaid\n')
    f.write('graph TD\n\n')

    for inst in diagram:
        f.write(f"{inst}\n")

    f.write('\n\n\n```\n')
