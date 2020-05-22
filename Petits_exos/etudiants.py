import operator

class Etudiant:

  def __init__(self, nom, age, moyenne):
    self.nom = nom
    self.age = age
    self.moyenne = moyenne

  def __repr__(self):
    return "<Etudiant {} (age : {}, moyenne : {}".format(self.nom, self.age, self.moyenne)

etudiants = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]

print(sorted(etudiants, key=operator.attrgetter("moyenne")))