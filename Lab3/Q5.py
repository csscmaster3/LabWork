#KV get sales amount
sales=int(input('Sales:'))

##if sales<10000:
##    commissionRate=.10
##    print('Commissions Rate for $',sales,'is',commissionRate*100,'%')
##elif 10000<=sales<=15000:
##    commissionRate=.15
##    print('Commissions Rate for $',sales,'is',commissionRate*100,'%')
##else:
##    commissionRate=.20
##    print('Commissions Rate for $',sales,'is',commissionRate*100,'%')


#KV normal if statements for comissions rates
if sales<10000:
    commissionRate=.10
    print('Commissions Rate for $',sales,'is',commissionRate*100,'%')
if 10000<=sales<=15000:
    commissionRate=.15
    print('Commissions Rate for $',sales,'is',commissionRate*100,'%')
if sales>15000:
    commissionRate=.20
    print('Commissions Rate for $',sales,'is',commissionRate*100,'%')




