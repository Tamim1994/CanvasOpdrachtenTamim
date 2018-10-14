def seizoen(maand):

    #berekenen in welke seizoen de maanden vallen

    if (maand >= 3) and (maand <= 5):
        print("Het seizoen in deze maand is: Lente")
    elif (maand >= 6) and (maand <= 8):
        print("Het seizoen in deze maand is: Zomer")
    elif (maand >= 9) and (maand <= 11):
        print("Het seizoen in deze maand is: Herfst")
    elif (maand > 11 and maand < 13) or (maand >=1 and maand < 3):
        print("Het seizoen in deze maand is: Winter")

    return maand

seizoen(2)
