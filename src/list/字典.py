
dc = {"a":1, "b":2, "c": 3, "d":4}

print(dc)
print(dc["a"])
print(type(dc))

del dc['a'];

print(dc)

print("b" in dc)

print(dc.keys())

print(dc.values())

print(dc.items())

print(dc.get("a", 11))

print(dc.pop("b", 22))

print(dc.popitem())

print(len(dc))

dc.clear()

print(dc)