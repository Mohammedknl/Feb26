'''
WAP to accept marks of 3 subjects and display the grade based on avg marks
I/P:Enter Subject1 marks
    Enter Subject2 marks
    Enter Subject3 marks
avg=...
O/P:Grade A if avg is greater than or equal to 70
    Grade B if avg is between 60 and 70
    Grade C if avg is between 50 and 60
    Grade D if avg is between 40 and 50
    Grade F if avg is between less than 40
'''
S1=int(input('Enter Subject1 Marks:'))
S2=int(input('Enter Subject2 Marks:'))
S3=int(input('Enter Subject3 Marks:'))
avg=float((S1+S2+S3)/3)
print('average=',avg)
#Method 1 using elif keywords
# if avg>=70:
#     print('Grade A')
# elif avg>=60:
#     print('Grade B')
# elif avg>=50:
#     print('Grade C')
# elif avg>=40:
#     print('Grade D')
# else:
#     print('Grade F')
#Method 2 using match and case
match avg:
    case _ if avg>=70:
        print('Grade A')
    case _ if avg>=60:
        print('Grade B')
    case _ if avg>=50:
        print('Grade C')
    case _ if avg>=40:
        print('Garde D')
    case _:
        print('Grade F')