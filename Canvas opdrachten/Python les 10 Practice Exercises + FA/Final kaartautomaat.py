def inlezen_beginstation(stations):
    global stationsNS       #Globale variabele stationsNS zodat ik hem in andere functies kan oproepen.
    stationsNS = ['Schagen','Heerhugowaard','Alkmaar','Castricum','Zaandam',
                'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel',
                'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven','Weert',
                'Roermond','Sittard','Maastricht']

    while(1):

        # Controleer of de juiste beginstation wordt ingevoerd, zoja return beginstation

        beginstation = input("Wat is uw beginstation?: ")
        if beginstation in stationsNS:
            return beginstation
        if beginstation not in stationsNS:
            continue
        break

def inlezen_eindstation(stations,beginstation):
    global stationsNS

    while(1):

        #Controleer of juiste eindstation wordt ingevoerd, zoja return eindstation, anders geef foutmelding en vraag opnieuw input

        eindstation = input("Wat is uw eindstation?: ")
        if eindstation in stationsNS:
            if stationsNS.index(eindstation) > stationsNS.index(beginstation):
                return eindstation
        else:
            print("U heeft het verkeerde eindstation ingevoerd! Probeer het opnieuw\n")
            continue


def omroepen_reis(stations, beginstation, eindstation):
    global stationsNS
    naamBeginStation = inlezen_beginstation(stations)
    naamEindStation = inlezen_eindstation(stations,beginstation)
    afstand = stationsNS.index(naamEindStation)+1 - (stationsNS.index(naamBeginStation)+1)
    tussenstops = []

    for x in range(stationsNS.index(naamBeginStation)+1,stationsNS.index(naamEindStation)): #Stop de tussenstations in een lijst
        tussenstops.append(stationsNS[x])


    print("\nHet beginstation {} is het {}e station in het traject.\n".format(naamBeginStation,stationsNS.index(naamBeginStation)+1))
    print("Het eindstation {} is het {}e station in het traject.\n".format(naamEindStation, stationsNS.index(naamEindStation)+1))
    print("De afstand bedraagt {} station(s)".format(afstand))
    print("De prijs van het kaartje is {} euro\n".format(afstand*5))
    print("Jij stapt in de trein in: {}".format(naamBeginStation))
    print('Tussenstop(s): ', end='')
    print(",".join(tussenstops))
    print("Jij stapt uit in: {}".format(naamEindStation))




stationsNS = []
beginstation = 'Heerhugowaard'
eindstation = 'Maastricht'
omroepen_reis(stationsNS,beginstation,eindstation)
