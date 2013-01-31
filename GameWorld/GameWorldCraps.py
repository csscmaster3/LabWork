##KV 

import os
import random


def Craps():
# mpk Demonstrates random number generation


#KV
    crapsTotal = 0

# mpk Set up the screen
    

# KV generate random numbers 1 - 6
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    total=die1+die2
#KV
    if total == 7 or total == 11:
        crapsTotal = crapsTotal + 1
    
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
    print(' '*7+'='*56+'=')


# mpk Pause the screen
    input(' '*10+'Press any key to continue...')


# mpk Set up the screen Toss #2
    

# mpk generate random numbers 1 - 6
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    total=die1+die2
    #KV
    if total == 7 or total == 11:
        crapsTotal = crapsTotal + 1

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
    print(' '*7+'='*56+'=')

# mpk Pause the screen
    input(' '*10+'Press any key to continue...')


# mpk Set up the screen Toss #3
    

# KV generate random numbers 1 - 6
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    total=die1+die2
    #KV
    if total == 7 or total == 11:
        crapsTotal = crapsTotal + 1

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
    print(' '*7+'='*56+'=')

#KV
    return crapsTotal
