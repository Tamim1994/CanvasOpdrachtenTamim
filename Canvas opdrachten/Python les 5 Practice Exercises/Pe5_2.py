leeftijd = input("Wat is je leeftijd?: ")
controle = input("Heb je een Nederlands paspoort?: ")

if int(leeftijd) >= int(18) and controle == ('ja' or 'Ja'):
    print("Gefeliciteerd! U mag stemmen")

else:
    print("U voldoet helaas niet aan de voorwaarden")