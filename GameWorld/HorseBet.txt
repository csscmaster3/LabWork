#Horse Betting
#March 14, 2013
#Kevin Varcasio & Deng Zhu
#Game in which the user bets on a horse, the horses race, and then the game will return the total score when the user quits

#KV Import statement.  Random to calculate random numers, datetime to display time, and os to run system commands.
import random
import datetime
import os

#KV - Initialization of the horse names and variable
horses=['Seabiscuit','Poe',"Santa's Little Helper",'Mickey','Above and Beyond',\
        'Ace of Spades','Big League','Captain Canada','Dareto Dream']

times=[0,1,2]

#DZ Game Header
def intro():
    print('|Horse Betting Version 1.0|'.center(60,'_'))
    print('|Kevin Varcasio & Deng Zhu|'.center(60, ' '))
    print()

#DZ - Generate random times for the first race, sort these times.  The for loop runs 3 times (times is defined to have 3 list locations) and will
# result in 3 different random numbers ranged 120 - 160.
def initTimes():
    for x in times:
        times[x]=random.randrange(120,160)
    times.sort()

#DZ - Displays the race results and convert int to time format.  The for loop displays both the horse's name and their times - this is why it is a for
# loop with a counter variable.  The time is created by converting an integer into datetime format (00:00:00).
def listResults():
    y=0
    for x in racers:
        print(str(y+1)+') ',x,' '*10, end='')
        print(datetime.timedelta(seconds=times[y]))
        y=y+1


#KV - Asks the user for a bet and checks to see if it is valid or if they want to quit.  To be valid the user input must be a digit between 1 and 3 inclusively.
# If the user types a zero the program begins its quit operation - going to score() then exiting.  If a user enters anything else they will be asked to try again.
def gamble():
    global racers
    global horseBetScore

    bet=input('Which horse do you place your bet on? (0 to Exit) :')

    while not bet.isdigit():
        print('Invalid Entry')
        bet=input('Which horse do you place your bet on? (0 to Exit) :')

    bet=int(bet)
    if bet==0:
        score()
    elif bet<4 and bet>=1:
        race(bet)   
    else:
        print('Invalid horse')
        gamble()

#KV - Generate random times based on the place of the horse in the previous race.  The random range has two possible ranges.  In order to
# use the first (lower valued) range, a percent chance operation takes placed.  The chances and places ratio is 1:50%, 2:35%, and 3:20%.
# Displays the user's bet for clarification and then proceeds to call listResults()
def race(betA):
    global times
    global horseBetScore

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
    intro()
    print('You have bet on',racers[betA-1])
    print('The race has concluded and the results are:')
    listResults()

    #DZ - Checks to see if the horse the user bet on had the fastest time.  This is calculated by comparing the user's bet
    # horse to the other horses in the list.  If the horse had the fastest time a win messaged is diplayed and the user's score
    # is increased by one.  If not, a loss message is displayed.  The program then calls gamble()
    if betA==1:
        if times[0] < times[1] and times[0] < times[2]:
            print('Congratulations'.center(50, ' '))
            print ('Your horse has won!'.center(50, ' '))
            horseBetScore+=1
        else:
            print ('Your horse did not win.'.center(50, ' '))

    if betA==2:
        if times[1] < times[0] and times[1] < times[2]:
            print('Congratulations'.center(50, ' '))
            print ('Your horse has won!'.center(50, ' '))
            horseBetScore+=1
        else:
            print ('Your horse did not win.'.center(50, ' '))

    if betA==3:
        if times[2] < times[0] and times[2] < times[1]:
            print('Congratulations'.center(50, ' '))
            print ('Your horse has won!'.center(50, ' '))
            horseBetScore+=1
        else:
            print ('Your horse did not win.'.center(50, ' '))

    print('Your score is:',horseBetScore)
    gamble()


#KV - Displays the final score.
def score():
    print('Your score is: ',horseBetScore,'. Thanks for playing!')

#DZ - Define main.  Starts program, welcome message, prepares variables and lists for game.  Starts gambling.
def horseBet():
    global racers
    global horseBetScore

    os.system('cls')
    print('Welcome'.center(60,'*'))
    horseBetScore=0
    intro()
    initTimes()
    #KV - Pick 3 random horses from the horse list
    racers=random.sample(horses, 3)
    print('The horses for the previous race and their times are: ')
    listResults()
    gamble()
    os.system('pause')
    return horseBetScore










