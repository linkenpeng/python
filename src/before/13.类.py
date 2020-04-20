#!/usr/bin/env python

class AddrBookEntry(object):
    'address book entry class'
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        print('Created instance for:',self.name)
    def updatePhone(self, newph):
        self.phone = newph
        print('Updated phone# for:', self.phone)
        
john = AddrBookEntry('John Doe','408-555-1212')
jane = AddrBookEntry('Jane Doe','650-555-1212')

print(john)
print(john.name)
print(john.phone)
print(jane)
print(jane.name)
print(jane.phone)
john.updatePhone('400-888-8888')
print(john)
print(john.name)
print(john.phone)
            
class EmplAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class'
    def __init__(self,nm,ph,id,em):
        AddrBookEntry.__init__(self,nm,ph)
        self.empid = id
        self.email = em
        
    def updateEmail(self,newem):
        self.email = newem
        print('Update e-mail address for:',self.email)
        
john = EmplAddrBookEntry('John Doe','408-555-1212',42,'john@spam.doe')
print(john)
print(john.name)
print(john.phone)
print(john.empid)
print(john.email)
john.updateEmail('john@163.doe')
print(john.email)
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    



