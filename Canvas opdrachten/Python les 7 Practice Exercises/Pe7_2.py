nummersWrite = open('kaartnummers.txt', 'w')
nummersWrite.write('325255, Jan Jansen\n')
nummersWrite.write('334343, Erik Materus\n')
nummersWrite.write('235434, Ali Ahson\n')
nummersWrite.write('645345, Eva Versteeg\n')
nummersWrite.write('534545, Jan de Wilde\n')
nummersWrite.write('345355, Henk de Vries\n')
nummersWrite.close()

nummersRead = open('kaartnummers.txt', 'r')
text = nummersRead.read()
i = text.replace(",", " ").split()



print("{} {} heeft kaartnummer: {}".format(i[1],i[2], i[0]))
print("{} {} heeft kaartnummer: {}".format(i[4],i[5], i[3]))
print("{} {} heeft kaartnummer: {}".format(i[7],i[8], i[6]))
print("{} {} heeft kaartnummer: {}".format(i[10],i[11], i[9]))
print("{} {} {} heeft kaartnummer: {}".format(i[13],i[14], i[15], i[12]))
print("{} {} {} heeft kaartnummer: {}".format(i[17],i[18], i[19], i[16]))

nummersRead.close()

