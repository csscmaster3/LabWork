# Lab 4
# 07/02/2013
# Kevin Varcasio
# Lab 4 Work

#KV Q1 - Write a while loop and check to see if when mulitplied by 2 it is
#less than 100
def questionOne():
    #KV initialize variables
    product=0

    print()
    #KV While statement to compare to 100
    while product<100:
        product=int(input('Please enter a number: '))
        product=product*2

    print(product/2,'times 2 is above or equal to 100!')
    main()

#KV Q2 - Sum two numbers and ask to repeat
def questionTwo():
    #KV initialize variables
    numA=0
    numB=0
    choice='y'

    print()
    #KV while statement to see if to repeat or not
    while choice != 'n':
        numA=int(input('Please enter the first number:'))
        numB=int(input('Pleas enter the second number:'))
        print('The sum of those two numbers is',numA+numB,'\n')
        choice=str(input('Would you like to repeat?(y or n)'))

    print('Program has ended')
    main()
    
#KV Q3 - input a number and continue until user inputs a positive number
def questionThree():
    #KV initialize variables
    nonzero=0

    print()
    #KV while statement to compare to 0
    while nonzero<=0:
        nonzero=int(input('Please enter a postive nonzero number:'))

    print('You have followed directions!')
    main()


#KV - Q4 - Displays 10 rows of # repeating 15 times
def questionFour():

    #KV initialize variables

    row=0
    column=0

    print()
    
    #KV For statement to print # 15 times and then 10 rows of that
    for row in range(1,11):
        print()
        for column in range (1,16):
            print('#', end="")
            
        
    print()
    print()
    print('Enjoy your 10x15 grid')
    main()


#KV Q5 - Count number of bugs collected with a for loop
def questionFive():
    #KV initialize variables
    bugs=0
    day=1

    print()
    #KV For loop to repeat for number of days
    for day in range(1,8):
        dayString='Please enter the number of bugs collected on day '+str(day)+':'
        bugs=bugs+int(input(dayString))
        

    print()
    print('The total bugs collected was',bugs)
    main()


#KV Q6 - Count number of bugs collected with a while loop
def questionSix():
    #KV initialize variables
    bugs=0
    day=1

    print()
    #KV While loop to repeat for number of days
    while day<8:
        dayString='Please enter the number of bugs collected on day '+str(day)+':'
        bugs=bugs+int(input(dayString))
        day=day+1

    print()
    print('The total bugs collected was',bugs)
    main()

#KV Q7- Display table with minutes and calories burned
def questionSeven():
    #KV initialize variables

    minutes=10
    print('Minutes          Calories Burned')
    print('-'*32)

    #KV while loop to count calories by 5 until 30
    while minutes<35:
        caloriesBurned=3.9*minutes
        print(minutes,' '*20,caloriesBurned)
        minutes=minutes+5

    main()

#KV Q8 - Same as Q5 and Q6, but with the ability to enter number of researchers
# and have it iterate that many times
def questionEight():
    runs=0
    bugs=0
    day=1
    research=int(input('Please enter the number of researchers:'))
    print()

    #KV Compares interations to number of researchers and repeats until more interations
    while runs<research:
        print('Researcher',runs+1)
        bugs = 0
        for day in range(1,8):
            dayString='Please enter the number of bugs collected on day '+str(day)+':'
            bugs=bugs+int(input(dayString))
        print('The total bugs collected for researcher', runs+1,'is',bugs)
        runs=runs+1
        

    print()
    main()
    
    
#KV - Allows user to pick question #
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
