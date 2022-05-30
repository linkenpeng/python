import wordcloud
import jieba

def genEnglish():
    txt = "life is short, you need python"
    w = wordcloud.WordCloud(background_color="white")
    w.generate(txt)
    w.to_file("pywordcloud.png")

def genChinese():
    txt = "程序设计语言是计算机能够理解和识别用户" \
          "操作意图的一种交互体系，它安装特定规则组织计算机指令,使计算机能够自动进行各种运算处理。"
    w = wordcloud.WordCloud(background_color="white", font_path="/System/Library/Fonts/PingFang.ttc", width=1000, height=700)
    w.generate(" ".join(jieba.lcut(txt)))
    w.to_file("pywordcloud.png")

genChinese()