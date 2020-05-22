import functions 

count = 8
success = False
user_char = []
continue_game = True

name = input("Bonjour, bienvenue au jeu du pendu. Quel est votre nom? (10 caracteres maximum)")
name = name.capitalize()[:10]

existant, points = functions.resume_game(name)
if existant:
    print("Vous voila de retour {}, vous avez actuellement {} points".format(name, points))

while True:
    word = functions.choose_word()
    print(word, len(word))
    print("Le mot a trouver fait {} caractères, vous avez droits à {} erreurs".format(len(word), count))


    while count > 0 and success == False:

        user_input = input("Entrez une lettre : ").upper()
        user_input = user_input[:1]
        user_char.append(user_input)
        word_founded, actual_word = functions.play_char(user_char, word)
        if word_founded == False:
            count -= 1
            print("Cette lettre ne fait pas partie ce ce mot. Il vous reste {} chances".format(count))

        if actual_word == word:
            success = True
        print(actual_word)
        if success:
            print("Vous avez réussi a trouver le mot. Vous gagnez {} points.".format(count))
        
    
    if input('Voulez vous continuer à jouer? y/n'.lower()) != 'y':
        break
    
print("Vous partez avec {} points".format(functions.save_game(name, count)))

print("Au revoir")