def convert(i):
    fahrenheit = (i * 1.8) + 32
    return fahrenheit


def table():

    print("F        C")
    for i in range(-30,41,10):
        i = convert(i)
        print("{} {:7}".format(i,(i-32)/1.8))

table()
