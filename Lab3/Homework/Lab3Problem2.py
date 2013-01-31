# Divisability
# 31/01/2013
# Kevin Varcasio
# Checks to see if a number is divisible by 5 and 6 and then 5 or 6

#KV determine if the inputed number is divisibly by 5 and 6
def determineAND(a):
    if (a % 5 == 0 and a % 6 == 0):
        print(a,'is divisible by 5 and 6.')
    else:
        print(a,'is not divisible by 5 and 6.')
        
#KV determine if the inputed number is divisibly by 5 or 6
def determineOR(a):
    if (a % 5 == 0 or a % 6 == 0):
        print(a,'is divisible by 5 or 6.')
    else:
        print(a,'is not divisible by 5 or 6.')

#KV Define main; get input from user and run the two determine functions
def main():
    num=int(input("Enter a integer value: "))
    determineAND(num)
    determineOR(num)

main()

            



