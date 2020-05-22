import random
import json
import pickle


def choose_word():
    with open('Exercices/Pendu/words.json') as file:
        data = json.load(file)
    word = random.choice(data)
    return word

def play_char(char, word):
    temp_word = ""
    char_founded = False
    for letter in word:
        if letter in char:
            temp_word += letter
            if char[-1] == letter:
                char_founded = True
        else:
            temp_word += "*"
    return char_founded, temp_word

def save_game(name, points):
    score = {}
    with open('Exercices/Pendu/tableau_scores', 'rb') as score_r:
        score = pickle.load(score_r)
        if name in score:
            score[name] += points 
        else:
            score[name] = points
    
    with open('Exercices/Pendu/tableau_scores', 'wb') as score_w:
        pickle.dump(score, score_w)
    
    return score[name]                

def resume_game(name):
    list_users = {}
    with open('Exercices/Pendu/tableau_scores', 'rb') as user:
        list_users = pickle.Unpickler(user).load()
    for key,value in list_users.items():
        if name == key:
            return True, value
    else:
        return False, 0
