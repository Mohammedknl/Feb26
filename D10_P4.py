#Working with Nested loops and structural pattern matching
for i in range(1,6):
    for j in range(1,6):
        print('*',end=' ')
    print()

'''
1
2 2 
3 3 3
4 4 4 4
5 5 5 5 5

'''
n=5
for i in range(1,n+1):  #i=1,2,3,4,5
    for j in range(1,i+1): #(1,6)
        print(i,end=' ')
    print()

'''
1 
2 1
3 2 1
4 3 2 1
5 4 3 2 1

'''