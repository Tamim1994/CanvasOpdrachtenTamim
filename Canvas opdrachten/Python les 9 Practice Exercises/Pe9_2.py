while True:
    invoer = input("Geef een string van vier letters: ")
    if len(invoer) == 4:
        break
    print("{} heeft {} letters".format(invoer, len(invoer)))
print("Inlezen van correcte string: {} is geslaagd".format(invoer))

