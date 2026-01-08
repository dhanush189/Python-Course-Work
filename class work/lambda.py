
#using normal function
def wish(name):
    return f"welcome to pthon course {name}!!"
print(wish("dhanush"))
print(wish("suman"))

#using Lamda function

wish1= lambda name: f"welcome to python course {name}"
print(wish1("dhanush"))
print(wish1("dhanush"))


def greatest(a,b):
    if a>b:
        return a
    else:
        return b
print(greatest(19,56))    


#using Lamda function
# funtion name: lambda (parameters): logic in function

greatest= lambda a,b: a if a>b else b
print(greatest(12,52))

#using Lamda function
# funtion name: lambda (parameters): logic in function

sum1= lambda a,b,c: a+b+c
print(sum1(12,52,69))

#map,Filter,Reduce
l=[1,2,3,4,5]
def even(l):
    l1=[]
    for i in l:
        if i%2==0:
            l1.append(i)
    return l1
print(even(l))

#using filter for finding even in list
l1=list(filter(lambda i:i%2==0, l))
print(l1)



k=[1,2,0,0,0,0,3,4,0,5,0,0,0,0,]
def removezero(k):
    k1=[]
    for i in l:
        if i!=0:
            k1.append(i)
    return k1
print(removezero(k))


#using filter for removing zeroes
k12=list(filter(lambda i:i!=0, k))
print(k12)


def sumof(l):
    sum1=0
    for i in l:
        sum1+=i
    return sum1
print(sumof(l))    

reduce(lambda sum,i:)

