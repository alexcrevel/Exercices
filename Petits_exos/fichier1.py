# -*- coding: utf8 -*-

import random
import json

def read_values_from_json(file, key):
    values = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
    return values

def get_random_item_in(tab):
    rand_num = random.randint(0, len(tab)-1)
    return tab[rand_num]

def show_random_quote():
    all_tab = read_values_from_json("quotes.json", "quote")
    return get_random_item_in(all_tab)

def show_random_character():
    all_tab = read_values_from_json("characters.json", "character")
    return get_random_item_in(all_tab)



# Show random quote
user_answer = input("Taper entrée pour connaitre une citation")
while user_answer != 'B':
    print("{} a dit : {}".format(show_random_character() , show_random_quote()))
    user_answer = input("Taper entrée pour connaitre une autre citation")
# - show another quote
