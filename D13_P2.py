#Working with String count,find and index methods
s='foo bar foo baz qwe foo'
print(len(s))
print(s.count('foo'))
print(s.count('o'))
print(s.count('foo',4))
print(s.count('foo',4,11))
print(s.count('foo',4,15))
#index method will always returns the index positon of a substring
print(s.index('foo'))
print(s.index('baz'))
print(s.index('baz',9))
#Index method searches always from 0th index
#find method
print(s.find('baz'))
print(s.find('foo',6))
print(s.find('Tahoora')) #-1
#print(s.index('Tahoora')) #value error it will raise