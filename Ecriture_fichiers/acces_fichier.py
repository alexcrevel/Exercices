import pickle

score = {
  "joueur 1":    5,
   "joueur 2":   35,
   "joueur 3":   20,
   "joueur 4":    2,
}

with open("Ecriture_fichiers/fichier.txt", "wb") as donnees:
    mon_pickler = pickle.Pickler(donnees)
    mon_pickler.dump(score)

with open("Ecriture_fichiers/fichier.txt", "rb") as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recup = mon_depickler.load()

print(score_recup)