'''
线性回归
https://scikit-learn.org/
'''
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
from pathlib import Path
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False


def hello():
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

def examPass():
    file_path = str(Path(__file__).parent.resolve()) + '/examdata.csv'
    print(file_path)
    data = pd.read_csv(file_path)
    print(data.head())

    fig1 = plt.figure()
    plt.scatter(data.loc[:, 'Exam1'], data.loc[:, 'Exam2'])
    plt.title('Exam1 and Exam2')
    plt.xlabel('Exam1')
    plt.ylabel('Exam2')
    plt.show()

    fig2 = plt.figure()
    mask = data.loc[:, 'Pass'] == 1
    #passed = plt.scatter(data.loc[mask, 'Exam1'], data.loc[mask, 'Exam2'])
    #failed = plt.scatter(data.loc[~mask, 'Exam1'], data.loc[~mask, 'Exam2'], marker='^')
    passed = plt.scatter(data.loc[:, 'Exam1'][mask], data.loc[:, 'Exam2'][mask])
    failed = plt.scatter(data.loc[:, 'Exam1'][~mask], data.loc[:, 'Exam2'][~mask])
    plt.title('Exam1 and Exam2')
    plt.xlabel('Exam1')
    plt.ylabel('Exam2')
    plt.legend((passed, failed), ('Passed', 'Failed'))
    plt.show()

    X = data.drop('Pass', axis=1)
    y = data.loc[:, 'Pass']
    x1 = data.loc[:, 'Exam1']
    x2 = data.loc[:, 'Exam2']
    LR = LogisticRegression()
    LR.fit(X, y)
    y_predictions = LR.predict(X)
    print(y_predictions)
    accuracy = accuracy_score(y, y_predictions)
    print(f"Accuracy: {accuracy}")

    y_test = LR.predict([[70, 65]])
    print(y_test)

    theta1, theta2 = LR.coef_[0][0], LR.coef_[0][1]
    theta0 = LR.intercept_[0]
    X2_new = -(theta0 + theta1 * x1) / theta2
    print(theta0, theta1, theta2)

    fig3 = plt.figure()
    plt.scatter(data.loc[:, 'Exam1'], data.loc[:, 'Exam2'])
    plt.title('Exam1 and Exam2')
    plt.xlabel('Exam1')
    plt.ylabel('Exam2')
    plt.plot(x1, X2_new)
    plt.show()

if __name__ == '__main__': 
    examPass()