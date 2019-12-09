import random
print("Go Fish")
cpile = 60
suits = ["spades", "diamonds", "clubs", "hearts"]
faces = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
pcards = []
ccards = []
for x in range(8):
    pface = random.choice(faces)
    psuit = random.choice(suits)
    pcards.append(pface + " of " + psuit)
    cface = random.choice(faces)
    csuit = random.choice(suits)
    ccards.append(cface + " of " + csuit)
print("Your cards are", pcards)
pchoice = input("Choose a card, (like Two of Spades) or quit. ")
pchoice.lower()
while pchoice != "quit":
    print("You: Do you have", pchoice + "?")
    if pchoice in ccards:
        ccards.remove(pchoice)
        print("Computer: Yes...")
    else:
        print("Computer: Go fish!")
        pgofif = random.choice(faces)
        pgofis = random.choice(suits)
        pgofi = str(pgofif + " of " + pgofis)
        pcards.append(pgofi)
        cpile = cpile - 1

    cfacec = random.choice(faces)
    csuitc = random.choice(suits)
    cchoice = (cfacec + " of " + csuitc)
    print("Computer: Do you have...", cchoice + "?")
    if cchoice in pcards:
        pcards.remove(pchoice)
        print("You: Yes...")
    else:
        print("You: Go fish!")
        cgofif = random.choice(faces)
        cgofis = random.choice(suits)
        cgofi = str(cgofif + " of " + cgofis)
        ccards.append(cgofi)
        cpile = cpile - 1

    print("Your cards are", ccards)
    if pcards == []:
        print("You win!")
        break
    if ccards == []:
        print("Computer wins!")
        break
    if cpile == 0:
        print("No more cards!")
        break
    pchoice = input("Choose a card, (like Two of Spades) or quit. ")
