## SSN Checker
## 27/02/2013
## Kevin Varcasio
##Write a program that prompts the user to enter a social security number in the format
##DDD-DD-DDDD, where D is a digit.The program will check if the ssn was entered in
##a valid format.

def main():
    #KV Get the SSN from the user
    SSN=str(input('Plase enter the social security number in this format: DDD-DD-DDDD: '))


    #KV Checks to see if '-' is at positions 3 and 6.  If it is print the respective lines, if it isn't there the
    #program will either purposely crash or I force an exit (depending if '-' isn't found or just in the wrong place)
    if SSN.index('-', 3) == 3 and SSN.index('-', 6) == 6 :
        print("Found '-' at position 3")
        print("Found '-' at position 6")
    else:
        exit()

    #KV Split SSN into 3 different sections using '-' as the seperator
    SSN1, SSN2, SSN3 = SSN.split('-')
    print('The social security split into 3 parts: ', SSN1, SSN2, SSN3)

    #KV Print T/F if SSN1-3 is all digitis and then how many characters are in each section
    print('Part 1 of SSN is all digits:',SSN1.isdigit(),'and has',len(SSN1),'characters')
    print('Part 2 of SSN is all digits:',SSN2.isdigit(),'and has',len(SSN2),'characters')
    print('Part 3 of SSN is all digits:',SSN3.isdigit(),'and has',len(SSN3),'characters')

main()

