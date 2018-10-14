def kwadraten_som(grondgetallen):
    getallen = []
    for i in grondgetallen:
        if i > 0:
            getallen.append(i ** 2)
    return sum(getallen)

grondgetallen = [4, 5, 3, -81]
print(kwadraten_som(grondgetallen))