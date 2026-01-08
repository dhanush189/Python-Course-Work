'''def display(uname,email,pwd):
    print(f'username:{uname}\nemail:{email}\npwd:{pwd}')
username=input()
gamil=input()
password=input()    
display(username,gamil,password)'''

#Keyword Arguments
'''''
def display(uname,email,pwd):
    print(f'username:{uname}\nemail:{email}\npwd:{pwd}')
username=input()
gamil=input()
password=input()   
display(uname=username,email=gamil,pwd=password)
display(email=gamil,uname=username,pwd=password)
display(email=gamil,pwd=password,uname=username)'''


#default parameters
"""""
def display(uname,email,pwd,status='absent'):
    print(f'username:{uname}\nemail:{email}\npwd:{pwd}\nstatus:{status}')
#username=input()
#gamil=input()
#password=input()
display('subhash','subhsh@gamil','123')
display('vinay','vinay@gamil','456','present')"""

#for variable no.of attributes
'''''
def display(*names):
    for i in names:
        print(i)
    print('------')    
display('subhash','vinay')    
display('abc','bcd','efg','wer')
display('dhanush')'''


#variable no.of keyword arguments
"""""
def display(**names):
    for i in names:
        print(f'{i}:{names[i]}')
    print('------')    
display(k1='subhash',k2='vinay')    
display(k1='abc',k2='bcd',k3='efg',k4='wer')
display(k1='dhanush')"""

#global declaration od variable in local
"""""
def display():
    global name
    name='lohit'
    print(f"Inside:{name}")
name="ram"
display()
print(f'outside:{name}') 
"""



def display():
    print(f'starting:{course}')
    def change():
        nonlocal course
        course='pyhton Full Stack'
        print(f'change:{course}')
    change()
    print(f"Final Course:{course}")    
course="java full stack"
display(course)

