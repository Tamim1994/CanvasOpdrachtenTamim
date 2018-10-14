dictCijfers = {'Alice':8.5, 'Bob':7.3, 'John':9.5, 'Richard':4.0, 'Martijn':5.5, 'Bart':10, 'Tony':9.2, 'Natasha': 6.5}

for key,value in dictCijfers.items():
    if value > 9:
        print(key,value)
