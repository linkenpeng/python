import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.stats as scs

def normal_list():
    normal_list = range(10000)
    for i in normal_list:
        i**2

def np_list():
    np_list = np.arange(10000)
    np_list**2

    np.arange(10) # 10个，不包括10，步长为1
    np.arange(3, 10, 0.1) # 从3到9，步长为0.1
    # 从2.0到3.0，生成均匀的5个值，不包括终值3.0
    np.linspace(2.0, 3.0, num=5, endpoint=False)
    # 返回一个6×4的随机数组，浮点型
    np.random.randn(6, 4)
    # 指定范围、指定形状的数组，整型
    np.random.randint(3, 7, size=(2, 4))
    # 创建值为0的数组
    np.zeros(6) # 6个浮点0.
    np.zeros((5, 6), dtype=int) # 5×6整型0
    np.ones(4) # 同上
    np.empty(4) # 同上
    # 创建一份和目标结构相同的0值数组
    np.zeros_like(np.arange(6))
    np.ones_like(np.arange(6)) # 同上
    np.empty_like(np.arange(6)) # 同上

    n = np.arange(10)
    n.shape() # 数组的形状，返回值是一个元组
    n.shape = (4, 1) # 改变形状
    a = n.reshape((2,2)) # 改变原数组的形状，创建一个新数组
    n.dtype # 数据类型
    n.ndim # 维度数
    n.size # 元素数
    np.typeDict # np的所有数据类型

def np_data_type():
    np.int64 # 有符号64位整型
    np.float32 # 标准双精度浮点类型
    np.complex # 由128位的浮点数组成的复数类型
    np.bool # bool类型（True或False）
    np.object # Python中的object类型
    np.string # 固定长度的string类型
    np.unicode # 固定长度的unicode类型
    np.NaN # np.float的子类型
    np.nan

def get_day_change():
    stock_cnt = 200
    view_days = 504
    stock_day_change = np.random.standard_normal((stock_cnt, view_days))
    return stock_day_change

def timeDif():
    start = time.perf_counter()
    normal_list()
    end = time.perf_counter()
    print(end - start)

    start = time.perf_counter()
    np_list()
    end = time.perf_counter()
    print(end - start)


def init_np():
    np_list = np.arange(10000)
    # 100个0
    np.zeros(100)
    # 3行2列 全是0
    np.zeros((3, 2))
    # 3行2列 全是1
    np.ones((3, 2))
    # shape: x=2 y=3 z=3 值随机
    np.empty((2, 3, 3))
    np.ones_like(np_list)
    np.zeros_like(np_list)
    np.eye(3)

    # 运行在每一个元素上 NumPy通过广播机制作用域每一个内部元素，是一种并行化执行的思想
    np_list = np.ones(5) * 3
    print(np_list)

    # 整理list * 3
    normal_list = [1, 1, 1, 1, 1] * 3
    print(normal_list)
    print(len(normal_list))

    data = [[1, 2, 3, 4], [5, 6, 7, 8]]
    arr_np = np.array(data)
    print(arr_np)

    random_np = np.linspace(0, 1, 10)
    print(random_np)


def stock():
    stock_day_change = stock_day_change = get_day_change()
    print(stock_day_change.shape)
    # 第一只 第二只， 前5个交易日 涨跌幅
    first = stock_day_change[0:2, 0:5]
    # 倒数第一只 倒数第二只 最后5个交易日的涨跌幅
    end = stock_day_change[-2:, -5:]

    # 交换
    tmp = first.copy()
    # tmp[0][0] = np.nan
    first = end
    end = tmp

    # mask = tmp > 0.5
    # print(mask)
    # print(tmp[mask])

    # tmp[tmp > 0.5] = 1
    # print(tmp)

    # print(tmp[(tmp > 1) | (tmp < -1)])

    # print(np.all(tmp > 0))

    # print(np.any(tmp))

    # print(np.maximum(first, end))
    # print(np.minimum(first, end))

    # print(first.astype(int))
    # print(np.unique(first.astype(int)))

    # print(np.diff(tmp, axis=0))

    print(np.where(tmp > 0.5, 1, 0))
    print(np.where(tmp > 0.5, 1, tmp))
    print(np.where(np.logical_and(tmp > 0.5, tmp < 1), 1, 0))
    print(np.where(np.logical_or(tmp > 0.5, tmp < 1), 1, 0))

    file_path = './gen/stock_day_change'
    np.save(file_path, stock_day_change)

    saved_np = np.load(file_path + '.npy')
    print(saved_np.shape)

    # tem = np.nan_to_num(tmp)
    # print(first.astype(int))
    # print(end.astype(int))
    # print(np.around(first))


