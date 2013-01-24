#KV Declare variable
count=int(0)
limit=int(10)

#KV display value of variables
print('Count is',count)
print('Limit is',limit,'\n')

#KV Show the description of all the boolean operations and the result
print('Count equal to 0 is', count==0)
print('Limit greater than or equal to 10 is', limit>=10)
print('Limit less than count+10 is',limit<=count+10)
print('Count+10 less than or equal to limit is', count+10<=limit)
print('Count equal to 0 and limit less than 20 is',(count==0) and (limit<20))
print('Count equal to 0 and limit less than 20 is', count==0 and limit<20)
print('Limit greater than 20 or count less than 5 is',(limit>20) or (count<5))
print('Not count is equal to 12 is',not(count==12))
print('Count is equal to 1 and x is less than y is',(count==1)and(x<y))
print('Count less than 10 or x less than y is', (count<10)or(x<y))
print('Not count is less than 10 or x is less than y and count is greater than 0 is', not((count<10)or(x<y)and(count>=0)))
print('Limit/count is greater than 7 or limit is less than 20 will generate a divide by zero error')#,((limit/count)>7)or(limit<20))
print('Limit is less than 20 or limit/count is greater than 7 is',(limit<20)or((limit/count)>7))
print('Limit/count is greater than 7 and limit is less than 0 will generate a divide by zero error')#,((limit/count)>7)and(limit<0))
print('Limit is less than 0 and limit/count is greater than 7 is', (limit<0)and((limit/count)>7))
