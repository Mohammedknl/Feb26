#Working with else statements using for loop
#If break not occurs in for loop then else block will not be executed
#If break occurs in for loop then else block will execute
for i in range(1,11):
    if i==5:
        break
    print(i,end=' ')
else:
    print('\nI am from else block as break not occur')
print('\nI am from outside of all blocks')