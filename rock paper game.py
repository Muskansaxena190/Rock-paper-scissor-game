'''
WORKFLOW OF PROJECTS:
1- Input from user(Rock,Paper,Scissor)
2-Computer choice(computer choose randomely)
3-Result

Cases:
A-Rock
Rock - Rock = Tie
Rock - Paper = papaer win
Rock - scissor = Rock win

B-Paper
Paper - Rock = Paper win
Paper - Paper = Tie
paper - scissor = scissor win

C-Scisoor
Scissor - scissor = Tie
Scissor - Paper = Scissor win
Scissor - Rock = Rock win
'''

#define function
import random
item_List = ["Rock","Paper","Scissor"]

#input from user and computer
print("[WELCOME TO ROCK,PAPER AND SCISSOR GAME:]")

user_choice = input("Enter your move = Rock,Paper,Scissor:")
com_choice = random.choice(item_List)
print(f"user_choice = {user_choice}, com_choice = {com_choice} ")

#both choice
if user_choice == com_choice:
    print("Both choice are same: = Game Tie")

elif user_choice == "Rock":
    if com_choice == "Paper":
        print("Paper covers Rock: = Computer Win")
    else:
        print("Rock break Scissor: = You Win")

elif user_choice == "Paper":
    if com_choice == "Scissor":
        print("Scissor cuts paper: = Computer Win")
    else:
        print("paper covers Rock: = You Win")

elif user_choice == "Scissor":
    if com_choice == "Rock":
        print("Scissor smahes by Rock: = Computer Win")
    else:
        print("Paper cuts by Scissor= You win") 
        


