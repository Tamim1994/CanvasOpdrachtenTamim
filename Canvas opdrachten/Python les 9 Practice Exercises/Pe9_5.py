def namen():
    dictNamen = {}
    telNamen = []       #lege lijst voor het tellen van het aantal voorkomende namen

    while True:
        vraagNamen = input("Volgende naam: ")
        telNamen.append(vraagNamen)             #stop naam in lijst telNamen
        dictNamen.update({vraagNamen:telNamen.count(vraagNamen)})   #update dictionary met key en value

        if vraagNamen == "":        #als er een lege string wordt gelezen, verwijder dat uit dict
            dictNamen.pop("")
            break
    for key,value in dictNamen.items():         #controleer de frequentie van namen en print het
        if (value > 0) and (value < 2):
            print("Er is {} student met de naam: {}".format(value,key))
        elif (value == 0) or (value >= 2):
            print("Er zijn {} studenten met de naam: {}".format(value,key))

namen()
