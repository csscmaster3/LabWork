#Horse Betting
#March 14, 2013
#Kevin Varcasio & Deng Zhu
#Game in which the user bets on a horse, the horses race, and then the game will return the total score when the user quits


import random
import datetime
import os

#KV - Initialization of the horse names and variables
horses=['Seabiscuit','Poe',"Santa's Little Helper",'Mickey','Above and Beyond',\
        'Ace of Spades','Big League','Captain Canada','Dareto Dream']

times=[0,1,2]
bet=0

#DZ - Generate random times for the first race, sort these times
def initTimes():
    for x in times:
        times[x]=random.randrange(120,160)
    times.sort()

#DZ - Displays the race results and convert int to time format       
def listResults():
    y=0
    for x in racers:
        print(str(y+1)+') ',x,' '*10, end='')
        print(datetime.timedelta(seconds=times[y]))
        y=y+1


#KV - Asks the user for a bet and checks to see if it is valid or if they want to quit
def gamble():
    global bet
    global racers
    global horseBetScore

    
    bet=int(input('Which horse do you place your bet on? (0 to Exit) :'))    
    if bet==0:
        score()
        exit()
    if bet<4 and bet>=1:
        
        race()   
    else:
        print('Invalid horse')
        gamble()

#KV - Generate random times based on the place of the horse in the previous race
# If they finished in a higher spot previously there is a higher chance of a better time
def race():
    global times

    if random.randrange(0,100) < 50:
        times[0]=random.randrange(110,130)
    else:
        times[0]=random.randrange(120,165)

    if random.randrange(0,100) < 35:
        times[1]=random.randrange(110,130)
    else:
        times[1]=random.randrange(120,165)

    if random.randrange(0,100) < 20:
        times[2]=random.randrange(110,130)
    else:
        times[2]=random.randrange(120,165)

    os.system('cls')
    print('You have bet on',racers[bet-1])
    print('The race has concluded and the results are:')
    listResults()
    winner()

#DZ - Checks to see if the horse the user bet on had the fastest time.  Compare
# times within the list to see if it is the highest
def winner():
    global horseBetScore
    

    if bet==1:
        if times[0] < times[1] and times[0] < times[2]:
            print ('Your horse has won!')
            horseBetScore+=1
        else:
            print ('Your horse has lost.')

    if bet==2:
        if times[1] < times[0] and times[1] < times[2]:
            print ('Your horse has won!')
            horseBetScore+=1
        else:
            print ('Your horse has lost.')

    if bet==3:
        if times[2] < times[0] and times[2] < times[1]:
            print ('Your horse has won!')
            horseBetScore+=1
        else:
            print ('Your horse has lost.')

    print('Your score is:',horseBetScore)
    gamble()


def intro():
    welcome='Welcome'
    print(welcome.center(60,'*'))
    print('|Horse Betting Version 1.0|'.center(60,'_'))
    print('|Kevin Varcasio & Deng Zhu|'.center(60, ' '))
    print()

def score():
    print('Your score is: ',horseBetScore,'. Thanks for playing!')
    os.system('pause')
    
def horseBet():
    global racers
    global horseBetScore

    os.system('cls')
    horseBetScore=0
    intro()
    initTimes()
    racers=random.sample(horses, 3)
    print('The horses for the previous race and their times are: ')
    listResults()
    gamble()

horseBet()









