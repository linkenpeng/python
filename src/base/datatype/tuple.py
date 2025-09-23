
# 返回的其实是元组
def func():
    return 1, 2

def init():
    x = (1,2,3,4,5)
    a, *b = x # a占第一个，剩余的组成列表全给b
    # a -> 1
    # b -> [2, 3, 4, 5]
    # a, b -> (1, [2, 3, 4, 5])

    a, *b, c = x # a占第一个，c占最后一个，剩余的组成列表全给b
    # a -> 1
    # b -> [2, 3, 4]
    # c -> 5
    # a, b, c -> (1, [2, 3, 4], 5)
def test():
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

if __name__ == '__main__':
    init()