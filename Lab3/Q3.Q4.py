#KV Q3 Declare variable

exam=int(input('Exam score:'))
programsDone=int(input('programsDone:'))


#KV Q3 Compare against 60 and 10 display pass/fail
if exam>=60 and programsDone>=10:
    print('Passed')
else:
    print('Failed')

print()

#KV Q4, testing of IF statements
if 0:
    print('0 is true\n')
else:
    print('0 is false\n')

if 1:
    print('1 is true\n')
else:
    print('1 is false\n')


if -1:
    print('-1 is true\n')
else:
    print('-1 if false\n')

extra=2
if(extra<0):
    print('small\n')
else:
    if(extra==0):
        print('medium\n')
    else:
        print('large\n')

if(extra<0):
    print('small\n')
elif(extra==0):
    print('medium\n')
else:
    print('large\n')

#KV Q4 compare n to the same statement
n=0
print('N=',n,'(n<0 or (0<=n<=100) or n>100) is',n<0 or (0<=n<=100) or n>100 )
n=150
print('N=',n,'(n<0 or (0<=n<=100) or n>100) is',n<0 or (0<=n<=100) or n>100 )
n=-50
print('N=',n,'(n<0 or (0<=n<=100) or n>100) is',n<0 or (0<=n<=100) or n>100 )
n=100
print('N=',n,'(n<0 or (0<=n<=100) or n>100) is',n<0 or (0<=n<=100) or n>100 )







