'''
WAP to exchange only first and last character of a string 'Hello World'
'''
s='Hello World'
x=s[-1]+s[1:-1]+s[0]
y=s[-1]+s[1:len(s)-1]+s[0]

print(x)
print(y)
