names=['harsha','dhanush','abhi','rohan','vijay']
print(names[::-1]) #['vijay', 'rohan', 'abhi', 'dhanush', 'harsha']
print(names[::2]) #['harsha', 'abhi', 'vijay']
print(names[-1::-2])  #['vijay', 'abhi', 'harsha']
print(names[2]) #abhi
names[2]='sai'
print(names)  #['harsha', 'dhanush', 'sai', 'rohan', 'vijay'],adds only one element at a time at end
names.append("tanmai")
print(names) #['harsha', 'dhanush', 'sai', 'rohan', 'vijay', 'tanmai']
names.insert(2,'keerthi')
print(names)  #['harsha', 'dhanush', 'keerthi', 'sai', 'rohan', 'vijay', 'tanmai']
names.extend(['jai','surya','ram'])
print(names)  #['harsha', 'dhanush', 'keerthi', 'sai', 'rohan', 'vijay', 'tanmai', 'jai', 'surya', 'ram'],adds multiple elments at a time ,at the end
names.remove('tanmai')
print(names) #['harsha', 'dhanush', 'keerthi', 'sai', 'rohan', 'vijay', 'jai', 'surya', 'ram'],removes elment by giving element
names.pop(3)
print(names)  #['harsha', 'dhanush', 'keerthi', 'rohan', 'vijay', 'jai', 'surya', 'ram'],,removes elment by giving index
