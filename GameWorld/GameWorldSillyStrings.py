#####################################################################################
#  SillyStrings
# Purpose:  A training program to demonstrate string concepts from chapter 8 and list concepts from Chapter 9

import os

def sillyStrings():

#mpk
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    sillyStringScore=0 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    os.system('cls')

#mpk 
    print("\t\t              Welcome to 'SillyStrings'!")
    print()
    print()

# mpk 
    
    print(' '*10,"The point of this game is to build words within the strings.")
    print(' '*10," One point per letter for vertical and horizontal words.")
    print(' '*10,"    Three points per letter for diagonal words.")
    print(' '*10,"            Finish off a word with an 'X'")
    print(' '*10,"           Enter 'XXXXXXXXX' to Quit.\n")

#mpk 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    sillyStringScore=buildStrings()
    return sillyStringScore
    
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def buildStrings():


#mpk 
    charString = ""
    gameString = ""
    gameBoard = []

#mpk 
    while charString.upper() != "XXXXXXXXX":
        
        gameString = ("")
        print()
        prompt =  " "*10 + "Please enter 9 characters: "

#mpk 
        charString = input(prompt)

#mpk 
        while not(charString.isalpha()) or len(charString) !=9:
            print(" "*12+"Please enter 9 alphas, no numbers or symbols.")
            charString = input(prompt)

#mpk 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        for numbers in range(0,9):
            alpha=charString[numbers]
            gameString=gameString+" "+alpha.upper()
            
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#mpk 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        gameBoard.append(gameString)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#mpk 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        print(" "*10+"*"*49)
        os.system('cls')
        print(" "*10+"*"*49)
        for lines in range(len(gameBoard)):
            print(" "*10+"*"+" "*10+gameBoard[lines]+" "*10+"*")
            print(" "*10+"*"*49)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        print(" "*10+"*"*49)

#============================================================================
#mpk
    sillyStringScore=int(input(" "*10+"Enter your score for the game: "))
    return sillyStringScore

#============================================================================
