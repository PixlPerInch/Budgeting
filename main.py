import banking as track

while True:
    print("options: Check or Add")
    userInput = input("What do you want to do? ")

    if userInput == "Check":
        userCheck = input("What do you want to check? Investments, Purchases or Gains? ")
        if userCheck == "Investments" or userCheck == "Purchases" or userCheck == "Gains":
            print(track.displayTotal(userCheck))
        else:
            print("What?")
            continue

    elif userInput == "Add":
        userAdd = input("What do you want to add? Investment, Purchase or Gain? ")

        if userAdd == "Investment":
            source = input("Where did you invest? ")
            amount = int(input("How much did you invest? "))
            track.invest(source, amount)
        elif userAdd == "Purchase":
            source = input("What did you purchase? ")
            amount = int(input("How much did it cost? "))
            track.spent(source, amount)
        elif userAdd == "Gain":
            source = input("How did you earn? ")
            amount = int(input("How much did you earn? "))
            track.earnt(source, amount)
        else:
            print("What?")
            continue

    elif userInput == "Stop":
        break

    else:
        print("What?")
        continue