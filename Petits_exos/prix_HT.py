
price_tax_free = input("Entrez un prix HT : ")
try:
  while price_tax_free != "O":
    
    if float(price_tax_free) > 0:
      price_tax_free = float(price_tax_free)
      price_with_tax = ((price_tax_free * 19.6)/100) + price_tax_free
      print(price_with_tax)
    else:
      print("valeur incorrecte")
    
    price_tax_free = input("Entrez un prix HT : ")
    pass

except ValueError:
  print("Erreur de saisie")
  pass


print("Bye")  
quit