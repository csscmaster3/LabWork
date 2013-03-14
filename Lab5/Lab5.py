## Chapter 8 Lab
## 3/14/2013
## Kevin Varcasio
## Doing the chapter 8 lab

#KV force the input to be lower case so that both Y or y would pass the test
def questionOne():
    print()
    choice=input('Input y or Y: ')

    if choice.lower() == 'y':
        print('Pass')
    else:
        print('Fail')

    print()
    main()


#KV counts the number of free spaces in a string.  The string is given.
def questionTwo():
    print()
    myString='The best things in live are free.'
    counter=0
    spaces=0

    while counter<len(myString):
        if myString[counter]==' ':
            counter+=1
            spaces+=1
        else:
            counter+=1
    print('There are',str(spaces),'spaces in the string.')
    print()
    main()

#KV Checks to see if the user entered string ends in .com
def questionThree():
    print()
    str=input('Please enter a string: ')
    comChecker(str)
    print()
    main()

def comChecker(str):
    if str[-4:]=='.com':
        print('Your string ended in .com')
    else:
        print('Your string did not end in .com')

#KV User enters a string and then it is displayed backwards to them one character per line
def questionFour():
    print()
    str=input('Please enter a string: ')
    reverser(str)
    print()
    main()

def reverser(str):
    counter=0

    for letter in reversed(str):
        print(letter)


        
#KV This function has the lowercase1-5 scenarios from the lab entered into it.  It returns a True/False value depending on the string entered.
#I used 'test' as my string
def questionFive():
    print()
    str=input('Enter a string: ')

    print('Lowercase 1 returned:',any_lowercase1(str))
    print('Lowercase 2 returned:',any_lowercase2(str))
    print('Lowercase 3 returned:',any_lowercase3(str))
    print('Lowercase 4 returned:',any_lowercase4(str))
    print('Lowercase 5 returned:',any_lowercase5(str))

    
    print()
    main()
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
def any_lowercase3(s):
    for c in s:
        flag=c.islower()
    return flag
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
        return flag
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


#KV The user enters 3 strings.  The function checks to see if the first and second string are in the third string.  It then switches the first and second string in
#third string
def questionSix():
    print()
    string1=input('Please enter the first string: ')
    string2=input('Please enter the second string: ')
    string3=input('Please enter the third string: ')

    print()
    if string1 in string3:
        print('The first string is in the third string.')
    else:
        print('The first string is not in the third string.')

    print()
    if string2 in string3:
        print('The second string is in the third string.')
    else:
        print('The second string is not in the third string.')

    string4=string3.replace(string1,string2)

    print()
    print('Replacing string one with string two in string three nets:')
    print(string4)
    main()
    
    

    
def main():
    question=input('Which question? ')
    if question=='1':
        questionOne()
    if question=='2':
        questionTwo()
    if question=='3':
        questionThree()
    if question=='4':
        questionFour()
    if question=='5':
        questionFive()
    if question=='6':
        questionSix()
    else:
        main()
main()
