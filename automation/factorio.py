import json
from pathlib import Path

icons = json.loads(Path('icons.json').read_text())
recipe_data = json.load(open('recipes.json'))

icons_created = []

target_items = ['LOGISTIC_SCIENCE_PACK']


def create_recipe(target_items, recipe_data, nodes, diagram):
    for item in target_items:
        if item not in recipe_data:
            return
        nodes[item] = f"{item}(( <img src='{icons[item]}' /> ))"
        for ingredient in recipe_data[item]:
            nodes[
                ingredient] = f"{ingredient}(( <img src='{icons[ingredient]}' /> ))"
            try:
                diagram[item].append(ingredient)
            except KeyError:
                diagram[item] = [
                    ingredient,
                ]
            create_recipe([
                ingredient,
            ], recipe_data, nodes, diagram)


nodes = {}
diagram = {}

target_items = [
    'LOGISTIC_SCIENCE_PACK', 'AUTOMATION_SCIENCE_PACK',
    'MILITARY_SCIENCE_PACK', 'CHEMICAL_SCIENCE_PACK',
    'PRODUCTION_SCIENCE_PACK', 'UTILITY_SCIENCE_PACK', 'ROCKET_SILO'
]
# target_items = [
#     'ROCKET_SILO',
# ]

create_recipe(target_items, recipe_data, nodes, diagram)

with open('factorio.md', 'w') as f:
    f.write('```mermaid\n')
    f.write('graph TD\n\n')

    for node in nodes.values():
        f.write(f"{node}\n")

    f.write('\n\n')

    for product, ingredients in diagram.items():
        for ingredient in set(ingredients):
            f.write(f"{ingredient:50} --> {product}\n")

    f.write('\n\n\n```\n')
