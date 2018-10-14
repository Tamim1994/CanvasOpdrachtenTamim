def lang_genoeg(lengte):
    if int(lengte) >= int(120):
        return "Je bent lang genoeg voor de attractie!"
    else:
        return "Sorry, je bent te klein!"

gebruiker = input("Wat is je lengte in cm?: ")

print(lang_genoeg(gebruiker))
