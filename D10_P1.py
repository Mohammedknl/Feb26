#WAP to print n natural no's in reverse order using while loop and for loop
'''
I/P:10
'''
n=int(input('Enter any no:'))
i=n
print('Natural numbers from {} to 1 in reverse order is:'.format(n))
while i>=1:
    print(i,end=' ')
    i=i-1
print('\nBelow result is using for loop')
for k in range(n,0,-1):
    print(k,end=' ')

