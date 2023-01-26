import json
import logging
from pathlib import Path

logging.basicConfig(filename="backtrack.log",
                    format='%(message)s',
                    filemode='w',
                    encoding='utf-8')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Position:
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x


class Node:
    def __init__(self, name, center: Position) -> None:
        self.name = name
        self.center = center
        self.right = []
        self.left = []
        self.up = []
        self.down = []


class Factorio:

    aliases = [chr(122 - i) for i in range(26)]
    aliases_dict = []

    def __init__(self, size=50) -> None:
        self.size = size
        self.space = [[' ' for _ in range(self.size)]
                      for _ in range(self.size)]

        self.recipe = json.loads(Path('recipe.json').read_text())

    def insert(self, val, pos: Position):
        pos = Position(pos.y + self.size // 2, pos.x + self.size // 2)
        self.space[pos.y][pos.x] = val

    def display(self):
        for _, r in enumerate(self.space):
            r = ''.join(r).strip()
            if r:
                logger.info(''.join(r))

    def design(self, products: list, pos=Position(0, 0)):

        for p in products:
            if p not in self.aliases_dict:
                self.aliases_dict[p] = self.aliases.pop()
            self.insert(self.aliases_dict[p], pos)


factorio = Factorio()

factorio.design([
    'LOGISTIC_SCIENCE_PACK',
])

factorio.display()