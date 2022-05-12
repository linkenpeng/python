
x = [1, 2, 3, 3, 'a', 3, True]
s = [1, 2, 3]

print(s in x)
print(s not in x)
print(s + x)
print(s*2)
print(s[1])
# 切片 步长2
print(x[1:4:2])
# 从后往前
print(x[::-1])
print(len(x))

print(min(s))
print(max(s))

print(s.index(2))
print(x.index(3, 2, 6))

print(x.count(3))