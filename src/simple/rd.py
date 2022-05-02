import random

random.seed(10)
print(random.random())
print(random.getrandbits(16))
print(random.randint(1,10))
print(random.choice([1,2,3,4,5,6,7]))
print(random.shuffle([1,2,3,4,5,6,7]))