## Loan Calculator
## 14/02/2013
## Kevin Varcasio
## Write a python program that lets the user enter the loan
## amount and loan period in number of years.  The program will
## then display the monthly andtotal payments for each interest
## rate starting from 4 to 8 in increments of 1. 

import math

#KV - define calculation, calculation loan values based on inputs
def calculation():
    loanAmt=int(input('Please enter the amount (greater than 0) of the loan: '))
    numYears=int(input('Please enter the number of years as an interger: '))
    print('Rate\t','Monthly Payment\t', 'Total Payment\t')
    for monthlyRate in range (4,9):
        monthlyPayment = loanAmt * (monthlyRate/12/100) / (1 - math.pow(1 / (1 + (monthlyRate/12/100)), numYears * 12))
        totalPayment = monthlyPayment * numYears * 12
        print(monthlyRate,'%\t$',round(monthlyPayment,2),'\t$',round(totalPayment,2))


#KV - define main, set up while loop for calculations
def main():
    contin='y'
    while contin!='n':
        calculation()
        contin=str(input('Do you want to continue? (Type n to stop): '))
main()
    
            



