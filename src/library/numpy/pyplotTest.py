import matplotlib.pyplot as plt
import matplotlib
import numpy as np

'''
https://www.runoob.com/matplotlib/matplotlib-tutorial.html

# 画单条线
plot([x], y, [fmt], *, data=None, **kwargs)

如果我们不指定 x 轴上的点，则 x 会根据 y 的值来设置为 0, 1, 2, 3..N-1。

# 画多条线
plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)

参数说明：

x, y：点或线的节点，x 为 x 轴数据，y 为 y 轴数据，数据可以列表或数组。

fmt：可选，定义基本格式（如颜色、标记和线条样式）。

**kwargs：可选，用在二维平面图上，设置指定属性，如标签，线的宽度等。

颜色字符：'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，
'c' 青绿色，'#008000' RGB 颜色符串。多条曲线不指定颜色时，会自动选择不同颜色。

线型参数：'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线。

标记字符：'.' 点标记，',' 像素标记(极小点)，'o' 实心圈标记，'v' 倒三角标记，
'^' 上三角标记，'>' 右三角标记，'<' 左三角标记...等等。

标记大小与颜色
我们可以自定义标记的大小与颜色，使用的参数分别是：
markersize，简写为 ms：定义标记的大小。
markerfacecolor，简写为 mfc：定义标记内部的颜色。
markeredgecolor，简写为 mec：定义标记边框的颜色。

'''

def sin():
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

    x = np.arange(0,4*np.pi,0.1)   # start,stop,step
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x,y,x,z)
    plt.show()

def xy():
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 100])
    plt.plot(xpoints, ypoints, 'm')
    plt.show()

def marker():
    ypoints = np.array([1,3,4,5,8,9,6,1,3,4,5,2,4])

    plt.plot(ypoints, marker = 'o')
    plt.show()

    ypoints = np.array([6, 2, 13, 10])

    plt.plot(ypoints, marker = 'o', ms = 20)
    plt.show()

    plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
    plt.show()

    plt.plot(ypoints, 'o:r')
    plt.show()

    plt.plot(ypoints, linestyle = 'dotted')
    plt.show()

    plt.plot(ypoints, ls = '-.')
    plt.show()

    plt.plot(ypoints, c = '#8FBC8F')
    plt.show()

    plt.plot(ypoints, linewidth = '12.5')
    plt.show()

    y1 = np.array([3, 7, 5, 9])
    y2 = np.array([6, 2, 13, 10])

    plt.plot(y1)
    plt.plot(y2)

    plt.show()

    x1 = np.array([0, 1, 2, 3])
    y1 = np.array([3, 7, 5, 9])
    x2 = np.array([0, 1, 2, 3])
    y2 = np.array([6, 2, 13, 10])

    plt.plot(x1, y1, x2, y2)
    plt.show()


def label():
    # fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径，size 参数设置字体大小
    zhfont1 = matplotlib.font_manager.FontProperties(fname="/Users/pengzhenxian/project/font/SourceHanSansSC-Bold.otf", size=18)
    font1 = {'color':'blue','size':20}
    font2 = {'color':'darkred','size':15}
    x = np.arange(1, 11)
    y = 2 * x + 5

    # fontdict 可以使用 css 来设置字体样式
    plt.title("标题", fontproperties=zhfont1, fontdict=font1, loc="left")

    # fontproperties 设置中文显示，fontsize 设置字体大小
    plt.xlabel("x 轴", fontproperties=zhfont1, loc="left")
    plt.ylabel("y 轴", fontproperties=zhfont1, loc="top")
    plt.plot(x, y)
    plt.show()

def grid():
    x = np.array([1, 2, 3, 4])
    y = np.array([1, 4, 9, 16])
    plt.title("RUNOOB grid() Test")
    plt.xlabel("x - label")
    plt.ylabel("y - label")
    plt.plot(x, y)
    '''
    axis: x, y, both
    color：'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串。
    linestyle：'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线。
    linewidth：设置线的宽度，可以设置一个数字。
    '''
    plt.grid(axis='both', color = 'r', linestyle = '--', linewidth = 0.5)
    plt.show()

