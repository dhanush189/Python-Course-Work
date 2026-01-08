'''def display(n,ind):
    if(ind==(len(s)-n+1)):
        return
    print(s[ind:ind+n])
    display(n,ind+1)

n=int(input("Enter the step value:"))
s='abcdef'
display(n,0)'''

def sumpro(i):
    if i==0:
        return
    print(sumpro(i)+sumpro(i-1))
    sumpro(i-1)

n=int(input())
sumpro(n)

