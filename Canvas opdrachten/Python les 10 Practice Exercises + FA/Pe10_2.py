import random
def monopolyworp():
    steen1 = random.randint(1,7)
    steen2 = random.randint(1,7)
    steen3 = random.randint(1,7)
    steen4 = random.randint(1,7)
    steen5 = random.randint(1,7)
    steen6 = random.randint(1,7)

    print(steen1, '+', steen2, '=', (steen1+steen2),end = '')

    if steen1 == steen2:
        print("(dubbel)")
        print(steen3, '+', steen4, '=', (steen3 + steen4), end='')
        if steen3 == steen4:
            print("(dubbel)")
            if steen5 == steen6:
                print(steen5, '+', steen6, '=', "(direct naar gevangenis)")
            else:
                print(steen5, '+', steen6, '=', (steen5 + steen6))


monopolyworp()