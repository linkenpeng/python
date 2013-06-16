import os;

squared = [x ** 2 for x in range(4)]
for i in squared:
    print(i)
    
print()
sqdEvents = [x ** 2 for x in range(8) if not x % 2]
for i in sqdEvents:
    print(i)
    
rectangle = [(x+1, y+1) for x in range(3) for y in range(5)]
print(rectangle)

f = open('test.txt', 'r')
print("空白字符数目：")
print(len([word for line in f for word in line.split()]))
print(os.stat('test.txt').st_size,'字节')
f.seek(0)
print("字符个数：")
print(sum([len(word) for line in f for word in line.split()]))
f.close()

print('生成器表达式：生成器不真正创建数字列表，\
而是返回一个生成器，这个生成器在每次计算出一个条目后，吧这个条目产生出来')
f = open('test.txt', 'r')
print(sum(len(word) for line in f for word in line.split()))
f.close
rows = [1, 2, 3, 17]
def cols():
    yield 56
    yield 2
    yield 1
    
x_product_pairs = ((i, j) for i in rows for j in cols())
for pair in x_product_pairs:
    print(pair)

print('取最长行')
f = open('test.txt', 'r')
longest = 0
#allLines = f.readlines()
#allLines = [x.strip() for x in f.readlines()]
allLineLens = [len(x.strip()) for x in f]
f.close
#for line in allLines:
#    linelen = len(line.strip())
#    if linelen > longest:
#        longest = linelen

print(max(allLineLens))

f = open('test.txt', 'r')
longest = max(len(x.strip()) for x in f)
f.close
print(longest)

print(max(len(x.strip()) for x in open('test.txt')))









