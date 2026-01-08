products=['iphon','headset','smartwatch','tv','ac']
product=input("enter product").strip()
for i in products:
    if i==product:
        print(f"{product} is found.you can buy it.")
        break
else:
    print(f"{product} is not found")    

