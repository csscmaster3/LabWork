#####################################################################################
# Guess My Number
#
# mpk 
# mpk 
# mpk 
# mpk

import os
import random


def guessMyNumber():
    
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #KV score variable
    guessMyNumberTotal = 0

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    os.system('cls')
    print()

    print("\t\tWelcome to 'Guess My Number'!")
    print()
    print(' '*10,"I'm thinking of a number between 1 and 100.")
    print(' '*10, "Try to guess it in as few attempts as possible.\n")

#mpk
    the_number = random.randint(1, 100)
#mpk 
    guess = int(input(" "*11+"Take a guess: "))
    tries = 1

#mpk guessing loop
    while guess != the_number:
        if guess > the_number:
            print(' '*11+'Lower...')
        else:
            print(' '*11+'Higher...')

        guess=int(input(' '*11+'Take a guess: '))
        tries += 1

    if tries <= 5:
        guessMyNumberTotal += 1
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#mpk
    print()
    print(' '*12+"You guessed it!  The number was", the_number)
    print(' '*12+"And it only took you", tries, "tries!")
#mpk
    if tries <=5:
        print(" "*12+"Congratulations!  You earned a point.")
    else:
        print(" "*12+"Unfortunately, you didn't earn a point this time.")
        
  
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#mpk
    return guessMyNumberTotal

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


