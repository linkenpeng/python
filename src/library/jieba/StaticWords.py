import jieba
import wordcloud
import imageio
import sys

def getText(file):
    txt = open(file, "r", encoding="utf-8").read()
    txt = txt.lower()
    for ch in '|"#$%()*+,-./:;<=>?@[\\]^_~{|}''':
        txt.replace(ch, " ")
    return txt

def dealHamlet():
    # https://python123.io/resources/pye/hamlet.txt
    hamletTxt = getText("hamlet.txt")
    words = hamletTxt.split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))

def dealThreeKingDoms():
    # https://python123.io/resources/pye/threekingdoms.txt
    content = getText("threekingsdoms.txt")
    excludes = {"将军", "却说", "荆州", "二人", "不可", "不能",
                "如此","商议","如何","主公","军士","左右","军马",
                "引兵","操场","次日","大喜","天下","东吴",
                "于是","今日","不敢","魏兵","一人",
                "都督","人马","陛下","不知","汉中","只见",
                "众将","后主","蜀兵","上马","大叫","太守","此人","夫人","先主"}
    words = jieba.lcut(content)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        elif word == "诸葛亮" or word == "孔明曰":
            rword = "孔明"
        elif word == "关公" or word == "云长":
            rword = "关羽"
        elif word == "玄德" or word == "玄德曰":
            rword = "刘备"
        elif word == "孟德" or word == "丞相":
            rword = "曹操"
        else:
            rword = word
        counts[rword] = counts.get(rword, 0) + 1

    for word in excludes:
        del counts[word]

    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    top_list = []
    for i in range(12):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))
        top_list.append(word)

    w = wordcloud.WordCloud(background_color="white",
                            font_path=get_font_path(),
                            width=1000, height=700)
    w.generate(" ".join(top_list))
    w.to_file("threekongsdoms.png")

def makeWordCloud(fileName, outImage, excludes):
    print("="*20 + fileName + "="*20)
    content = getText(fileName + ".txt")
    words = jieba.lcut(content)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            rword = word
        counts[rword] = counts.get(rword, 0) + 1

    if excludes:
        for word in excludes:
            del counts[word]

    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    top_list = []
    for i in range(50):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))
        top_list.append(word)

    if(outImage):
        mask = imageio.imread_v2("fivestar.jpeg")
        w = wordcloud.WordCloud(background_color="white",
                                font_path=get_font_path(),
                                width=1000, height=700, max_words=15)
        w.generate(" ".join(top_list))
        w.to_file(fileName + ".png")

'''
win32：表示 windows 系统
linux：表示 linux 系统
cygwin：表示 Windows/Cygwin 系统
darwin：表示 macOS 系统
'''
def get_font_path():
    font_path = "/System/Library/Fonts/PingFang.ttc"
    if sys.platform == "win32":
        font_path = "C:/Windows/Fonts/STKAITI.TTF"
    return font_path

makeWordCloud("项目复盘", True, {"一些", "mmp", "积分","资格", "部分", "方式"})
makeWordCloud("风险管理", True, {"同学","迁移", "原来"})
