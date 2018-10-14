def ticker(filename):
    'Stop alle lines van het bestand in readTicker en splits vervolgens alle indexes'
    filename = open("ticker symbol.txt")
    readTicker = filename.readlines()
    tickerNameSymbol = {}

    for x in readTicker:
        key, value = x.strip().split(':')
        tickerNameSymbol[key] = str(value)

    filename.close()
    return tickerNameSymbol



tickerFO = open("ticker symbol.txt", "r+")
tickerFO.write("YAHOO:YHOO\n")
tickerFO.write("GOOGLE INC:GOOG\n")
tickerFO.write("Harley-Davidson:HOG\n")
tickerFO.write("Yamana Gold:AUY\n")
tickerFO.write("Sotheby's:BID\n")
tickerFO.write("inBev:BUD\n")
tickerFO.close()



filename = tickerFO
functionCall = ticker(filename)

companyName = input("Enter company name: ")

for key,value in functionCall.items():      #controleer voor elke key of input overeenkomt met key
    if companyName == key:
        print("Ticker symbol: ", value)

keyValue = input("Enter Ticker symbol: ")

for key,value in functionCall.items():      #controleer of value overeenkomt met input, print dan key
    if keyValue == value:
        print("Company name: ", key)

