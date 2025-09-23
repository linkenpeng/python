def init():
    s = {} # 空集合
    s = {'5元', '10元', '20元'} # 定义集合
    s = set() # 空集合
    s = set([1,2,3,4,5]) # {1, 2, 3, 4, 5}（使用列表定义）
    s = {1, True, 'a'}
    s = {1, 1, 1} # {1}（去重）
    type(s) # set（类型检测）

    s = {'a', 'b', 'c'}

    # 判断是否有某个元素
    'a' in s # True

    # 添加元素
    s.add(2) # {2, 'a', 'b', 'c'}
    s.update([1,3,4]) # {1, 2, 3, 4, 'a', 'b', 'c'}

    # 删除和清空元素
    s.remove('a') # {'b', 'c'}（删除不存在的会报错）
    s.discard('3') # 删除一个元素，无则忽略，不报错
    s.clear() # set()（清空）

    s1 = {1,2,3}
    s2 = {2,3,4}

    s1 & s2 # {2, 3}（交集）
    s1.intersection(s2) # {2, 3}（交集）
    s1.intersection_update(s2) # {2, 3}（交集，会覆盖s1）

    s1 | s2  # {1, 2, 3, 4}（并集）
    s1.union(s2) # {1, 2, 3, 4}（并集）

    s1.difference(s2) # {1}（差集）
    s1.difference_update(s2) # {1}（差集，会覆盖s1）

    s1.symmetric_difference(s2) # {1, 4}（交集之外）

    s1.isdisjoint(s2) # False（是否没有交集）
    s1.issubset(s2) # False （s1是否是s2的子集）
    s1.issuperset(s2) # False（s1是否是s2的超集，即s1是否包含s2中的所有元素）


def test1():
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

A = {"python", 123, ("a", "b")}
B = {"python", 234, ("a", "b"), "java"}
C = set("python")
D = "a"

def op():
    print(A | B)
    print(A - B)
    print(A & B)
    print(A ^ B)
    print(A < B)
    print(A <= B)
    print(A > B)
    print(A >= B)

def func():
    print(A.add("d"))
    print(A.discard(123))
    print(A.remove("python"))
    print(A.pop())
    print(A.clear())

    print(B.copy())
    print(len(B))
    print(234 in  B)
    print(6 in  B)

def read():
    for item in B:
        print(item, end="")

    try:
        while True:
            print(B.pop(), end="")
    except:
        pass

def removeDup():
    ls = ["p", "p", "y", "y", 123]
    s = set(ls)
    print(s)
    print(list(s))

def list_op():
    x = set(range(5))
    y = set(range(10))
    print(x)
    print(y)
    print(y - x)
    print(x & y)
    print(x | y)
    print(x ^ y)

if __name__ == "__main__":
    list_op()