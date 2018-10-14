def standaardprijs(afstandKM):

    """Dit is de functie voor het berekenen van de standaardprijzen"""

    treinrit = (afstandKM * 0.80)
    prijs = 0.00

    if afstandKM < 0:
        prijs = 0.00
    elif afstandKM < 50 and (afstandKM > 0):    #ALS AFSTAND TUSSEN 1-49KM, BETAAL STANDAARDPRIJS
        prijs = treinrit
    elif afstandKM >= 50:
        prijs = float(15) + ((afstandKM - 50) * 0.60)   #ALS AFSTAND GROTER OF GELIJK AAN 50, BETAAL STANDAARD TARIEF
    return format(prijs, ".2f")                         #FUNCTIE RETURNED DE WAARDE VAN PRIJS


def ritprijs(leeftijd, weekendrit, afstandKM):

    """Functie voor het toepassen van de korting bovenop de vaste prijzen"""

    prijs = standaardprijs(afstandKM)

    if (weekendrit == 'nee') and (leeftijd < 12 or leeftijd >= 65): #ALS HET EEN WERKDAG IS EN LEEFTIJD IS X, GEEF KORTING
        prijs = (float(prijs) - (float(prijs) * 0.30))
        return format(float(prijs), ".2f")

    elif (weekendrit == 'ja') and (leeftijd < 12 or leeftijd >= 65): #ALS HET EEN WERKDAG IS EN LEEFTIJD IS X, GEEF KORTING
        prijs = (float(prijs) - (float(prijs) * 0.35))
        return format(float(prijs), ".2f")

    elif (weekendrit == 'nee') and (leeftijd >= 12 or leeftijd >= 65): #ALS HET EEN WERKDAG IS EN LEEFTIJD IS X, GEEF KORTING
        return format(float(standaardprijs(afstandKM)), ".2f")

    elif (weekendrit == 'ja') and (leeftijd >= 12 or leeftijd >= 65): #ALS HET EEN WERKDAG IS EN LEEFTIJD IS X, GEEF KORTING
        prijs = (float(prijs) - (float(prijs) * 0.40))
        return format(float(prijs), ".2f")


def testing(testPrijs):

    """Functie voor het controleren van de outputwaarde van ritprijs(leeftijd, weekendrit, afstandKM)
    en vergelijken met de vooraf ingestelde waarden. De returnwaarde (float) van functie ritprijs wordt in
    variabele testPrijs gestopt, die geef ik dan als argument mee aan functie testing zodat gecontroleerd kan
    worden of de prijzen ook daadwerkelijk kloppen met vooraf ingestelde waarden"""

    #CONTROLEER BIJ ELKE IF STATEMENT OF VOORAF INGESTELDE WAARDES EN DE OUTPUT VAN RITPRIJS OVEREENKOMT

    prijsBepaling = (float(ritprijs(leeftijd,weekendrit,afstandKM)))

    if ritprijs(11,'nee',51) and (testPrijs == float(10.92)):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
                testPrijs,format(testPrijs,".2f"), (testPrijs == float(10.92))))

    elif (ritprijs(11, 'ja', 51)) and (testPrijs == float(10.14)):
      print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
      testPrijs,format(testPrijs,".2f"), (testPrijs == float(10.14))))

    elif (ritprijs(11, 'nee', 49)) and (testPrijs == float(27.44)):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
             testPrijs,format(testPrijs,".2f"),(testPrijs == float(27.44))))

    elif (ritprijs(11, 'ja', -1) and (testPrijs == float(0.00))):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
             format(testPrijs,".2f"),format(testPrijs,".2f"),(testPrijs == float(0.00))))

    elif (ritprijs(11, 'ja', 49)) and (testPrijs == float(25.48)):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
             testPrijs,format(testPrijs,".2f"),(testPrijs == float(25.48))))

    elif (ritprijs(12, 'nee', 51)) and (testPrijs == float(15.60)):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
             format(testPrijs,".2f"),format(testPrijs,".2f"),(testPrijs == float(15.60))))

    elif (ritprijs(12, 'ja', 49)) and (testPrijs) == float(23.52):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
             format(testPrijs, ".2f"), format(testPrijs, ".2f"), (testPrijs == float(23.52))))

    elif (ritprijs(12, 'nee', 1)) and (testPrijs == float(0.80)):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
             format(testPrijs, ".2f"), format(testPrijs, ".2f"), (testPrijs == float(0.80))))

    elif (ritprijs(12, 'ja', -1)) and (testPrijs == float(0.00)):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
             format(testPrijs, ".2f"), format(testPrijs, ".2f"), (testPrijs == float(0.00))))

    elif (ritprijs(12, 'ja', 51)) and (testPrijs == float(9.36)):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
             format(testPrijs, ".2f"), format(testPrijs, ".2f"), (testPrijs == float(9.36))))

    elif ritprijs(64, 'ja', 49) and (testPrijs == float(23.52)):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
             format(testPrijs, ".2f"), format(testPrijs, ".2f"), (testPrijs == float(23.52))))

    elif ritprijs(64, 'nee', 49) and (testPrijs == float(39.20)):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
             format(testPrijs, ".2f"), format(testPrijs, ".2f"), (testPrijs == float(39.20))))

    elif ritprijs(64, 'ja', 51) and (testPrijs == float(9.36)):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
             format(testPrijs, ".2f"), format(testPrijs, ".2f"), (testPrijs == float(9.36))))

    elif ritprijs(64, 'nee', 51) and (testPrijs == float(15.60)):
         print("De verwachte prijs is €{}  en de berekende prijs is €{}. De prijsberekening is dus {}".format(
             format(testPrijs, ".2f"), format(testPrijs, ".2f"), (testPrijs == float(15.60))))




#HIERONDER WORDT DE INFORMATIE VERGAARD OM VERVOLGENS DE BEREKENINGEN EROP LOS TE LATEN

leeftijd = int(input("Wat is uw leeftijd?: "))
weekendrit = (input("Gaat u in het weekend reizen?: "))
afstandKM = int(input("Voer aantal kilometers in tot uw bestemming: "))
print("Uw reis met eventuele korting bedraagt:", ritprijs(leeftijd, weekendrit, afstandKM), '\n')
testPrijs = float(ritprijs(leeftijd,weekendrit,afstandKM))
testing(testPrijs)
