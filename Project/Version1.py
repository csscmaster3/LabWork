import random
import datetime

## Need to create a dictionary joining horses and times
horses=['Seabiscuit','Poe',"Santa's Little Helper",'Mickey','Above and Beyond',\
        'Ace of Spades','Big League','Captain Canada','Dareto Dream']

times=[0,1,2]

bet=0

horseRaceScore=0

def initTimes():
    for x in times:
        times[x]=random.randrange(120,160)
    times.sort()
        
def listResults():
    y=0
    for x in racers:
        print(str(y+1)+') ',x,' '*10, end='')
        print(datetime.timedelta(seconds=times[y]))
        y=y+1

def gamble():
    global bet
    global racers 
    bet=int(input('Which horse do you place your bet on? :'))
    print()
    if bet<4 and bet>0:
        print('You have bet on',racers[bet-1])
        race()   
    else:
        print('Invalid horse')
        gamble()
    
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

    print()
    print('The race has concluded and the results are:')
    listResults()
    winner()

def winner():
    global horseRaceScore

    if bet==1:
        if times[0] < times[1] and times[0] < times[2]:
            print ('win')
            horseRaceScore+=1
        else:
            print ('loss')

    if bet==2:
        if times[1] < times[0] and times[1] < times[2]:
            print ('win')
            horseRaceScore+=1
        else:
            print ('loss')

    if bet==3:
        if times[2] < times[0] and times[2] < times[3]:
            print ('win')
            horseRaceScore+=1
        else:
            print ('loss')

    print('Your score is:',horseRaceScore)

    gamble()
    
    
def main():
    
    global racers
    initTimes()
    racers=random.sample(horses, 3)
    print('The horses for this race and their previous lap times are: ')
    listResults()
    gamble()

main()








