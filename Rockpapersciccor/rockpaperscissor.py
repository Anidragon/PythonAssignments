'''
Created on Jan 31, 2021

@author: Balu
'''
import random

yes_no = input("would you like to play rock paper scissors? yes, or no")

    
played = 0
counter = 0
while yes_no == "yes":
    choice = input("write your choice, Rock,Paper,orScissors")
    while choice != "Rock" and choice != "Paper" and choice != "Scissors":
        choice = input("you did not write a valid response please remember to capitalize the first letter!, write your choice,Rock,Paper,orScissors")
    played = played + 1
    comp_choice = random.randint(1,4)
    if comp_choice == 1:
        comp_choice = "Rock"
    elif comp_choice == 2:
        comp_choice = "Paper"
    elif comp_choice == 3:
        comp_choice = "Scissors"
    else:
        print("Error")
    if choice == "Rock" and comp_choice == "Rock":
        result = "tie"
    elif choice == "Paper" and comp_choice == "Paper":
        result = "tie"
    elif choice == "Scissors" and comp_choice  == "Scissors":
        result = "tie"
    elif choice == "Rock" and comp_choice == "Scissors":
        result = "win"
    elif choice == "Paper" and comp_choice == "Rock":
        result = "win"
    elif choice == "Scissors" and comp_choice  == "Paper":
        result = "win"
    elif comp_choice == "Rock" and choice == "Scissors":
        result = "loss"
    elif  comp_choice == "Paper" and choice == "Rock":
        result = "loss"
    elif comp_choice == "Scissors" and choice == "Paper":
        result = "loss"            
    else: 
        print("error")
    print("the result is a", result,"the computer chose",comp_choice,)
    if result == "tie":
        counter = counter + 0 
    elif result == "win":
        counter = counter + 1
    if result == "loss":
        counter = counter + 0
               
    yes_no = input("play again? yes or no (say no to view your record)")

print("Your record is",counter,"of",played,"games won")
