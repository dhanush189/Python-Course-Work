x = 10           
print(x)        



age = 25         
def greet():     
# 'age' is an identifier for the variable 
# 'greet' is an identifier for a function
         
#_name = "John"      
 score1 = 88         
# 1age = 30          
# 'age' is an identifier (valid) 
# '_name' is a valid identifier 
# valid: letters + digits 
# Invalid examples (will cause errors if uncommented) 
# Invalid: starts with a digit 
# def = 5            
# Invalid: 'def' is a Python keyword 


# This is a single-line comment 
x = 10  # This is also a comment 

#Python
''' This is a multi-line comment. 
It spans multiple lines. 
''' 
print("Hello, World!")

product_name = "Laptop" 
price = 45000 
in_stock = True 
print(product_name, price, in_stock)

a, b, c = 10, 20, 30 
print(a, b, c)  # Output: 10 20 30

#Python
a, b = 5, 10 
a, b = b, a 
print(a, b)  # Output: 10 5


x = 100 
del x 
# print(x)  # Raises: NameError: name 'x' is not defined