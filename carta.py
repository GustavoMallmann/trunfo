import random
from configsTrunfo import tipos


class Carta:

    def __init__(self):
        self.stats = []
        type_int = random.randint(0, len(tipos) - 1)
        self.type = tipos[type_int]

        for _ in tipos:
            self.stats.append(random.randint(1, 30))
