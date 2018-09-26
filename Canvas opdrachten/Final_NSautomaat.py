def standaardprijs(afstandKM):
    treinrit = (0.80 * afstandKM)
    prijs = float(15) + (afstandKM * 0.60)

    if afstandKM > 50:
        prijs = float(15) + ((afstandKM - 50) * (0.60))
        return format(prijs, ".2f")
    elif afstandKM < float(0):
        prijs = float(0)
        return format(prijs, ".2f")
    else:
        return format(treinrit, ".2f")


def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if reisDag in weekendrit[0:] and (leeftijd < str(12) or leeftijd >= str(65)):
        prijs = (float(prijs) - (float(prijs) * 0.35))
        return "€" + format(prijs, ".2f")
    elif reisDag not in weekendrit[0:] and leeftijd < str(12) or leeftijd >= str(65):
        prijs = (float(prijs) - (float(prijs) * 0.30))
        return "€" + format(prijs, ".2f")





# werkdagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
weekendrit = ["zaterdag", "zondag"]
leeftijd = input("Wat is uw leeftijd?: ")
reisDag = str(input("Op welke dag gaat u reizen?: "))
afstandKM = float(input("Voer aantal kilometers in tot uw bestemming: "))
print("Uw reis kost:", ritprijs(leeftijd, weekendrit, afstandKM))

