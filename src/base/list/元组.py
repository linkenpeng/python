
# 返回的其实是元组
def func():
    return 1, 2

# 元组一旦创建就不可修改
creature = "cat", "dog", "tiger", "human"

print(creature)

color = (0x001100, "blue", creature)
print(color)

print(creature[::-1])
print(color[-1][2])

ls = [1, 2, 3]
it = tuple(ls)
print(it)

ls2 = list(creature)
print(ls2)
it2 = tuple(ls2)
print(it2)