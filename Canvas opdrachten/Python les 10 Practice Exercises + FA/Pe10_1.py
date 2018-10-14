bruin = set()

bruin.add('Deurne')
bruin.add('Helmond Brouwhuis')
bruin.add('Helmond')
bruin.add('Helmond \'t Hout')
bruin.add('Best')
bruin.add('Boxtel')
bruin.add('Eindhoven')
bruin.add('Beukenlaan')


groen = set()

groen.add('Weert')
groen.add('Heeze')
groen.add('Geldrop')
groen.add('Beukenlaan')
groen.add('Boxtel')
groen.add('Eindhoven')
groen.add('Best')

print(groen.intersection(bruin))        #welke elementen komen overeen tussen de twee sets
print(bruin.difference(groen))          #welke elementen van bruin zitten niet in groen
print(groen.union(bruin))               #nieuwe set met elementen uit broen en groen


