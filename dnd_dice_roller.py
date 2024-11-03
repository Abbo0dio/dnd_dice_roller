import random
while True:
    
    rng = 0
    diceAmount = int(input("Dice amount: "))
    diceSides = int(input("Dice sides: "))
    modifier = int(input("Modifier: "))


    for i in range(0,diceAmount):
        
        rng += random.randint(1,diceSides)
        
    
    totalRoll = rng + modifier

    print("Total = {0}" .format(totalRoll))
    redo = input(("Again? (Y/n): "))

    if (redo == "n" or redo == "N"):
        break