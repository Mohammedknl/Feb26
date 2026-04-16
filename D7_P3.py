#Short hand If statements in python
#WAP to check whether the number is even or odd
'''
I/P:Enter any no:5
O/P:It is Odd number
'''
x=int(input('Enter any number:'))
#Using variable and print function
#z="It is Even as test pass" if(x%2==0) else "It is Odd as test fails"
#print(z)
#Without using variable directly using print function
#print("It is Even as test pass and printing without storing in variable") if(x%2==0) else print("It is Odd as test fails")

#With Indentation and block of code
if(x%2==0):
    print("It is Even from if block")
else:
    print('It is Odd from else block')

print('It is from outside of blocks and it will print always as it is independent of if else conditions')

