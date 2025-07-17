import random
choice = ["rock", "paper", "scissor"]
usercount = 0
computercount = 0

while True:
    print('''
Game Start...
          1.YES
          2.NO | EXIT
          ''')
    choiceinput = int(input("Enter your choice:-"))  
    if choiceinput == 1:
        for i in range(1,6):
            print('''
              1.rock
              2.paper
              3.scissor
              ''')
            userinput = int(input("enter your choice: "))

            if userinput == 1:
                userchoice = "rock"
            elif userinput == 2:
                userchoice = "paper"
            elif userinput == 3:
                userchoice = "scissor"
            else:
                print("invalid choice!.. Please try again!..")
                continue

            computerchoice = random.choice(choice)

            if userchoice == computerchoice:
                print("......Game Draw......")
                print("userchoice is :-", userchoice)
                print("computerchoice is :-", computerchoice)
                computercount += 1
                usercount = usercount + 1
            elif (userchoice == "rock" and computerchoice == "scissor") or \
                 (userchoice == "paper" and computerchoice == "rock") or \
                 (userchoice == "scissor" and computerchoice == "paper"):
                print(".....YOU WIN.....")
                print("userchoice is :-", userchoice)
                print("computerchoice is :-", computerchoice)
                usercount += 1
            else:
                print(".....COMPUTER WIN....")
                print("userchoice is :-", userchoice)
                print("computerchoice is :-", computerchoice)
                computercount += 1

            print("computer score is :", computercount)
            print("your score is :", usercount)

        if computercount == usercount:
            print(".......GAME DRAW ......!")
            print("computer score is :", computercount)
            print("your score is :", usercount)
        elif computercount > usercount:
            print("....COMPUTER WON THE GAME....!")
            print("computer score is :", computercount)
            print("your score is :", usercount)
        else:
            print("....YOU WON THE GAME....!")
            print("computer score is :", computercount)
            print("your score is :", usercount)
            if computercount>usercount :
                print(".........YOU LOSE !!! BETTER LUCK NEXT TIME!...")
            else:
                print("....YOU WIN... CONGRATULATIONS!!!!..")

    else:
        break
