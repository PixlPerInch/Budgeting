Purchases = {}
Gains = {}
Investments = {}

def spent(purchase, cost):
    Purchases[purchase] = cost

def earnt(source, earning):
    Gains[source] = earning

def invest(type, invested):
    Investments[type] = invested

def displayTotal(userInput):
    total = 0
    if userInput == "Purchases":
        for i in Purchases.values():
            total += i
    elif userInput == "Gains":
        for i in Gains.values():
            total += i
    elif userInput == "Investments":
        for i in Investments.values():
            total += i
    else:
        print("Bad argument")
    return total

if __name__ == "__main__":
    spent("Food", 5000)
    spent("Commute", 1400)
    spent("Subsciptions", 980)

    earnt("Salary", 25000)
    earnt("Rent", 10000)
    earnt("Gifts", 2000)

    invest("Mutual Funds", 6000)
    invest("Stock", 500)
    invest("Gold", 400)

    print(displayTotal("Purchases"))
    print(displayTotal("Gains"))
    print(displayTotal("Investments"))

    #do main.py
    #create a module to calculate money in bank or bank details
    #feedback on the website