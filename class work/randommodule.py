import random

#random.seed(100)
print(random.randint(1,6))
print(random.uniform(1,6))
names=['harsh','dhanush','abhinov','rohan']
print(random.choice(names))
print(random.choices(names))
print(random.shuffle(names))

