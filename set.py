s = set('cheeseshop')
print(s)
t = frozenset('bookshop')
print(t)
print(type(s))
print(type(t))

print('e' in s)
print('e' not in t)

for i in s:
    print(i)
    
print(s > t)