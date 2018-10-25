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

    def shoot(message, name):
        reg = re.compile("\.shoot \w")

        l1 = "+--^----------,--------,-----,--------^-,\n"
        l2 = "| |||||||||   `--------'     |          O        BANG BANG " + name + " SHOT " + message[7:] + "!\n"
        l3 = " +---------------------------^----------|\n"
        l4 = "  `\_,-------, _________________________|\n"
        l5 = "    / XXXXXX /'|       /'\n"
        l6 = "   / XXXXXX /  `\    /'\n"
        l7 = "  / XXXXXX /`-------'\n"
        l8 = " / XXXXXX /\n"
        l9 = "/ XXXXXX /\n"
        l10 = "(________(\n"
        l11 = " `------'\n"

        if reg.search(message):
            return l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11
        else:
            return "Eff3 doesn't know who to shoot!", "\n"

    def rainbow(message):
        reg = re.compile("\.rainbow \w")

        if reg.search(message):
            message = message[9:]

        #return ''.join('' + str(divmod(n, 14)[1] + 1) + message[n] for n in range(0, len(message)))

        return "This feature isn't ready yet"

    def green(message, name):
        reg = re.compile("\.green \w")

        if reg.search(message):
            return name + " rolls a fat spliff for " + message[7:] + " and sends it sliding down the bar. " + message[7:] + " smiles and lights it up."
        else:
            return name + " rolls a fat spliff but has no one to pass it to!"