def statics_stock():
    stock_day_change = get_day_change()
    stock_day_four = stock_day_change[:4, :4]
    print(stock_day_four)

    print('-' * 60)

    # axis=1 横向
    print('最大涨幅{}'.format(np.max(stock_day_four, axis=1)))
    print('最大跌幅{}'.format(np.min(stock_day_four, axis=1)))
    print('振幅幅度{}'.format(np.std(stock_day_four, axis=1)))
    print('平均涨跌{}'.format(np.mean(stock_day_four, axis=1)))

    print('-' * 60)

    # axis=0 竖向
    print('最大涨幅{}'.format(np.max(stock_day_four, axis=0)))
    print('最大跌幅{}'.format(np.min(stock_day_four, axis=0)))
    print('振幅幅度{}'.format(np.std(stock_day_four, axis=0)))
    print('平均涨跌{}'.format(np.mean(stock_day_four, axis=0)))
    print('最大涨幅股票{}'.format(np.argmax(stock_day_four, axis=0)))
    print('最大跌幅股票{}'.format(np.argmin(stock_day_four, axis=0)))


# 方差
def fc():
    a_investor = np.random.normal(loc=100, scale=50, size=(100, 1))
    b_investor = np.random.normal(loc=100, scale=20, size=(100, 1))
    print('a交易组期望{0:.2f}元，标准差{1:.2f}, 方差{2:.2f}'.format(a_investor.mean(), a_investor.std(), a_investor.var()))
    print('b交易组期望{0:.2f}元，标准差{1:.2f}, 方差{2:.2f}'.format(b_investor.mean(), b_investor.std(), b_investor.var()))
    a_mean = a_investor.mean()
    a_std = a_investor.std()
    plt.plot(a_investor)
    plt.axhline(a_mean + a_std, color='r')
    plt.axhline(a_mean, color = 'y')
    plt.axhline(a_mean - a_std, color='g')

    b_mean = b_investor.mean()
    b_std = b_investor.std()
    plt.plot(b_investor)
    plt.axhline(b_mean + b_std, color='r')
    plt.axhline(b_mean, color = 'y')
    plt.axhline(b_mean - b_std, color='g')
    plt.show()

# 正态分布
def show_buy_lower(stock_ind):
    """
    :param stock_ind: 股票序号
    :return:
    """
    keep_days = 50
    stock_cnt = 200
    view_days = 504
    stock_day_change = np.random.standard_normal((stock_cnt, view_days))
    stock_day_change_test = stock_day_change[:stock_cnt, 0:view_days - keep_days]
    # print(np.sort(np.sum(stock_day_change_test, axis=1)))[:3]
    stock_lower_array = np.argsort(np.sum(stock_day_change_test, axis=1))[:3]
    print(stock_lower_array)

    _, axs = plt.subplots(nrows=1, ncols=2, figsize=(16,5))
    axs[0].plot(np.arange(0, view_days - keep_days),
    stock_day_change_test[stock_ind].cumsum())
    cs_buy = stock_day_change[stock_ind][view_days - keep_days:view_days].cumsum()
    axs[1].plot(np.arange(view_days - keep_days, view_days), cs_buy)
    return cs_buy[-1]



def sin():
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

def zf():
    stock_day_change = get_day_change()
    # 均只期望
    stock_mean = stock_day_change[0].mean()
    # 标准差
    stock_std = stock_day_change[0].std()
    print('股票0 mean均只期望：{:.3f}'.format(stock_mean))
    print('股票0 std振幅标准差：{:.3f}'.format(stock_std))

    # 绘制股票0的直方图
    plt.hist(stock_day_change[0], bins=50, normed=True)
    # linspace从股票0 最小值 -> 最大值生成数据
    fit_linspace = np.linspace(stock_day_change[0].min(), stock_day_change[0].max())
    # 概率密度函数，有均值，方差来描述曲线
    pdf = scs.norm(stock_mean, stock_std).pdf(fit_linspace)

    plt.plot(fit_linspace, pdf, lw=2, c='r')
    plt.show()
