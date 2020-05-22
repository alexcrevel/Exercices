import random
import math
import pickle

client_money = 50
continue_game = True

def play(bet, client_number, money):
    casino_play = random.randrange(49)
    global client_money
    if casino_play == 0:
        client_money -= client_bet
        print("Vous avez joué le ", client_number, ", la boule est tombée sur le ", casino_play, ", vous avez donc perdu votre mise. Il vous reste", client_money, "$")
    elif casino_play % 2 == 0 and client_number % 2 == 0:
        client_money += math.ceil(client_bet/2)
        print("Vous avez joué le ", client_number, ", la boule est tombée sur le ", casino_play, ", les 2 nombres étant pairs, vous avez donc gagné la moitié de votre mise. Il vous reste", client_money, "$")
        
    elif casino_play % 2 != 0 and client_number % 2 != 0:
        client_money += math.ceil(client_bet/2)
        print("Vous avez joué le ", client_number, ", la boule est tombée sur le ", casino_play, ", les 2 nombres étant impairs, vous avez donc gagné la moitié de votre mise. Il vous reste", client_money, "$")
        
    elif casino_play == client_number:
        client_money += client_bet*3
        print("Vous avez joué le ", client_number, ", la boule est tombée sur le ", casino_play, ", vous avez donc gagné 3 fois votre mise. Il vous reste", client_money, "$")
        
    else:
        client_money -= client_bet
        print("Vous avez joué le ", client_number, ", la boule est tombée sur le ", casino_play, ", vous avez donc perdu votre mise. Il vous reste", client_money, "$")

def save_game(name, money):
    score = {}
    with open('donnees', 'rb') as score_r:
       score = pickle.load(score_r)
    score[name] = money
    with open('donnees', 'wb') as score_w:
        pickle.dump(score, score_w)

def resume_game(name):
    list_users = {}
    with open('donnees', 'rb') as user:
        my_unpickler = pickle.Unpickler(user)
        list_users = my_unpickler.load()
    for key,value in list_users.items():
        if name == key:
            return True, value
    else:
        return False  


name = input("Bonjour, bienvenue au casino. Quel est votre nom? (10 caracteres maximum)")
name = name[:10]
result = resume_game(name)
print(result)
if result[0]:
    print("Vous voila de retour {} !".format(name))
    client_money = result[1]
while continue_game:
    try:   
        print("{}, vous avec actuellement {}$".format(name, client_money))
        client_bet = int(input("Entrer votre mise : "))
        client_number = int(input("Entrer votre nombre : "))
        while client_bet<=0 or client_bet>client_money or client_number<1 or client_number>49:
            print("Mise incorrecte, réessayez")
            client_bet = int(input("Entrer votre mise : "))
            client_number = int(input("Entrer votre nombre : "))
        play(client_bet, client_number, client_money)
        
        if(client_money == 0):
            print("Vous quittez le casino sans un sou")
            continue_game = False

        else:
            user_choice = input("Voulez vous continuer à jouer? Appuyer sur O pour quitter la table")
            if user_choice.lower() == "o":
                print("Vous quittez le casino avec ", client_money, "$")
                save_game(name, client_money)
                continue_game = False

    except ValueError:
        print("Saisie incorrecte, réessayez")
