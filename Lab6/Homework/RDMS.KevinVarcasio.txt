## Relational Database MAnagement System
## 3/14/2013
## Kevin Varcasio
##Develop a RDBMS (Relational Database Management System) in Python.
##The DBMS should actually be written in Python, not just interface
##with some other DBMS.  This system should track students:  Personal Data and Grades.  
##The system should contain the following features:User menu of choices, Add a record, delete a
##record, report on the database

#KV Setting up 3 blank tables
nameList=['']
idList=['']
gradeList=['']

#KV Add to the databases using student ID as the index key
def dbADD():
    print()
    print('Add')
    
    id=input('What is the 4 digit student ID number?: ')
    idList.append(id)
    name=input("What is the student's name?: ")
    nameList.append(name)
    grade=input("What is the student's grade?: ")
    gradeList.append(grade)

    print('Record added.')

    print()
    main()

#KV Delete a student from the databases by using their student ID
def dbDELETE():
    print()
    print('Delete')
    id=input('What is the 4 digit student ID number?: ')
    #KV Look up the position of the student ID is the idList and use that position on the other lists
    query=idList.index(id)
    idList.pop(query)
    nameList.pop(query)
    gradeList.pop(query)
    
    print()
    main()

#KV Query a student from the databases by using their student ID    
def dbQUERY():
    print()
    print('Query')
    id=input('What is the 4 digit student ID number?: ')
    #KV Look up the position of the student ID is the idList and use that position on the other lists
    query=idList.index(id)
    print("The student's name is: ",nameList[query])
    print("The student's grade is: ",gradeList[query])
    print()
    main()

#KV Define main with a menu and choices
def main():
    print('1: Add a record')
    print('2: Delete a record')
    print('3: Query Database')
    print('4: Quit')
    choice=int(input('What would you like to do? '))

    if choice == 1:
        dbADD()
    if choice == 2:
        dbDELETE()
    if choice == 3:
        dbQUERY()
    if choice == 4:
        exit
main()

