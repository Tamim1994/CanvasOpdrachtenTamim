leeftijd = input("Wat is je leeftijd?: ")
controle = input("Heb je een Nederlands paspoort?: ")

if int(leeftijd) >= int(18) and controle == str("ja" or "Ja"):
    print("Gefeliciteerd! U bent oud genoeg en hebt een Nederlands paspoort")

else:
    print("U bent helaas niet oud genoeg")