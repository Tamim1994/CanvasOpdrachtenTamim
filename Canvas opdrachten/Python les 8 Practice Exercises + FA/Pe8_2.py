inputString = eval(input(("Geef lijst met minimaal 10 strings: ")))
newList = []
for x in inputString:
    if len(x) == 4:
        newList.append((x))

print()
print("De nieuw-gemaakte lijst met alle vier-letter strings is: \n", newList)