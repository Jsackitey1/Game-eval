"""
A program to allow the user to either play a simple game or evaluate the contents of a list
and determine if it's ordered from least to greatest.

@author: Sackitey Joseph
"""

import random

# Defining a function to play the game Bear Ninja cowboy
# This function takes two inputs, one from the user and one generated randomly by the computer
# It compares the index of the inputs with with the list conatining Bear Ninja Cowboy and determines the winner

def bear_game(player_character,computer_character):
    
    if player_character==computer_character:
       result=  print("There is a tie.")
    elif (player_character ==0 and computer_character== 1) or \
        (player_character==1 and computer_character== 2) or \
        (player_character==0 and computer_character== 2):
        result=print("You won")
    else:
        result= print("You lost")
    return result    



# A function to evaluate if a list of numbers entered by the user are arranged from the least to the greatest
def list_evaluation(my_list):
    # This prints out the users list entered
    print(f"The list you entered is {my_list}\n")

    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            result = "The list is not in order"
            break
        else:
            result = "The list is in order"
    
    print(result)


    
              
    
    
print("1.Bear, Ninja, Cowboy \n2.List Evalution \n")
# To take the game choice from the user
user_choice = int(input("Enter 1 or 2 to Choose the game you want to play: "))
print()


# For bear ninja cowboy
if user_choice==1:
    # list containing the characters
    item_list=["Bear","Ninja","Cowboy"]
    print("0.Bear\n1.Ninja\n2.Cowboy")
    print()
    player_character= int(input("Enter 0, 1, or 2 to choose a character: "))
    print()
    # computer generates a random number from 0 to 2
    computer_character= random.randint(0,2)
    print(f"You selected {item_list[player_character]}")
    print(f"The computer chose {item_list[computer_character]}")
    
    # Function call
    bear_game(player_character,computer_character)
    
    
    
elif user_choice==2:
    #new_list stores user input as int values 
    new_list=[]
    # User string input is stored in my_list
    my_list= input("Enter a list of numbers seperated by a space: \n")
    
    my_list= my_list.split()
    
    
    for number in my_list:
        new_number = int(number)
        new_list.append(new_number)

    # List evaluation function call    
    list_evaluation(new_list)
    
    
else:
    print("Ooops!!!\nYou didn't select any game.\nRESTART GAME")
    
        
    

