# Lab 4
# 07/02/2013
# Kevin Varcasio
#


def questionOne():
    product=0

    print()
    while product<100:
        product=int(input('Please enter a number: '))
        product=product*2

    print(product/2,'times 2 is above or equal to 100!')
    main()


def questionTwo():
    numA=0
    numB=0
    choice='y'

    print()
    while choice != 'n':
        numA=int(input('Please enter the first number:'))
        numB=int(input('Pleas enter the second number:'))
        print('The sum of those two numbers is',numA+numB,'\n')
        choice=str(input('Would you like to repeat?(y or n)'))

    print('Program has ended')
    main()

def questionThree():
    nonzero=0

    print()
    while nonzero<=0:
        nonzero=int(input('Please enter a postive nonzero number:'))

    print('You have followed directions!')
    main()

def questionFour():

    row=0
    column=0

    print()
    

    for row in range(1,11):
        print()
        for column in range (1,16):
            print('#', end="")
            
        
    print()
    print()
    print('Enjoy your 10x15 grid')
    main()


def questionFive():

    bugs=0
    day=1

    print()
    for day in range(1,8):
        dayString='Please enter the number of bugs collected on day '+str(day)+':'
        bugs=bugs+int(input(dayString))
        

    print()
    print('The total bugs collected was',bugs)
    main()

def questionSix():
    bugs=0
    day=1

    print()
    while day<8:
        dayString='Please enter the number of bugs collected on day '+str(day)+':'
        bugs=bugs+int(input(dayString))
        day=day+1

    print()
    print('The total bugs collected was',bugs)
    main()


def questionSeven():

    minutes=10
    print('Minutes          Calories Burned')
    print('-'*32)

    while minutes<35:
        caloriesBurned=3.9*minutes
        print(minutes,' '*20,caloriesBurned)
        minutes=minutes+5

    main()

def questionEight():
    runs=0
    bugs=0
    day=1
    research=int(input('Please enter the number of researchers:'))
    print()
    
    while runs<research:
        print('Researcher',runs+1)
        for day in range(1,8):
            dayString='Please enter the number of bugs collected on day '+str(day)+':'
            bugs=bugs+int(input(dayString))
        runs=runs+1
        

    print()
    print('The total bugs collected was',bugs)
    main()
    
    

def main():
    print()
    choice=int(input('Which question to run?:'))
    if choice==1:
        questionOne()
    if choice==2:
        questionTwo()
    if choice==3:
        questionThree()
    if choice==4:
        questionFour()
    if choice==5:
        questionFive()
    if choice==6:
        questionSix()
    if choice==7:
        questionSeven()
    if choice==8:
        questionEight()
    else:
        main()
main()
