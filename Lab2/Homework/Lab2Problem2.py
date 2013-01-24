# Monthly Expenses
# 24/01/2013
# Kevin Varcasio
# Get monthly expenses and generate a total

#KV Define the main function; get inputs from user
def main():
    loan=float(input('Monthly loan amount: '))
    insurance=float(input('Monthly insurance amount: '))
    gas=float(input('Monthly gas amount: '))
    oil=float(input('Monthly oil amount: '))
    tires=float(input('Monthly tires amount: '))
    maintenance=float(input('Monthly maintenance amount: '))
    showExpenses(loan,insurance,gas,oil,tires,maintenance)

#KV Sums expenses and outputs total
def showExpenses(a,b,c,d,e,f):
    total=round(a+b+c+d+e+f,2)
    annual=total*12
    print('Total Monthly Expense:',total)
    print('Total Annual Expense',annual)

main()
    
    
