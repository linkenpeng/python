import random

def rand():
    random.seed(10)
    print(random.random())
    print(random.getrandbits(16))
    print(random.randint(1,10))
    print(random.choice([1,2,3,4,5,6,7]))
    print(random.shuffle([1,2,3,4,5,6,7]))
    
if __name__ == '__main__':
    rand()
    
    
    
    
    
    
    
    
    