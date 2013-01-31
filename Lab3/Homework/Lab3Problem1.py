# Book Awards
# 31/01/2013
# Kevin Varcasio
# Award points based on the numbers of books a user inputs

#KV Define the simple if function 
def simpleIfFunction(a):
    if a == 0:
        print("The simpleIfFunction awarded 0 points.")
    if a == 1:
        print("The simpleIfFunction awarded 5 points.")
    if a == 2:
        print("The simpleIfFunction awarded 15 points.")
    if a == 3:
        print("The simpleIfFunction awarded 30 points.")
    if a >= 4:
        print("The simpleIfFunction awarded 60 points.")
        
    
#KV define the nested If function
def nestedIfFunction(a):
    if a == 0:
        print("The nestedIfFunction awarded 0 points.")
    else:
        if a == 1:
            print("The nestedIfFunction awarded 5 points.")
        else:
            if a == 2:
                print("The nestedIfFunction awarded 15 points.")
            else:
                if a == 3:
                    print("The nestedIfFunction awarded 30 points.")
                else:
                    if a >= 4:
                        print("The nestedIfFunction awarded 60 points.")

#KV define the elif function
def elifFunction(a):
    if a == 0:
        print("The elifFunction awarded 0 points.")
    elif a == 1:
        print("The elifFunction awarded 5 points.")
    elif a == 2:
        print("The elifFunction awarded 15 points.")
    elif a == 3:
        print("The elifFunction awarded 30 points.")
    elif a >= 4:
        print("The elifFunction awarded 60 points.")
    
#KV Define main; get user input and call the different if functions
def main():
    books=int(input("Number of books puchased for the month: "))
    if books < 0:
        print("Invalid entry, please try again.")
        main()
    else:
        simpleIfFunction(books)
        nestedIfFunction(books)
        elifFunction(books)


main()






    
    