def tow_line():
    '''
    matplotlib.pyplot.subplots(nrows=1, ncols=1, *, sharex=False,
    sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
    nrows：默认为 1，设置图表的行数。
    ncols：默认为 1，设置图表的列数。
    sharex、sharey：设置 x、y 轴是否共享属性，默认为 false，可设置为 'none'、'all'、'row' 或 'col'。 False 或 none 每个子图的 x 轴或 y 轴都是独立的，True 或 'all'：所有子图共享 x 轴或 y 轴，'row' 设置每个子图行共享一个 x 轴或 y 轴，'col'：设置每个子图列共享一个 x 轴或 y 轴。
    squeeze：布尔值，默认为 True，表示额外的维度从返回的 Axes(轴)对象中挤出，对于 N*1 或 1*N 个子图，返回一个 1 维数组，对于 N*M，N>1 和 M>1 返回一个 2 维数组。如果设置为 False，则不进行挤压操作，返回一个元素为 Axes 实例的2维数组，即使它最终是1x1。
    subplot_kw：可选，字典类型。把字典的关键字传递给 add_subplot() 来创建每个子图。
    gridspec_kw：可选，字典类型。把字典的关键字传递给 GridSpec 构造函数创建子图放在网格里(grid)。
    **fig_kw：把详细的关键字参数传给 figure() 函数。
    '''
    #plot 1:
    x = np.array([0, 6])
    y = np.array([0, 100])

    plt.subplot(2, 2, 1)
    plt.plot(x,y)
    plt.title("plot 1")

    #plot 2:
    x = np.array([1, 2, 3, 4])
    y = np.array([1, 4, 9, 16])

    plt.subplot(2, 2, 2)
    plt.plot(x,y)
    plt.title("plot 2")

    #plot 3:
    x = np.array([1, 2, 3, 4])
    y = np.array([3, 5, 7, 9])

    plt.subplot(2, 2, 3)
    plt.plot(x,y)
    plt.title("plot 3")

    #plot 4:
    x = np.array([1, 2, 3, 4])
    y = np.array([4, 5, 6, 7])

    plt.subplot(2, 2, 4)
    plt.plot(x,y)
    plt.title("plot 4")

    plt.suptitle("RUNOOB subplot Test")
    plt.show()

def multi_line():
    # 创建一些测试数据 -- 图1
    x = np.linspace(0, 2*np.pi, 400)
    y = np.sin(x**2)

    # 创建一个画像和子图 -- 图2
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Simple plot')

    # 创建两个子图 -- 图3
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.plot(x, y)
    ax1.set_title('Sharing Y axis')
    ax2.scatter(x, y)

    # 创建四个子图 -- 图4
    fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
    axs[0, 0].plot(x, y)
    axs[1, 1].scatter(x, y)

    # 共享 x 轴
    plt.subplots(2, 2, sharex='col')

    # 共享 y 轴
    plt.subplots(2, 2, sharey='row')

    # 共享 x 轴和 y 轴
    plt.subplots(2, 2, sharex='all', sharey='all')

    # 这个也是共享 x 轴和 y 轴
    plt.subplots(2, 2, sharex=True, sharey=True)

    # 创建10 张图，已经存在的则删除
    fig, ax = plt.subplots(num=10, clear=True)

    plt.show()

'''
matplotlib.pyplot.scatter(x, y, s=None, c=None, 
marker=None, cmap=None, norm=None, vmin=None, 
vmax=None, alpha=None, linewidths=None, *, 
edgecolors=None, plotnonfinite=False, data=None, **kwargs)

参数说明：
x，y：长度相同的数组，也就是我们即将绘制散点图的数据点，输入数据。
s：点的大小，默认 20，也可以是个数组，数组每个参数为对应点的大小。
c：点的颜色，默认蓝色 'b'，也可以是个 RGB 或 RGBA 二维行数组。
marker：点的样式，默认小圆圈 'o'。
cmap：Colormap，默认 None，标量或者是一个 colormap 的名字，只有 c 是一个浮点数数组的时才使用。如果没有申明就是 image.cmap。
norm：Normalize，默认 None，数据亮度在 0-1 之间，只有 c 是一个浮点数的数组的时才使用。
vmin，vmax：：亮度设置，在 norm 参数存在时会忽略。
alpha：：透明度设置，0-1 之间，默认 None，即不透明。
linewidths：：标记点的长度。
edgecolors：：颜色或颜色序列，默认为 'face'，可选值有 'face', 'none', None。
plotnonfinite：：布尔值，设置是否使用非限定的 c ( inf, -inf 或 nan) 绘制点。
**kwargs：：其他参数。
'''
def scatter():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
    sizes = np.array([20,50,100,200,500,1000,60,90])
    colors = np.array(["red","green","black","orange","purple","beige","cyan","magenta"])
    plt.scatter(x, y, s=sizes, c=colors)
    plt.show()

