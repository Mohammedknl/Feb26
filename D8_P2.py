'''
WAP to accept any character through the keyboard and
print whether it is Vowel or Consonent
'''
x=input('Enter any character:')
# if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
# if (x=='a' or 'e' or 'i' or 'o' or 'u'):
#     print('It is Vowel')
# else:
#     print('It is Consonent')

#II way using Membership operator
print('It is Vowel') if x in 'a,e,i,o,u' else print('It is Consonent')
print('It is Consonent') if x not in 'a,e,i,o,u' else print('It is Vowel')