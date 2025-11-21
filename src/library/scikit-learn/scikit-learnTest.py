from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs
from sklearn.datasets import load_digits
from sklearn.datasets import load_iris
from sklearn.datasets import make_regression

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False


# 1. 线性回归 (Linear Regression)
def linear_regression():
    # 1. 生成模拟数据
    X = np.random.rand(100, 1) * 10  # 特征
    y = 2 * X + 3 + np.random.randn(100, 1) * 2  # 标签

    # 2. 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. 创建并训练模型
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 4. 预测
    y_pred = model.predict(X_test)

    # 5. 评估
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"系数: {model.coef_[0][0]:.2f}")
    print(f"截距: {model.intercept_[0]:.2f}")
    print(f"均方误差: {mse:.2f}")
    print(f"R² 分数: {r2:.2f}")

# 2. 逻辑回归 (Logistic Regression)
def logistic_regression():
    # 1. 生成模拟数据
    X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=42)

    # 2. 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. 创建并训练模型
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # 4. 预测
    y_pred = model.predict(X_test)

    # 5. 评估
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

    print(f"准确率: {accuracy:.2f}")
    print("混淆矩阵:")
    print(conf_matrix)
    print("分类报告:")
    print(class_report)


# 决策树 (Decision Tree)
def decision_tree():
    # 1. 加载数据
    data = load_iris()
    X, y = data.data, data.target

    # 2. 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. 创建并训练模型
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X_train, y_train)

    # 4. 预测
    y_pred = model.predict(X_test)

    # 5. 评估
    accuracy = accuracy_score(y_test, y_pred)
    print(f"准确率: {accuracy:.2f}")

    # 6. 可视化决策树
    plt.figure(figsize=(10, 6))
    plot_tree(model, filled=True, feature_names=data.feature_names, class_names=data.target_names)
    plt.show()

# 随机森林 (Random Forest)
def random_forest():
    # 1. 生成模拟数据
    X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)

    # 2. 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. 创建并训练模型
    model = RandomForestRegressor(n_estimators=100, max_depth=3, random_state=42)
    model.fit(X_train, y_train)

    # 4. 预测
    y_pred = model.predict(X_test)

    # 5. 评估
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"平均绝对误差: {mae:.2f}")
    print(f"R² 分数: {r2:.2f}")

    # 6. 特征重要性
    feature_importance = model.feature_importances_
    print("特征重要性:", feature_importance)

# 支持向量机 (SVM)
def svm():
    # 1. 生成模拟数据
    X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=42)

    # 2. 数据标准化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 3. 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 4. 创建并训练模型
    model = SVC(kernel='rbf', C=1.0, gamma='scale')
    model.fit(X_train, y_train)

    # 5. 预测
    y_pred = model.predict(X_test)

    # 6. 评估
    accuracy = accuracy_score(y_test, y_pred)
    print(f"准确率: {accuracy:.2f}")

# 6. K 近邻 (KNN)
def knn():
    # 1. 加载数据
    data = load_iris()
    X, y = data.data, data.target

    # 2. 数据标准化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 3. 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 4. 创建并训练模型
    model = KNeighborsClassifier(n_neighbors=5, weights='distance')
    model.fit(X_train, y_train)

    # 5. 预测
    y_pred = model.predict(X_test)

    # 6. 评估
    accuracy = accuracy_score(y_test, y_pred)
    print(f"准确率: {accuracy:.2f}")

# 7. 主成分分析 (PCA)
def pca():
    
    # 1. 加载数据
    data = load_digits()
    X, y = data.data, data.target

    # 2. 数据标准化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 3. 创建并训练模型
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X_scaled)

    # 4. 可视化结果
    plt.figure(figsize=(10, 6))
    for i in range(10):
        plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], label=str(i), alpha=0.7)
    plt.xlabel('主成分 1')
    plt.ylabel('主成分 2')
    plt.legend()
    plt.title('PCA 降维结果')
    plt.show()

    # 5. 解释方差比例
    print(f"主成分 1 解释方差比例: {pca.explained_variance_ratio_[0]:.2f}")
    print(f"主成分 2 解释方差比例: {pca.explained_variance_ratio_[1]:.2f}")
    print(f"总解释方差比例: {sum(pca.explained_variance_ratio_):.2f}")

# 8. K 均值聚类 (K-Means)
def kmeans():
    # 1. 生成模拟数据
    X, y = make_blobs(n_samples=100, n_features=2, centers=3, random_state=42)

    # 2. 创建并训练模型
    kmeans = KMeans(n_clusters=3, random_state=42)
    y_pred = kmeans.fit_predict(X)

    # 3. 可视化结果
    plt.figure(figsize=(10, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis', alpha=0.7)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X')
    plt.xlabel('特征 1')
    plt.ylabel('特征 2')
    plt.title('K-Means 聚类结果')
    plt.show()

    # 4. 评估聚类效果（轮廓系数）
    from sklearn.metrics import silhouette_score
    silhouette_avg = silhouette_score(X, y_pred)
    print(f"轮廓系数: {silhouette_avg:.2f}")

# 9. 梯度提升 (Gradient Boosting)
def gradient_boosting():
    # 1. 生成模拟数据
    X, y = make_classification(n_samples=100, n_features=5, n_informative=3, random_state=42)

    # 2. 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. 创建并训练模型
    model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    model.fit(X_train, y_train)

    # 4. 预测
    y_pred = model.predict(X_test)

    # 5. 评估
    accuracy = accuracy_score(y_test, y_pred)
    print(f"准确率: {accuracy:.2f}")

    # 6. 特征重要性
    feature_importance = model.feature_importances_
    print("特征重要性:", feature_importance)

# 10. 朴素贝叶斯 (Naive Bayes)
def naive_bayes():
    # 1. 加载数据
    data = load_iris()
    X, y = data.data, data.target

    # 2. 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. 创建并训练模型
    model = GaussianNB()
    model.fit(X_train, y_train)

    # 4. 预测
    y_pred = model.predict(X_test)

    # 5. 评估
    accuracy = accuracy_score(y_test, y_pred)
    print(f"准确率: {accuracy:.2f}")

if __name__ == '__main__': 
    naive_bayes()