#Inflation Calculator
#Kevin Varcasio
#17/01/2013
#Calculate inflation based on a two year price

#KV Enter price of the items
year1=float(input('Please enter the price of the item in Year 1:'))
year2=float(input('Please enter the price of the item in Year 2:'))

#KV Calculate and display inflation
def inf():
    inf=((year2-year1)/year1)
    print('The inflation is:',round((inf*100), 2),'%')

inf()
