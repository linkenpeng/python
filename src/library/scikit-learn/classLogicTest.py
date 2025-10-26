'''
线性回归
https://scikit-learn.org/
'''
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

X1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
X2 = np.array([7,9,11,13,15,17,19,21,23,25])
LR = LogisticRegression()
LR.fit(X1, X2)

theta1, theta2 = LR.coef_[0][0], LR.coef_[0][1]
theta0 = LR.intercept_[0]

predictions_y_new = LR.predict(X1)
print(predictions_y_new)

y_predictions = LR.predict(X1)
accuracy = accuracy_score(predictions_y_new, y_predictions)
print(f"Accuracy: {accuracy}")

y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
mask = y == 1
plt.plot(X1, X2)
passed = plt.scatter(X1[mask], X2[mask])
failed = plt.scatter(X1[~mask], X2[~mask], marker='^')

plt.show()