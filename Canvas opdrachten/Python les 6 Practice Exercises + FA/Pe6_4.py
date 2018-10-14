def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and str(len(str(newpassword))) >= str(6):
        return True
    else:
        return False

oldpassword = input("Voer uw oude wachtwoord in: ")
newpassword = input("Voer uw nieuwe wachtwoord in: ")
print(new_password(oldpassword, newpassword))