import numpy as np
import pandas as pd


class LogisticRegression:

    def __init__(self, max_iterations=1000):
        self.weights = None
        self.bias = None
        self.__learningRate = 0.1
        self.max_iterations = max_iterations

    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def __compute_gradients(self, X, y):
        m = X.shape[0]
        z = np.dot(X, self.weights) + self.bias
        y_pred = self.__sigmoid(z)
        dw = (1 / m) * np.dot(X.T, (y_pred - y))
        db = (1 / m) * np.sum(y_pred - y)
        return dw, db

    def fit(self, X, y):
        n = X.shape[1]
        self.weights = np.random.rand(n, 1)
        self.bias = np.random.rand(1)

        for i in range(1, self.max_iterations + 1):
            dw, db = self.__compute_gradients(X, y)
            self.weights -= self.__learningRate * dw
            self.bias -= self.__learningRate * db

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        Y = (y_pred >= 0.5).astype(int)
        return Y

    def score(self, X, y):
        y_pred = np.dot(X, self.weights) + self.bias
        Y = y_pred >= 0.5
        accuracy = np.mean(Y == y) * 100
        return accuracy

