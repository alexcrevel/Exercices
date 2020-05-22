while True:
  try:
    user_number = int(input("Entrer un nombre positif : "))
    count = 2
    number_divised = user_number
    list = []

    while (count < user_number):
      if (user_number % count == 0):
        list.append(count)
      count += 1
    
    if (len(list) == 0):
      print("Aucun diviseur propre")
    else:
      print("Diviseurs propres sans répétition de ", user_number, " : ", list, " soit ", len(list), "diviseurs propres")
    break
  except ValueError:
    print("Données erronées")