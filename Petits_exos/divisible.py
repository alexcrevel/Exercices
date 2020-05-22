while True:
  try:
    user_number = int(input("Entrer un nombre positif : "))
    count = 0
    number_divised = user_number
    while (number_divised > 2):
      number_divised = number_divised // 2
      count += 1
    
    print(count)
    break
  except ValueError:
    print("Données erronées")