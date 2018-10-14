def gemiddelde():
    randomString = input("Type een willekeurige zin: ")
    x = randomString.split()    #Split elk woord zodat we de lengte kunnen bepalen
    lengteGetal = []
    for i in x:                     #lege lijst wordt gemaakt en de lengte van elke index wordt bepaald
        lengteGetal.append(len(i))
    somLijst = sum(lengteGetal)
    print("De gemiddelde lengte van de woorden in de zin zijn: ",somLijst / len(lengteGetal))


gemiddelde()