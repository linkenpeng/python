
def print1():
    print("Hello, %s!" % "World")
    print("The number is %d" % 42)
    print("The number in hex is %x" % 255)

def print2():
    print("Hello, {}!".format("World"))
    print("The number is {}".format(42))
    print("The number in hex is {0:x}".format(255))
    print("Left aligned: {:<10} | Right aligned: {:>10}".format('left', 'right'))
    
def print3():
    name = "World"
    number = 42
    print(f"Hello, {name}!")
    print(f"The number is {number}")
    print(f"The number in hex is {number:x}")
    
def print4():
    values = {'name': 'World', 'number': 42}
    print("Hello, %(name)s! The number is %(number)d" % values)
    print("Hello, {name}! The number is {number}".format_map(values))
    
if __name__ == '__main__':
    print1()
    print('-' * 30)
    print2()
    print('-' * 30)
    print3()
    print('-' * 30)
    print4()
    
    
    
    
    
    
    
    
    
    