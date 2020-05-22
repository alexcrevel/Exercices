while True:
  try:
    user_number = int(input("Entrer un nombre positif : "))
    if (user_number % 2 == 0):
      print("PAIR")
    else:
      print("IMPAIR") 
    break
  except ValueError:
    print("Données erronées")