import random

Choose_AI = ["Rock" , "Paper" , " Scissore"]

AI = Choose_AI[random.randint(0,2)]

tries = 5
score = 0

player =False
while player == False:
    player = input("Enter Any of Those Rock/r or Paper/p or Sissore/s")
    if player == AI:
        print("TIE!!!")

     
    elif player == "Paper" or player == "p":
        if AI == "Scissors":
            print("You lose!, Better luck next time as computer choose", AI)
        else:
            print("You win! as the computer choose ", AI)
            player = True
    elif player == "Rock" or player == "r":
        if AI == "Paper":
            print("You lose!, Better luck next time as computer choose", AI)
        else:
            print("You win! as the computer choose ", AI)
            player = True        
    elif player == "Scissors" or player == "s":
        if AI == "Rock":
            print("You lose!, Better luck next time as computer choose", AI)
        else:
            print("You win! as the computer choose ", AI)
            player = True
    else:
        print("That's not a valid Input. plz Check your spelling!")
     
    player = False
    AI = Choose_AI[random.randint(0,2)]
    tries -=1
    print(f"You have {tries} tires and your score is {score}")
    if tries == 0:
        break 
    if player == True:
        score +=1        
    else:
        score -=1        
