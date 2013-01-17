#Cups to Ounces
#Kevin Varcasio
#17/01/2013
#Convert Cups to Ounces

def main():
    #KV Runs the beginning of the program
    intro()
    
    #KV Find out cups needed from the user
    cups_needed = float(input('Enter the number of cups: '))
    
    #KV Call function to Convert from cups to ounces
    cups_to_ounces(cups_needed)
    

#KV Intro to the program
def intro():
    print ('This program converts measurements')
    print ('in cups to fluid ounces. For your')
    print ('reference the formula is:')
    print ('    1 cup = 8 fluid ounces')
    print ()

#KV convert from cups to ounces
#KV Display result to user
def cups_to_ounces(cups):
    ounces = cups * 8
    print ('That converts to', ounces, 'ounces.')

# Run the whole program as defined in def main() 
main()