def tow_scatter():
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    plt.scatter(x, y, color = 'hotpink')

    x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
    y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
    plt.scatter(x, y, color = '#88c999')

    plt.show()

def random_scatter():
    # 随机数生成器的种子
    np.random.seed(19680801)
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
    plt.scatter(x, y, s=area, c=colors, alpha=0.5) # 设置颜色及透明度
    plt.title("RUNOOB Scatter Test") # 设置标题
    plt.show()

def color_bar():
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    # afmhot_r
    plt.scatter(x, y, c=colors, cmap='viridis')
    plt.colorbar()
    plt.show()

'''
柱状图
matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
参数说明：
x：浮点型数组，柱形图的 x 轴数据。
height：浮点型数组，柱形图的高度。
width：浮点型数组，柱形图的宽度。
bottom：浮点型数组，底座的 y 坐标，默认 0。
align：柱形图与 x 坐标的对齐方式，'center' 以 x 位置为中心，这是默认值。 
'edge'：将柱形图的左边缘与 x 位置对齐。要对齐右边缘的条形，可以传递负数的宽度值及 align='edge'。
**kwargs：：其他参数。
'''
def bar():
    x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
    y = np.array([12, 22, 6, 18])
    colors = ["#4CAF50","red","hotpink","#556B2F"]
    # plt.bar(x,y, width=0.1, color=colors)
    plt.barh(x,y, color=colors, height=0.1)
    plt.show()


'''
Matplotlib 饼图
matplotlib.pyplot.pie(x, explode=None, labels=None, 
colors=None, autopct=None, pctdistance=0.6, 
shadow=False, labeldistance=1.1, startangle=0, 
radius=1, counterclock=True, wedgeprops=None, 
textprops=None, center=0, 0, frame=False, 
rotatelabels=False, *, normalize=None, data=None)[source]

参数说明：

x：浮点型数组，表示每个扇形的面积。
explode：数组，表示各个扇形之间的间隔，默认值为0。
labels：列表，各个扇形的标签，默认值为 None。
colors：数组，表示各个扇形的颜色，默认值为 None。
autopct：设置饼图内各个扇形百分比显示格式，%d%% 整数百分比，%0.1f 一位小数， %0.1f%% 一位小数百分比， %0.2f%% 两位小数百分比。
labeldistance：标签标记的绘制位置，相对于半径的比例，默认值为 1.1，如 <1则绘制在饼图内侧。
pctdistance：：类似于 labeldistance，指定 autopct 的位置刻度，默认值为 0.6。
shadow：：布尔值 True 或 False，设置饼图的阴影，默认为 False，不设置阴影。
radius：：设置饼图的半径，默认为 1。
startangle：：起始绘制饼图的角度，默认为从 x 轴正方向逆时针画起，如设定 =90 则从 y 轴正方向画起。
counterclock：布尔值，设置指针方向，默认为 True，即逆时针，False 为顺时针。
wedgeprops ：字典类型，默认值 None。参数字典传递给 wedge 对象用来画一个饼图。例如：wedgeprops={'linewidth':5} 设置 wedge 线宽为5。
textprops ：字典类型，默认值为：None。传递给 text 对象的字典参数，用于设置标签（labels）和比例文字的格式。
center ：浮点类型的列表，默认值：(0,0)。用于设置图标中心位置。
frame ：布尔类型，默认值：False。如果是 True，绘制带有表的轴框架。
rotatelabels ：布尔类型，默认为 False。如果为 True，旋转每个 label 到指定的角度。
'''
def pie():
    y = np.array([35, 25, 25, 15])
    plt.pie(y,
            labels=['A','B','C','D'], # 设置饼图标签
            colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # 设置饼图颜色
            explode=(0, 0.2, 0, 0), # 第二部分突出显示，值越大，距离中心越远
            autopct='%.2f%%', # 格式化输出百分比
            )
    plt.title("RUNOOB Pie Test")
    plt.show()

pie()