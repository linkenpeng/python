
def unicode():
    for i in range(12):
        print(chr(9800 + i), end="")

    print(ord("Ø"))


def basicFuction():
    a = "123abc我是"
    b = 982
    c = "abD G"

    print(len(a))
    print(str(b))
    print(hex(10))
    print(oct(8))
    print(ord("a"))
    print(chr(100))
    print(c.lower())
    print(c.upper())
    print(c.split())
    print(c.replace("D", "F"))
    print(c.center(10, '='))
    print(c.strip(" "))
    print(c.join(a))
    print(c.format("{:.2f}"))

basicFuction()