def code(invoerstring):
    rangLijst = []          #lege lijst voor return waardes van ord()
    rangLijstChar = []      #lege lijst voor omzetten van ord + 3 naar char
    for teken in invoerstring:
        rangLijst.append(ord(teken))

    for x in rangLijst:
        b = x + 3
        rangLijstChar.append(chr(b))
    print(''.join(rangLijstChar))   #voeg alle elementen in de lijst samen

code("RutteAlkmaarDen Helder")
