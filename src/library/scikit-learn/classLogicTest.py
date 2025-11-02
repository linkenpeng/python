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
    #print(data.head())

    fig1 = plt.figure()
    plt.scatter(data.loc[:, 'Exam1'], data.loc[:, 'Exam2'])
    plt.title('Exam1 and Exam2')
    plt.xlabel('Exam1')
    plt.ylabel('Exam2')
    #plt.show()

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
    #plt.show()

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
    #print(y_test)

    theta1, theta2 = LR.coef_[0][0], LR.coef_[0][1]
    theta0 = LR.intercept_[0]
    X2_new = -(theta0 + theta1 * x1) / theta2
    #print(theta0, theta1, theta2)

    fig3 = plt.figure()
    plt.scatter(data.loc[:, 'Exam1'], data.loc[:, 'Exam2'])
    plt.title('Exam1 and Exam2')
    plt.xlabel('Exam1')
    plt.ylabel('Exam2')
    plt.plot(x1, X2_new)
    #plt.show()

    X1_2 = x1 * x1
    x2_2 = x2 * x2
    X1_x2 = x1 * x2
    x_new = {'x1': x1, 'x2': x2, 'x1_2': X1_2, 'x2_2': x2_2, 'x1_x2': X1_x2}
    x_new = pd.DataFrame(x_new)
    #print(x_new.head())

    x1 = x1.sort_values()
    LR2 = LogisticRegression()
    LR2.fit(x_new, y)
    y_predictions2 = LR2.predict(x_new)
    accuracy2 = accuracy_score(y, y_predictions2)
    print(f"Accuracy: {accuracy2}")
    theta0 = LR2.intercept_
    theta1, theta2, theta3, theta4, theta5 = LR2.coef_[0][0], LR2.coef_[0][1], LR2.coef_[0][2], LR2.coef_[0][3], LR2.coef_[0][4]
    print(theta0, theta1, theta2, theta3, theta4, theta5)
    a = theta0
    b = theta5 * x1 + theta2
    c = theta0 + theta1 * x1 + theta3 * x1 * x1
    x2_new_boudary = (-b + np.sqrt(b * b - 4 * a * c)) / (2 * a)
    print(x2_new_boudary)

    fig4 = plt.figure()
    plt.plot(x1, x2_new_boudary)
    plt.show()



def chipTest():
    file_path = str(Path(__file__).parent.resolve()) + '/test.csv'
    print(file_path)
    data = pd.read_csv(file_path)
    print(data.head())

    fig1 = plt.figure()
    mask = data.loc[:, 'pass'] == 1
    passed = plt.scatter(data.loc[:, 'test1'][mask], data.loc[:, 'test2'][mask])
    failed = plt.scatter(data.loc[:, 'test1'][~mask], data.loc[:, 'test2'][~mask])
    plt.title('Test1 and Test2')
    plt.xlabel('Test1')
    plt.ylabel('Test2')
    plt.legend((passed, failed), ('Passed', 'Failed'))
    plt.show()

    X = data.drop('pass', axis=1)
    y = data.loc[:, 'pass']
    x1 = data.loc[:, 'test1']
    x2 = data.loc[:, 'test2']
    X1_2 = x1 * x1
    x2_2 = x2 * x2
    X1_x2 = x1 * x2
    x_new = {'x1': x1, 'x2': x2, 'x1_2': X1_2, 'x2_2': x2_2, 'x1_x2': X1_x2}
    x_new = pd.DataFrame(x_new)

    x1 = x1.sort_values()
    LR2 = LogisticRegression()
    LR2.fit(x_new, y)
    y_predictions2 = LR2.predict(x_new)
    accuracy2 = accuracy_score(y, y_predictions2)
    print(f"Accuracy: {accuracy2}")
    theta0 = LR2.intercept_
    theta1, theta2, theta3, theta4, theta5 = LR2.coef_[0][0], LR2.coef_[0][1], LR2.coef_[0][2], LR2.coef_[0][3], LR2.coef_[0][4]
    print(theta0, theta1, theta2, theta3, theta4, theta5)
    a = theta4
    b = theta5 * x1 + theta2
    c = theta0 + theta1 * x1 + theta3 * x1 * x1
    x2_new_boudary = (-b + np.sqrt(b * b - 4 * a * c)) / (2 * a)
    x3_new_boudary = (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)
    print(x2_new_boudary)

    x2_new_boudary1 = []
    x2_new_boudary1.append(x2_new_boudary)
    x2_new_boudary2 = []
    x2_new_boudary2.append(x3_new_boudary)
    x1_range = [-0.9 + x/10000 for x in range(190000)] 
    x1_range = np.array(x1_range)

    fig2 = plt.figure()
    mask = data.loc[:, 'pass'] == 1
    passed = plt.scatter(data.loc[:, 'test1'][mask], data.loc[:, 'test2'][mask])
    failed = plt.scatter(data.loc[:, 'test1'][~mask], data.loc[:, 'test2'][~mask])
    plt.plot(x1, x2_new_boudary)
    plt.plot(x1, x3_new_boudary)
    plt.title('Test1 and Test2')
    plt.xlabel('Test1')
    plt.ylabel('Test2')
    plt.legend((passed, failed), ('Passed', 'Failed'))
    plt.show()

if __name__ == '__main__': 
    chipTest()