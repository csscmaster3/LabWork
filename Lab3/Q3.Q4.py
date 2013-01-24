#KV Declare variable

exam=int(input('Exam score:'))
programsDone=int(input('programsDone:'))



if exam>=60 and programsDone>=10:
    print('Passed')
else:
    print('Failed')

print()

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


n=0
print('N=',n,'(n<0 or (0<=n<=100) or n>100) is',n<0 or (0<=n<=100) or n>100 )
n=150
print('N=',n,'(n<0 or (0<=n<=100) or n>100) is',n<0 or (0<=n<=100) or n>100 )
n=-50
print('N=',n,'(n<0 or (0<=n<=100) or n>100) is',n<0 or (0<=n<=100) or n>100 )
n=100
print('N=',n,'(n<0 or (0<=n<=100) or n>100) is',n<0 or (0<=n<=100) or n>100 )







