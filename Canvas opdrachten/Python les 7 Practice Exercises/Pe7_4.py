import time
fileObject = open("hardlopers.txt", "a")
vandaag = time.localtime()           #localetijd wordt in variable vandaag gestopt

i = 0

while i < 5:
#while loop om van 5 gebruikers hun naam op te vragen en in een bestand te schrijven
    fileObject.write(time.strftime("%a %d %b %Y, %H:%M:%S, ",time.localtime()))
    fileObject.write(input("Voer uw naam in: "))
    fileObject.write('\n')
    i += 1


fileObject.close()