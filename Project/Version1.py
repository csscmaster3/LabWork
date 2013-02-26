import random
import datetime

## Need to create a dictionary joining horses and times
horses=['Seabiscuit','Poe',"Santa's Little Helper",'Mickey','Above and Beyond',\
        'Ace of Spades','Big League','Captain Canada','Dareto Dream']

times=[0,1,2]

bet=0

def randTimes():
    for x in times:
        times[x]=random.randrange(120,220)
    times.sort()
    times.reverse()
        
def listResults():
    y=0
    for x in racers:
        print(str(y+1)+') ',x,' '*10, end='')
        print(datetime.timedelta(seconds=times[y]))
        y=y+1

def gamble():
    global bet
    bet=int(input('Which horse do you place your bet on? :'))
    if bet<4 and bet>0:
        results()
    else:
        print('Invalid horse')
        gamble()

def results():
    print('You have bet on',racers[bet-1])


def main():
    global racers
    randTimes()
    racers=random.sample(horses, 3)
    print('The horses for this race and their previous lap times are: ')
    listResults()
    gamble()

main()








