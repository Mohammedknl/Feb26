#Assignment
price=int(input("enter total meal price:"))
tip=price*7/100
salestax=price*15/100
total=price+tip+salestax
# Tip amount is:7
#Sales Tax amount is:15
#Total amount to pay is:122
print('Tip amount is:',int(tip))
print('Tip amount is:%d'%(tip))
print('Tip amount is:{}'.format(tip))