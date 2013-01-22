# Project Name: Game World
# 15/01/2013
# Kevin Varcasio
# Training project to demonstrate concepts from the lectures.
# Presentes a menu of games to the user and plays the game the user chooses.


import os
import random
import math

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
    if userName=='' or passWord=='':
        print(' '*10+'Please enter a valid Username and Password.')
        userName=input(' '*10+'Please enter user ID:')
        passWord=input(' '*10+'Please enter password: ')

    if passWord!="happy":
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
    if gameChoice=="1":
        Craps()
    elif gameChoice=="2":
        print()
        print(" "*9,"Game under construction.  Please try again later.")
        input(screenPause)
    elif gameChoice=="3":
        print()
        print(" "*9,"Game under construction.  Please try again later.")
        input(screenPause)
    elif gameChoice=="4":
        print()
        print(" "*9,"Game under construction.  Please try again later.")
        input(screenPause)
    else:
        print()
        print(' '*9,'You have entered an invalid menu choice.')
        gameChoice=input(' '*10+'Please choose a game between 1 and 4: ')
        getGame(gameChoice)
    


####################################################################################
####################################################################################


def Craps():
# mpk Demonstrates random number generation

# mpk Set up the screen
    

# KV generate random numbers 1 - 6
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    total=die1+die2
    
# mpk Output Results
    print()
    print()
    print()
    print(' '*7+'='*56+'=')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    
    #KV Fix margins for 2 digit numbers
    if total > 9:
        print(' '*7 + '|  *  | You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!' +' |  *  |')
    else:
        print(' '*7 + '|  *  | You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!' +'  |  *  |')



        
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')      
    #print(' '*7+' -----  You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!'+' -----')
    #print()
    print(' '*7+'='*56+'=')


# mpk Pause the screen
    input(' '*10+'Press any key to continue...')


# mpk Set up the screen Toss #2
    

# mpk generate random numbers 1 - 6
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    total=die1+die2

# mpk Output Results
    print()
    print()
    print()
    print(' '*7+'='*56+'=')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
   #KV Fix margins for 2 digit numbers
    if total > 9:
        print(' '*7 + '|  *  | You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!' +' |  *  |')
    else:
        print(' '*7 + '|  *  | You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!' +'  |  *  |')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')      
    #print(' '*7+' -----  You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!'+' -----')
    #print()
    print(' '*7+'='*56+'=')

# mpk Pause the screen
    input(' '*10+'Press any key to continue...')


# mpk Set up the screen Toss #3
    

# KV generate random numbers 1 - 6
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    total=die1+die2

# mpk Output Results
    print()
    print()
    print()
    print(' '*7+'='*56+'=')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    #KV Fix margins for 2 digit numbers
    if total > 9:
        print(' '*7 + '|  *  | You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!' +' |  *  |')
    else:
        print(' '*7 + '|  *  | You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!' +'  |  *  |')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')      
    #print(' '*7+' -----  You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!'+' -----')
    #print()
    print(' '*7+'='*56+'=')

# mpk Pause the screen
    input(' '*10+'Press any key to continue...')

####################################################################################
####################################################################################

# KV Declare the Main() function
def Main():
    getPassword()
    print()

# mpk Call the Main() function
Main()
