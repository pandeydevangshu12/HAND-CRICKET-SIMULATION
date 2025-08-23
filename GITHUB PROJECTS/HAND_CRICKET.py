import random

print("---------------------------------------------------------------------------ENJOY------------------------------------------------------------------------")
print()

india = {1: "V.kohli", 2: "R.Sharma", 3: "S.Gill", 4: "S.Iyer", 5: "R.Jadeja", 6: "H.Pandaya",
         7: "J.Bumrah", 8: "KL Rahul", 9: "K.Yadav", 10: "M.shami", 11: "M.Siraj"}
pakistan = {1: "B.Azam", 2: "F.Zaman", 3: "S.Afridi", 4: "M.Rizwan", 5: "A.Shafique", 6: "H.Rauf",
            7: "S.Khan", 8: "Imam-ul-Haq", 9: "I.Khan", 10: "H.Ali", 11: "Z.Khan"}
england = {1: "B.Duckett", 2: "J.Root", 3: "O.Pope", 4: 'Z.Crawley', 5: 'B.Stokes', 6: 'R.Ahmed',
           7: 'B.Foakes', 8: 'A.Rashid', 9: 'J.Anderson', 10: 'M.Wood', 11: 'A.Cook'}

while True:
    l1 = []
    overs = int(input("Enter the number of overs you want to play: "))
    print()
    wickets = int(input("Enter the number of wickets with which you want to play: "))
    print()
    print('Choose your team:')
    print("1.India")
    print("2.Pakistan")
    print("3.England")
    team = int(input("Enter your Choice(1/2/3): "))
    print()
    if 1<=team<=3: 
        oppo = [1, 2, 3]

        if team == 1:
            oppo.remove(1)
            print("Your Team is India And here are your players: ")
            print(india)
            print()
            opponent = random.choice(oppo)
            if opponent == 2:
                print("Your opponent is 'Pakistan': ")
                print(pakistan)
            else:
                print("Your opponent is 'England': ")
                print(england)
            print()
            print("Here You Make Your Team List: ")
            for i in range(wickets):
                player = int(input("Enter the respective player id provided in the team list: "))
                l1.append(india[player])
            print(l1)

        elif team == 2:
            oppo.remove(2)
            print("Your Team is Pakistan And here are your players: ")
            print(pakistan)
            opponent = random.choice(oppo)
            if opponent == 1:
                print("Your opponent is 'India': ")
                print(india)
            else:
                print("Your opponent is 'England': ")
                print(england)
            print()
            print("Here You Make Your Team List: ")
            for i in range(wickets):
                player = int(input("Enter the respective player id provided in the team list: "))
                l1.append(pakistan[player])
            print(l1)

        else:
            oppo.remove(3)
            print("Your Team is England And here are your players: ")
            print(england)
            opponent = random.choice(oppo)
            if opponent == 2:
                print("Your opponent is 'Pakistan': ")
                print(pakistan)
            else:
                print("Your opponent is 'India': ")
                print(india)
            print()
            print("Here You Make Your Team List: ")
            for i in range(wickets):
                player = int(input("Enter the respective player id provided in the team list: "))
                l1.append(england[player])
            print(l1)
    else:
        print("INVALID INPUT")
        break
    print()
    print("----------------------------------------------------TOSS------------------------------------------------------------")
    print()

    toss = input("Head Or Tail: ")
    print()
    f, g, d, e, h, i = 0, 0, 0, 0, 0, 0

    if toss == 'Head':
        print("YOU WON THE TOSS")
        print("\nEnter your choice: ")
        print("1. Batting")
        print("2. Bowling")
        a = input("Enter the choice(1/2): ")

        if a == "1":
            print("!!You Chose To Bat First!!")
            print()
            print("----------------------------------------FIRST INNINGS-----------------------------------------------------")
            print()

            while f <= overs * 6 - 1:
                f += 1
                c = random.randrange(1, 7)
                b = int(input("Enter your choice(between 1 to 6): "))
                if b < 7:
                    print("The computer bowls:", c)
                    if b == c:
                        print("\n!!OUT!!")
                        e += 1
                        if e < wickets:
                            print("\nYou're left with", wickets - e, "wickets!!")
                            print("\nYour score is: ", d, "at the loss of: ", e, "wickets\n")
                            continue
                        else:
                            print("\nYou are all out at the score: ", d, "\n")
                            break
                    else:
                        d += b
                else:
                    f -= 1
                    print("!!BE CAREFUL WHAT YOU TYPE!!")

            print("You're final score is:", d, "at the loss of", e, "wickets")
            print("\nThe target for the computer is:", d + 1, "in", overs, "overs and with", wickets, "wickets in hand\n")

            print("--------------------------------------------SECOND INNINGS-----------------------------------------------------\n")

            while g <= overs * 6 - 1:
                g += 1
                if i > d:
                    break
                b = int(input("Enter your choice(between 1 to 6): "))
                if b < 7:
                    c = random.randrange(1, 7)
                    print("The computer hits a:", c)
                    if b == c:
                        print("\n!!OUT!!")
                        h += 1
                        if h < wickets:
                            print("\nComputer left with", wickets - h, "wickets!!")
                            print("\nComputer's score is: ", i, "at the loss of: ", h, "wickets\n")
                            continue
                        else:
                            print("\nComputer is all out at the score: ", i, "\n")
                            break
                    else:
                        i += c
                else:
                    g -= 1
                    print("!!NO BALL!!..!!Be careful with what you type!!")
                    i += 1

            print("Computer's score is:", i, "at the loss of", h, "wickets")
            print()
            if d > i:
                print("You won by", d - i, "runs\n")
            elif d<i:
                print("Computer won by", wickets - h, "wickets\n")
            else:
                print("IT'S A DRAW")
                print("We will have a toss to decide who won the match")
                print()
                toss = input("Head Or Tail: ")
                if toss == 'Head':
                    print("YOU WON MATCH")
                elif toss == "Tail":
                    print("YOU LOST THE MATCH")
                else:
                    print("YOU LOST THE MATCH")


        elif a == "2":
            print("!!You Chose To Bowl First!!")
            print()
            print("----------------------------------------FIRST INNINGS---------------------------------------------")
            print()

            while g <= overs * 6 - 1:
                g += 1
                b = int(input("Enter your choice(between 1 to 6): "))
                if b < 7:
                    c = random.randrange(1, 7)
                    print("The computer hits:", c)
                    if b == c:
                        print("\n!!OUT!!")
                        h += 1
                        if h < wickets:
                            print("\nComputer left with", wickets - h, "wickets!!")
                            print("\nComputer's score is: ", i, "at the loss of: ", h, "wickets\n")
                            continue
                        else:
                            print("\nComputer is all out at the score: ", i, "\n")
                            break
                    else:
                        i += c
                else:
                    g -= 1
                    print("!!NO BALL!!")
                    i += 1

            print("Computer's score is:", i, "at the loss of", h, "wickets")
            print("\nThe target is:", i + 1, "in", overs, " overs and with", wickets, "wickets in hand\n")

            print("-----------------------------------------SECOND INNINGS--------------------------------------")
            while f <= overs * 6 - 1:
                f += 1
                if d > i:
                    break
                b = int(input("Enter your choice(between 1 to 6): "))
                if b < 7:
                    c = random.randrange(1, 7)
                    print("The computer bowls:", c)
                    if b == c:
                        print("\n!!OUT!!")
                        e += 1
                        if e < wickets:
                            print("\nYou're left with", wickets - e, " wicket!!")
                            print("\nYour score is: ", d, "at the loss of: ", e, "wickets\n")
                            continue
                        else:
                            print("\nYou are all out at the score: ", d, "\n")
                            break
                    else:
                        d += b
                else:
                    f -= 1
                    print("!!BE CAREFUL WHAT YOU TYPE!!")

            print("You're final score is:", d, "at the loss of", e, "wickets")
            if d > i:
                print("\nYou won by", wickets - e, "wickets\n")
            elif d<i:
                print("\nComputer won by", i - d, "runs\n")
            else:
                print("IT'S A DRAW")
                print("We will have a toss to decide who won the match")
                print()
                toss = input("Head Or Tail: ")
                if toss == 'Head':
                    print("YOU WON MATCH")
                elif toss == "Tail":
                    print("YOU LOST THE MATCH")
                else:
                    print("YOU LOST THE MATCH")

        else:
            print("Invalid Input")

    else:
        a = random.randrange(1, 2)
        print()
        f, g, d, e, h, i = 0, 0, 0, 0, 0, 0
        if a == 1:
            print("!!Computer Chose To Bowl First!!")
            print()
            print("-------------------------------------------FIRST INNINGS-------------------------------------------")
            while f <= overs*6-1:
                f += 1
                c = random.randrange(1, 7)
                b = int(input("Enter your choice(between 1 to 6): "))
                if b < 7:
                    print("The computer bowls:", c)
                    if b == c:
                        print("\n!!OUT!!")
                        e += 1
                        if e < wickets:
                            if f != overs:
                                print("You're left with", wickets - e, " wickets!!\n")
                                print("Your score is: ", d, "at the loss of: ", e, "wickets")
                                continue
                        else:
                            print("\nYou are all out at the score: ", d, "\n")
                            break
                    else:
                        d += b
                else:
                    f -= 1
                    print("!!BE CAREFUL WHAT YOU TYPE!!")

            print("You're final score is:", d, "at the loss of", e, "wickets")
            print("\nThe target for the computer is:", d + 1, "in", overs, "overs and with", wickets, "wickets in hand\n")

            print("----------------------------------------------SECOND INNINGS---------------------------------------------")
            print()
            while g <= 11:
                g += 1
                if i > d:
                    break
                b = int(input("Enter your choice(between 1 to 6): "))
                if b < 7:
                    c = random.randrange(1, 7)
                    print("The computer hits:", c)
                    if b == c:
                        print("\n!!OUT!!")
                        h += 1
                        if h < wickets:
                            print("\nComputer left with", wickets - h, "wickets!!")
                            print("\nYour score is: ", i, "at the loss of: ", h, "wickets\n")
                            continue
                        else:
                            print("\nComputer is all out at the score: ", i, "\n")
                            break
                    else:
                        i += c
                else:
                    g -= 1
                    print("!!NO BALL!!")
                    i += 1

            print("Computer's score is:", i, "at the loss of", h, "wickets")
            print()
            if d > i:
                print("You won by", d - i, "runs\n")
            elif d<i:
                print("Computer won by", wickets - h, "wickets\n")
            else:
                print("IT'S A DRAW")
                print("We will have a toss to decide who won the match")
                print()
                toss = input("Head Or Tail: ")
                if toss == 'Head':
                    print("YOU WON MATCH")
                elif toss == "Tail":
                    print("YOU LOST THE MATCH")
                else:
                    print("YOU LOST THE MATCH")


        elif a == 2:
            print("!!Computer Chose To Bat First!!")
            print()
            print("--------------------------------------------------------FIRST INNINGS----------------------------------------------")
            print()
            while g <= overs * 6 - 1:
                g += 1
                b = int(input("Enter your choice(between 1 to 6): "))
                if b < 7:
                    c = random.randrange(1, 7)
                    print("The computer hits:", c)
                    if b == c:
                        print("\n!!OUT!!")
                        h += 1
                        if h < wickets:
                            print("\nComputer left with", wickets - h, "wickets!!")
                            print("\nYour score is: ", i, "at the loss of: ", h, "wickets\n")
                            continue
                        else:
                            print("\nComputer is all out at the score: ", i, "\n")
                            break
                    else:
                        i += c
                else:
                    g -= 1
                    print("!!NO BALL!!")
                    i += 1

            print("Computer's score is:", i, "at the loss of", h, "wickets")
            print("\nThe target is:", i + 1, "in", overs, "overs and with", wickets, "wickets in hand\n")

            print("--------------------------------------------------SECOND INNINGS---------------------------------------------")
            print()
            while f <= overs * 6 - 1:
                f += 1
                if d > i:
                    break
                b = int(input("Enter your choice(between 1 to 6): "))
                if b < 7:
                    c = random.randrange(1, 7)
                    print("The computer bowls:", c)
                    if b == c:
                        print("\n!!OUT!!")
                        e += 1
                        if e < wickets:
                            print("\nYou're left with", wickets - e, "wickets!!")
                            print("\nYour score is: ", d, "at the loss of: ", e, "wickets\n")
                            continue
                        else:
                            print("\nYou are all out at the score: ", d, "\n")
                            break
                    else:
                        d += b
                else:
                    f -= 1
                    print("!!BE CAREFUL WHAT YOU TYPE!!")

            print("You're final score is:", d, "at the loss of", e, "wickets")
            if d > i:
                print("\nYou won by", wickets - e, "wickets\n")
            elif d<i:
                print("\nComputer won by", i - d, "runs\n")
            else:
                print("IT'S A DRAW")
                print("We will have a toss to decide who won the match")
                print()
                toss = input("Head Or Tail: ")
                if toss == 'Head':
                    print("YOU WON MATCH")
                elif toss == "Tail":
                    print("YOU LOST THE MATCH")
                else:
                    print("YOU LOST THE MATCH")


    b1 = input("Do you want to quit(Y/N): ")
    if b1 == "Y":
        break
    else:
        print()
