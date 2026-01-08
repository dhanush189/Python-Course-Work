s='Python programming'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())
'''PYTHON PROGRAMMINGa
python programming
Python programming
Python Programming
pYTHON PROGRAMMING'''


print(s.center(35,'*'))
print(s.ljust(35,'*'))
print(s.rjust(35,'*'))
'''
*********Python programming********
Python programming*****************
*****************Python programming
'''
s='256'
print(s.zfill(7))#(zfill means Zero-fill)
#0000256

s='abc'
print(s.zfill(7))#(zfill means Zero-fill)


s='python programming power'
print(s.find('o'))
print(s.rfind('p'))
print(s.index('p'))
print(s.rindex('p'))
print(s.count('g'))

#m='Dhanush harsha abhinov'
#print(s.replace('p','*'))


#length of string
s='python programming'
print(len(s))#18
print(max(s))#y-print gratest ascii value of charecters
print(min(s))#y-print lowest ascii value of charecters

print(chr(128578))#🙂

print(sorted(s))#sorts and returns in list
#print(split().s)#splits into words returns in list

print(s.split())
s='dhanush.is_good.boy'
print(s.splitlines())
print(s.rsplit('.'))
print(s.partition('.'))
print(s.rpartition('.'))


s=['i','am','good','boy']
','.join(s)

k='   python     programming     '
print(k.strip())
print(k.lstrip())
print(k.rstrip())

text='hello,🙂'
print(text.encode())


print(k.isupper())
print(k.islower())
print(k.startswith(' '))
print(k.endswith(' '))
k='dhanush'
print(k.isalpha())
k='23dhanush'
print(k.isalnum())


