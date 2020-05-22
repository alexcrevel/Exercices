while True:
    try:
        user_year = int(input("Entrez une annee : "))
        if user_year % 400 == 0 or (user_year % 4 == 0 and user_year % 100 != 0):
            print("Bisextile")
        else:
            print('Non bisextile')
    except ValueError:
        print("Entree incorrecte")