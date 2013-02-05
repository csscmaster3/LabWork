# Project Name: Game World
# 15/01/2013
# Kevin Varcasio
# Training project to demonstrate concepts from the lectures.
# Presentes a menu of games to the user and plays the game the user chooses.


import os
import random
import math
import GameWorldCraps
import GameWorldGuessMyNumber


#KV define the Score variable
totalScore = 0

def getPassword():
    
# mpk Print password screen 
    os.system('cls')
    print()
    print()
    print(' '*10+'='*50+'=')
    print(' '*10+'='*50+'=')
    print(' '*10+'*'+' '*49+'*')
    print(' '*10 + '*' +' '*16+'Enter Game World'+' '*17+'*')
    print(' '*10+'*'+' '*49+'*')
    print(' '*10+'='*50+'=')
    print(' '*10+'='*50+'=')
    print()
    print(' '*10+'*'+' '*49 +'*')

# KV Read in User ID and Password
    userName=input(' '*10+'Please enter user ID:')
    passWord=input(' '*10+'Please enter password: ')
    print(' '*10+'*'+' '*49+'*')
    
# KV Validate the username and password
    while userName=='' or passWord=='':
        print(' '*10+'*'+' '*49+'*')
        print(' '*10+'Please enter a valid Username and Password.')
        userName=input(' '*10+'Please enter user ID:')
        passWord=input(' '*10+'Please enter password:')
        
                
    while passWord!="happy":
        print(' '*10+'*'+' '*49+'*')
        print(' '*10+'Please enter a valid password')
        passWord=input(' '*10+'Please enter password: ')

     
# KV Clear the Screen and Call the Game Menu function
    os.system('cls')
    GameMenu(userName)
   


####################################################################################
####################################################################################

def GameMenu(UserID):
    
#mpk Print the Game Menu Screen
    os.system('cls')
    print()
    print()
    print()
    print(' '*10+'='*50+'=')
    print(' '*10+'='*50+'=')
    print(' '*10+'*'+' '*49 +'*')

# mpk Calculate the margins for a message that changes
    greeting='Welcome to Game World, '+UserID+'!'
    greetingLength=(len(greeting))
    margins=((46-greetingLength)/2)
    if len(UserID) % 2==0:
        #KV Even Number
        margins=((46-greetingLength)/2)
        print(' '*9,'*'+' '*int(margins),greeting,' '*int(margins),'*')
    else:
        #KV Odd Number
        margins=((46-greetingLength)/2)
        print(' '*9,'*'+' '*int(margins),greeting,' '*int(margins+1),'*')



    
    print(' '*10+'*'+' '*49 +'*')
    print(' '*10+'*'+'   1. Craps'+' '*38 +'*')
    print(' '*10+'*'+'   2. Guess The Number'+' '*27 +'*')
    print(' '*10+'*'+'   3. Word Jumble'+' '*32 +'*')
    print(' '*10+'*'+'   4. Hangman'+' '*36 +'*')
    print(' '*10+'*'+' '*49 +'*')
    print(' '*10+'*'+' '*49 +'*')
    
    print(' '*10+'='*50+'=')
    print(' '*10+'='*50+'=')
    print()


# KV Read in the user's choice of game and call the correct game
    gameChoice=input(' '*10+'Please choose a game:')
    getGame(gameChoice)


# KV Call the correct game based on the user's choice
def getGame(gameChoice):

    screenPause=" "*10+"Press any key to continue..."
    
    while gameChoice != "1" and gameChoice != "2":
        if gameChoice=="3":
            print()
            print(" "*9,"Game under construction.  Please try again later.")
            gameChoice=input(' '*10+'Please choose a game between 1 and 4: ')      
        elif gameChoice=="4":
            print()
            print(" "*9,"Game under construction.  Please try again later.")
            gameChoice=input(' '*10+'Please choose a game between 1 and 4: ')
        else:
            print()
            print(' '*9,'You have entered an invalid menu choice.')
            gameChoice=input(' '*10+'Please choose a game between 1 and 4: ')


    if gameChoice=="1":
        crapsScore= GameWorldCraps.Craps()
        #KV Displays the craps score to the user
        os.system('cls')
        print()
        if crapsScore > 0:
            print(" "*14, "Congratulations! Your Craps score is",str(crapsScore)+".")
        else:
            print(" "*20, "Your Craps score is",str(crapsScore)+".")
        #KV Shows the total score to the user
        global totalScore
        totalScore = totalScore + crapsScore
        print(" "*12, "Your total score for this game session is",str(crapsScore)+".")
    elif gameChoice=="2":
        print()
        print(" "*9,"Game under construction.  Please try again later.")
        input(screenPause)
    

####################################################################################
####################################################################################

# KV Declare the Main() function
def Main():
    getPassword()
    print()

# mpk Call the Main() function
Main()
