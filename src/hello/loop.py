# 循环

for i in range (1, 6):
    print(i)

for s in "python":
    if s == "t":
        continue
    print(s, end=",")

list = [123, "a", "b", True]

# break 跳出当次最内层循环
for item in list:
    if item == "b":
        break
    print(item)

s = "python"
while s != "":
    for ss in s:
        print(ss)
    s = s[:-1]