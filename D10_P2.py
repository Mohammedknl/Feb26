#Working with break,continue and pass flow control statements
for i in range(1,11):
    if i==4:
        break
    print(i,end=' ')
print('\nThis line is after the for loop')
for j in range(1,11):
    if j==4:
        continue
    print(j,end=' ')
for k in range(1,11):
    if k==4:
        pass
    print(k,end=' ')