from operator import itemgetter

inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]
new_invent = []
for number in inventaire:
    fruit, quantite = number
    number = (quantite, fruit)
    new_invent.append(number)
new_invent = sorted(new_invent, reverse=True)
print(new_invent)