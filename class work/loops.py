chances=0
storedpin="12345"
while chances<5:
    pin=input("enter the pin")
    if pin==storedpin:
        print("login successful")
        break
    else: 
        print("password incorrect")    
        chances+=1
else:
    print("Try gain after 30 secs")
