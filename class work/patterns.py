n=int(input())
m=n//2
for row in range(n):
    for col in range(n):
        if row==0 or row==m or col==0 or col==n-1:
            print('*',end=' ')
        else:
            print(end='  ')
    print()    



          
