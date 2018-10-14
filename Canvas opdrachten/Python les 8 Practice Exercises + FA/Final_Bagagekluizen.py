def toon_aantal_kluizen_vrij():
    'Functie voor het berekenen van het aantal vrije kluizen '

    leesKluizen = open("kluizen.txt", "r")
    aantalRegels = leesKluizen.readlines()
    print("Er is/zijn {} kluis/kluizen vrij ".format(12 - len(aantalRegels)))
    leesKluizen.close()


def nieuwe_kluis():
    'Functie voor het aanmaken van een nieuwe kluis'

    kluizenFile = open("kluizen.txt", "r+")
    kluizenCheck = kluizenFile.readlines()
    kluisNummers = ['1','2','3','4','5','6','7','8','9','10','11','12']
    mijnLijst = [i.split(";")[0:] for i in kluizenCheck]

    for x in mijnLijst: #read elke index in de lines van file kluizen
        for y in x:
            if y in kluisNummers:   #komt index overeen met een kluisnummer
                kluisNummers.remove(y)
            elif kluisNummers == []:
                print("Er zijn geen kluizen meer beschikbaar!")
                return True


    # print(myList)
    print(mijnLijst)
    print(kluisNummers)

    if kluisNummers not in mijnLijst: #als kluisnummer niet in kluizencheck

        kluisCode = input("Voer een code voor uw kluis in: ")#voer kluiscode in
        print("U krijgt kluisnummer: ", kluisNummers[0])    #geef nieuwe kluisnummer
        kluizenFileAppend = open("kluizen.txt", "a")    #open kluizen.txt in append
        kluizenFileAppend.write("{}".format(kluisNummers[0])) #write nieuwe kluisnr,kluiscode
        kluizenFileAppend.write(";{}".format(kluisCode))
        kluizenFileAppend.write("\n")

    kluizenFile.close()


def kluis_openen():
    kluizenFile = open("kluizen.txt", "r+")
    kluizenCheck = kluizenFile.readlines()
    wachtwoordCheck = input("Voer uw kluisnummer in gevolgd door ; en dan uw wachtwoord: ")
    mijnLijst2 = [i.replace("\n","").split()[0:] for i in kluizenCheck]


    for x in mijnLijst2:            #controleer elk sub-index van mijnlijst2
        for y in x:
            if y in wachtwoordCheck:    #controleer of wachtwoord hoort bij kluisnummer
                print("U heeft de juiste gegevens ingevoerd.")



    kluizenFile.close()







print("\n1: Ik wil weten hoeveel kluizen nog vrij zijn")
print("2: Ik wil een nieuwe kluis")
print("3: Ik wil even iets uit mijn kluis halen\n")

keuzeKluis = int(input("Voer het nummer van uw gekozen optie in: "))
if keuzeKluis > 3 or keuzeKluis < 1:
    print("U heeft een niet bestaande optie gekozen")
elif keuzeKluis == 1:
    toon_aantal_kluizen_vrij()

elif keuzeKluis == 2:
    nieuwe_kluis()

elif keuzeKluis == 3:
    kluis_openen()

