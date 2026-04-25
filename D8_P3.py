#Working with Nested If else conditional flow statements
'''
WAP to check whether the student has passed or failed based on
3 subject marks and average using Nested If else statements
Case1:I/P:Enter your name:Tahoora
Enter Subject1 Marks:50
Enter Subject 2 marks:50
Enter Subject 3 Marks:50
O/P:
Sum of Marks:150
Avg of Marks=50
Congratulations Tahoora you passed the exam (If all Subject Marks>=40 and avg >=40)
Case2:I/P:Enter your name:Tahoora
Enter Subject1 Marks:30
Enter Subject 2 marks:30
Enter Subject 3 Marks:30
O/P:
Sum of Marks:90
Avg of Marks=30
Tahoora you Failed the exam(If Subject Marks<40 and avg <40)
Case3:I/P:Enter your name:Tahoora
Enter Subject1 Marks:100
Enter Subject 2 marks:50
Enter Subject 3 Marks:0
O/P:
Sum of Marks:150
Avg of Marks=50
Tahoora you Failed in subject(If Subject Marks>40 and avg >40)
'''
from tokenize import Single3

n=input('Enter your name:')
S1=int(input('Enter Subject1 Marks:'))
S2=int(input('Enter Subject2 Marks:'))
S3=int(input('Enter Subject3 Marks:'))
tot=S1+S2+S3
avg=(tot/3)
print('total=',tot)
print('average=',round(avg,2))
if avg>=40:
    if S1>=40 and S2>=40 and S3>=40:
        print('Congratulations {} you passed the exam'.format(n))
    else:
        print('{} you failed in subject'.format(n))
else:
    print('{} you Failed the exam'.format(n))



