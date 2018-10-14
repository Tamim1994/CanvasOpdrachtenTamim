counter = 0                 #counter voor het tellen van het aantal getallen
getallenLijst = []          #lege lijst voor opslaan van alle ingevoerde getallen

while True:
    getal = float(input("Geef een getal: "))
    counter += 1
    if getal == 0:
        counter -= 1            #als getal == 0, counter -1
        break   #ga uit de loop en print het aantal getallen en de som
    getallenLijst.append(getal)

print("Er zijn {} getallen ingevoerd, de som is: {}".format(counter, format(sum(getallenLijst), ".2f")))

