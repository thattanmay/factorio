import itertools
import json
from pathlib import Path

icons = json.loads(Path("icons.json").read_text())
recipe_data = json.load(open("recipes.json"))


def get_recipe(items, recipe_data):
    for item in items:
        if item not in recipe_data:
            return
        for ingredient in recipe_data[item]:
            yield ingredient, item
            yield from get_recipe(
                [
                    ingredient,
                ],
                recipe_data,
            )


data = {}
for ingredient, item in set(
    list(
        get_recipe(
            [
                "FAST_INSERTER",
                "LONG_HANDED_INSERTER",
                "TRANSPORT_BELT",
                "STEEL_FURNACE",
                "LAB",
                "AUTOMATION_SCIENCE_PACK",
                "LOGISTIC_SCIENCE_PACK",
            ],
            recipe_data,
        )
    )
):
    try:
        data[ingredient].append(item)
    except KeyError:
        data[ingredient] = [
            item,
        ]


with open("intermittent.md", "w", encoding="utf-8") as f:

    inst = []
    chest_count = 0
    for ingredient, products in data.items():
        if len(products) > 3:
            for i, product in enumerate(products):
                if (i - 1) // 3 != i // 3:
                    chest_count += 1
                    inst.append([ingredient, f"IRON_CHEST{('00' + str(chest_count))[-3:]}"])
                inst.append([f"IRON_CHEST{('00' + str(chest_count))[-3:]}", product])
        else:
            for product in products:
                inst.append([ingredient, product])

    f.write(f"```mermaid\n\ngraph TD\n\n\n")

    for node in set(itertools.chain.from_iterable(inst)):
        if node.startswith("IRON_CHEST"):
            f.write(f"{node}(( <img src='{icons['IRON_CHEST']}' /> ))\n")
        f.write(f"{node}(( <img src='{icons['IRON_CHEST']}' /> ))\n")
    f.write("\n\n\n")
    for ingredient, product in inst:
        f.write(f"{ingredient:50} --> {product}\n")

    f.write("\n\n```\n")
