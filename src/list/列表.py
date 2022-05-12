
ls = ["cat", "dog", "tiger", 1024]
ls2 = [9, 8]
print(ls)

# 只是赋值，同一个地址
lt = ls
lt.append("jak")

print(ls)

ls[1] = "chicken"
print(ls)

ls[0:1:1] = "aa"
print(ls)

del ls[0:1:1]
print(ls)

print(ls + ls2)
print(ls2 * 2)



print(ls2.append(7))
print(ls2.clear())
print(ls.copy())
print(ls.insert(0, 99))
print(ls.pop(0))
print(ls.remove(1024))
print(ls.reverse())
print(ls.index("dog"))