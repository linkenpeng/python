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