# WAP to find the volume of sphere with a radius 5 using Userdefine module functions
'''
1.I/P:r=5
2.Logic:4/3*3.14*r*r*r
3.O/P:Volume of Sphere with a radius 5 is:XXXX
'''
#r=5
import math
r=int(input("Enter any value for radius:"))
#vol=4/3*3.14*r*r*r
vol=4/3*math.pi*r*r*r
print('Volume of Sphere with a radius 5 is:',vol)
print('Volume of Sphere with a radius 5 is:',round(vol,3))

'''
Take Rahul's Basic salary as the input through the keyboard,
His Dearness allowance is 50% of his basic and House rent allowance is 30% of his basic salary WAP to calculate his total salary

I/P:Enter Basic Salary of Rahul:100
D.A=50(50/100*100)
H.R.A=30
Total salary=basic+D.A+H.R.A=180
O/P:Rahul's Total Salary =180
'''

