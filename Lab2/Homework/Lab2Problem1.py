# Kilometers to Miles
# 24/01/2013
# Kevin Varcasio
# Convert kilometers to miles

#KV Global constant for k to m
KILOMETERS_TO_MILES=float(0.6214)

#KV Define the main function; get distance and pass to conversion function
def main():
    distance=float(input('Distance in kilometers: '))
    showMiles(distance)

#KV converts km to m and displays output
def showMiles(distance):
    converted=KILOMETERS_TO_MILES*distance
    print('Conversion of',distance,'kilometers to miles:',converted,'miles')

main()
    
    
