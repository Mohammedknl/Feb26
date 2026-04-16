#WAP to print "addition of 2 and 3 is 5" using 3 diff string formatting methods
#I Way of string formatting using comma operator
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
c=a+b
# addition of 2 and 3 is 5
print("addition of",a,"and",b,"is",c)
#II method of string formatting using string modulo operator(%d,%f,%s)
print('addition of %d and %d is %d'%(a,b,c))
print('addition of %d and %d is %.2f'%(a,b,c))

#III method is using place holder/format specifier  {}
print('addition of {} and {} is {}'.format(a,b,c))
print('addition of {} and {} is {:.2f}'.format(a,b,c))

#IV Method using Fstring
d=f"addition of {a} and {b} is {c}"
print(f"addition of {a} and {b} is {c:.2f}")
print(d)



'''
WAP to accept price for a meal and calculate a tip of 7%,
sales tax of 15% and print the total amount to be paid for a meal
I/P:100
tip=7
st=15
tot=100+7+15=122
O/p:the tip amount is:7
     the sales tax is:15
     Total amount paid is:122   
print he above statement using 3 different string formatting methods
'''

