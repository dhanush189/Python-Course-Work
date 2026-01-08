    #stmts
#seq: list,tuple,set,dict,str
l=['mohan',"rohan",'vishnu','mani']
for i in l:
    i.title()
print(l)    
products={'airpods':3000,'iphone':100000,'smartwatch':9000}
for i in products:
    print(i,products[i])

s='dhanush'
for i in s:
    if i in ['a','e','i','o','u']:
        print(i)    
k=['airpods','iphone','smartwatch']
for i in range(len(k)):
    print(i,k[i])

t=['airpods','iphone','smartwatch']
for i in enumerate(t):
    print(t)
    