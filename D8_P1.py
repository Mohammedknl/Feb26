#Prog based on Reational and Logical operators using if conditions
'''
WAP to accept age and percentage of a candidate as the input and calculate whether
he is qualified or not qualified based on the age and percentage
if age is less than or equal to 25 and percentage is greater than or equal to 75 then
O/P:you are qualified  otherwise not qualified
'''
age=int(input("Enter age:"))
percent=float(input('Enter your percentage:'))
#print('Qualified') if age<=25 and percent>=75 else print('Not qualified')
if age<=25 and percent>=75:
    print('Qualified')
else:
    print('Not Qualified')
