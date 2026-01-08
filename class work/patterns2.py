n=int(input('enter the size:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n//2:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()            