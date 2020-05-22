import math

while True:
  try:
    user_R = float(input("Entrez le rayon : "))
    break
  except ValueError:
    print("Rayon incorrect, réessayez")

while True:
  try:
    user_H = float(input("Entrez la hauteur : "))
    break
  except ValueError:
    print("Hauteur incorrecte, réessayez")

volume = (math.pi * user_R**2 * user_H)/3

print (volume)