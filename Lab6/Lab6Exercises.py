#Parallel Processing

###Create 2 Corresponding Lists
##StudentNum=['1111','2222','3333','4444']
##StudentGrade=['B+','C','A','A-']
##
###Allow user to enter a student
##num=input('Search for a student number: ')
##
###Find the location of the student in the Student List
##location=StudentNum.index(num)
##
###Use the location of the desired student to find the corresponding
###grade in the grade list
##print('The grade for student #'+num+' is '+StudentGrade[location])

#Create a dictionary representing students and their grades
GradeBook={'1111':'B+','2222':'C','3333':'A','4444':'A-'}

#Allow user to enter a student:
num=input('Search for student number: ')

#Get teh grade for the student
print('The grade for the student #'+num+' is '+GradeBook[num])

