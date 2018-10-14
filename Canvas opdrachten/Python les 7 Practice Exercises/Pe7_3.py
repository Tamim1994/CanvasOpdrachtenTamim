openFile = open('kaartnummers.txt', 'r')
fileRead = openFile.read()



print("Deze file telt {} regels ".format((len(fileRead.splitlines()))))
list = []
i = fileRead.replace(",", "").splitlines()

for x in i:
    list.append(x)


maxList = max(list)
lijnNummer = list.index(maxList)+1
print("Het grootste kaartnummer is: {}en dat staat op regel {}".format(maxList[0:7],lijnNummer))

openFile.close()