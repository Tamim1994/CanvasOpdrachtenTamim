invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst = []
newInvoer = invoer.replace("-", "")
for x in newInvoer:
    newInvoer.split()
    lijst.append(int(x))

print("Gesorteerde list van ints: ", sorted(lijst))
print("Grootste getal: {} en kleinste getal: {}".format(max(lijst),min(lijst)))
print("Aantal getallen: {} en som van de getallen: {}".format(len(lijst), sum(lijst)))
print("Gemiddelde: ", sum(lijst) / len(lijst))