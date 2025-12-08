#Python
product_quantity = 3 
order_id = 10987432 
#b. float – Floating-point 

product_price = 749.99 
discount_percentage = 15.5 
average_rating = 4.3 

"""c. complex – Complex Numbers 
Rarely used in e-commerce. Could be used in specialized analytics or image processing. 
Python"""


z = 5 + 2j  # Not commonly used in typical e-commerce 

""""
2. Sequence Types 
a. str – String 
Used for names, addresses, categories, product descriptions, etc. 
Python"""


customer_name = "Rohit Sharma" 
delivery_address = "Bangalore, Karnataka" 
product_category = "Electronics" 

"""b. list – List 
Used to store lists of items such as products in a cart, wishlist, or categories. 
Python"""

cart_items = ["Shoes", "T-shirt", "Headphones"] 
top_categories = ["Mobiles", "Fashion", "Home", "Beauty"] 



"""3. Set Types 
a. set – Set 
Used to store unique items like available sizes or brands without duplicates. 
Python"""

available_sizes = {"S", "M", "L", "XL"} 
popular_brands = {"Nike", "Adidas", "Puma", "Nike"}  # 'Nike' 

""""" 
b. frozenset – Immutable Set 
Used when a fixed set of categories or tags should not be modified. 
Python"""

frozen_tags = frozenset(["Sale", "Limited Edition", 
"Trending"]) 

"""4. Mapping Type 
a. dict – Dictionary 
Used extensively to map product attributes, customer info, or order details. 
Python"""

product_details = { 
"name": "Wireless Mouse", 
"brand": "Logitech", 
"price": 899.99, 
"rating": 4.5 
} 
customer_profile = { 
"name": "Anjali Verma", 
"email": "anjali@example.com", 
"prime_member": True 
} 

"""5. Boolean Type 
a. bool – Boolean 
Used to check conditions like payment status, availability, or login status. 
Python"""

is_logged_in = True 
is_payment_successful = False 
is_in_stock = True

"""6. None Type 
a. NoneType – Represents a null or missing value 
Used when something is not yet assigned, like delivery tracking not yet available. 
Python"""

tracking_number = None 
delivery_partner = None