print('I like to use the Internet for:')
for item in ['e-mail', 'net-surfing', 'homework', 'chat']:
    print(item,),
print()

who = 'knights'
what = 'Ni!'
print('We are the', who ,'who say', what ,what, what, what)
print('We are the %s who say %s' % (who, ((what + ' ') * 4)))

for eachNum in [0, 1, 2]:
    print(eachNum)
    
print('range')
for eachNum in range(3):
    print(eachNum)
    
foo = 'abc'
for c in foo:
    print(c)
    
for i in range(len(foo)):
    print(foo[i], '(%d)' % i)
    
print()
print('enumerate')
for i, ch in enumerate(foo):
    print(ch, '(%d)' % i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    