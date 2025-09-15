#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:19:19 2024
线性规划求解

@author: pengzhenxian
"""

import numpy as np
from scipy.optimize import linprog

# 定义目标函数的系数（利润）
c = [-10, -15]  # 注意：linprog默认是最小化问题，所以我们用负利润

# 定义约束条件的系数矩阵和常数向量
A = np.array([[2, 4],
              [3, 1]])
b = np.array([8, 4])

# 定义变量的界限（非负约束）
x_bounds = (0, None)
y_bounds = (0, None)
bounds = [x_bounds, y_bounds]

# 求解线性规划问题
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# 输出结果
print(f'Optimal value: {result.fun * -1:.2f} (profit)')  # 由于我们用了负利润，所以要乘以-1
print(f'x: {result.x[0]:.0f}, y: {result.x[1]:.0f}')