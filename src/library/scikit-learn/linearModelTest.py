'''
线性回归
https://scikit-learn.org/
'''
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 原始数据
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([7,9,11,13,15,17,19,21,23,25])

# 预测线性模型中a, b的值
lr_model = LinearRegression()
lr_model.fit(x, y)

a = lr_model.coef_ 
b = lr_model.intercept_

print(a)
print(b)   

# 预测新数据
x_new = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]).reshape(-1, 1)
predictions_y_new = lr_model.predict(x_new)
print(predictions_y_new)

# 模型评估 - 使用训练数据进行评估
predictions_y_train = lr_model.predict(x)
MSE = mean_squared_error(y, predictions_y_train)
R2 = r2_score(y, predictions_y_train)   
print(f"MSE: {MSE}")
print(f"R2: {R2}")

# 绘制原始数据和预测结果
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='原始数据')
plt.plot(x, predictions_y_train, color='red', label='拟合线')
plt.scatter(x_new, predictions_y_new, color='green', label='预测数据')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('线性回归模型')
plt.show()