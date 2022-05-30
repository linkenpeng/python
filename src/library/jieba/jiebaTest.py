import jieba

tx = "中国是一个伟大的国家"
tx2 = "中华人民共和国是伟大的"
tx3 = "蟒蛇语言是一种新的语言"

list = jieba.lcut(tx)
print(list)

print(jieba.lcut(tx3))

list = jieba.lcut(tx, cut_all=True)
print(list)

list = jieba.lcut_for_search(tx2)
print(list)

jieba.add_word("蟒蛇语言")
print(jieba.lcut(tx3))



