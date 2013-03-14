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

###Create a dictionary representing students and their grades
##GradeBook={'1111':'B+','2222':'C','3333':'A','4444':'A-'}
##
###Allow user to enter a student:
##num=input('Search for student number: ')
##
###Get teh grade for the student
##print('The grade for the student #'+num+' is '+GradeBook[num])
##
##print(GradeBook["3333"])
##
###To add to a dictionary
##GradeBook["5555"]='F'
##
###Looping through a dictionary
##for grade in GradeBook:
##    print(grade,GradeBook[grade])
##
###The len function returns the number of items in teh dictionary
##print(len(GradeBook))
##
###You can search for a key in the dictionary
##print('6666' in GradeBook)
##print('5555' in GradeBook)
##
###or search for a vlue in the dictionary
##print('A-' in GradeBook)
##print('A-' in GradeBook.values())

##studentData = {'1111':['A','B','A','A'], '2222':['A','B','B','B'], '3333':['D','C','C','A']}
##studentNum = input('Search for student#: ')
##
##print('The grades for student # ' + studentNum + ' are ' + str(studentData[studentNum]))
##
##newStudentList=studentData.copy()
##print(newStudentList)
##
##newStudentList.clear()
##print(newStudentList)
##
##newList=('name','class','grade')
##initializedStudentList=dict.fromkeys(newList)
##print(initializedStudentList)
##
##
##print(studentData.items())
##print(studentData.keys())
##print(studentData.values())
##studentData.pop('2222')
##print(studentData.keys)



students ={'1111':{'name':'John Smith','phone':'555-2341','addr':'23 Foo Drive'},'2222':{'name':'Mary Alice Black','phone':'555-9102','addr':'42 Bar Street'},'3333':{'name':'Kenneth Aaron','phone':'555-3158','addr':'Baz Avenue 90'}}

d=dict(students)
print(d)
print(len(d))
print(d['3333'])


labels={'phone':'phone number','addr':'address'}

