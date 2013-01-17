# TestFunctions
# 17/01/2013
# Kevin Varcasio
# Tests some of the built in functions in Python

#KV get inputs from user
posInteger=int(input('Please enter a positive integer:'))
negInteger=int(input('Please enter a negative integer:'))
myChar=int(input('Please enter a value between 48 and 122 inclusively:'))
myString=str(input('Please enter a string:'))

#KV display absolute values
print('The absolute value of the positive integer is:', abs(posInteger))
print('The absolute value of the negative integer is:', abs(negInteger))

#KV Displays character from string
print('The character stored is:',chr(myChar))

#KV Print length of string
print('The length of the string is:',len(myString))

#KV Raised posInteger to the 4th power and print
myPower=posInteger**4
print(posInteger,'to the fourth power is', myPower)
