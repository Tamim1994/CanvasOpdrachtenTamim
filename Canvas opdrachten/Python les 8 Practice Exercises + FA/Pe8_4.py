studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentcijfers):
    gemiddeldeStudent = []            #lege lijst die gevuld wordt met gemiddelden
    for x in studentcijfers:
        gemiddeldeStudent.append(sum(x)/(len(x)))   #berekent gemiddelde per index

    return gemiddeldeStudent

def gemiddelde_van_alle_studenten(studentencijfers):
    gemiddeldeAlles = gemiddelde_per_student(studentencijfers)  #Roep functie op
    gemiddeldeTotaal = []
    gemiddeldeTotaal.append(int((sum(gemiddeldeAlles)/len(gemiddeldeAlles))))   #cast het gemiddelde als int

    return gemiddeldeTotaal




print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))