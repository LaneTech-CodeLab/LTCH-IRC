import random
import re

item = []
adj = []

with open("items.txt") as fd:
    for lines in fd.readlines():
        if lines.find("\n") != -1:
            lines = lines.strip("\n")

        item.append(lines)

with open("adj.txt") as fd:
    for lines in fd.readlines():
        if lines.find("\n") != -1:
            lines = lines.strip("\n")

        adj.append(lines)


class Commands:
    def __init__(self, message, name):
        self.message = message
        self.name = name

    def hello(name):
        return "Hello " + name + '!'

    def vend(message):
        reg = re.compile("\.vend \w")

        if reg.search(message):
            return "Vending... a " + random.choice(adj) + " " + random.choice(item) + " for " + message[6:] + "!\n"
        else:
            return "Vending... a " + random.choice(adj) + " " + random.choice(item) + "!\n"

