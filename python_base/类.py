class FooClass(object):
    """ my very first class: FooClass"""
    version = 0.1   # class (data) attribute
    
    def __init__(self, nm = 'John Doe'):
        """constructor"""
        self.name = nm # class instance (data)
        print('Created a class instance for', nm)
    
    def showname(self):
        """display instance attribute and class name"""
        print('Your name is ', self.name)
        print('My name is', self.__class__.__name__)
    
    def showver(self):
        """ display class(static) attribute"""
        print(self.version) # references FooClass.version
        
    def addMe2Me2(self, x):
        """apply + operation to argument"""
        return x + x

foo1 = FooClass()
foo1.showname()
foo1.showver()
print(foo1.addMe2Me2(5))
print(foo1.addMe2Me2('xyz'))
print()

print('Another instance')
foo2 = FooClass('Myron Linken')
foo2.showname()

print()
print('-' * 20)

#print(dir(foo2))
#print(help(foo2))
#print(str(foo2))
#print(type(foo2))

print(foo2.showname.__doc__)



