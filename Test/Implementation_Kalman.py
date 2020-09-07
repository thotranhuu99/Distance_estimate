import numpy as np
from filters import KalmanFixedFilter
import cv2

y = np.array([0.00552486, 0.00537634, 0.00471698, 0.00478469, 0.00546448, 0.00578035,
              0.00526316, 0.00699301, 0.00588235, 0.0078125,  0.00645161, 0.00729927,
              0.0075188,  0.008,      0.00740741, 0.00684932, 0.00862069, 0.00833333,
              0.00909091, 0.00854701, 0.00990099, 0.00854701, 0.00900901, 0.00892857,
              0.00900901, 0.00840336, 0.0125,     0.01176471, 0.01041667, 0.01234568,
              0.01204819, 0.01190476, 0.01086957, 0.01204819, 0.01282051, 0.01388889,
              0.01333333, 0.01351351, 0.01428571])
x = np.array([[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
               38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57,
               58, 59, 60]])
x_hat = np.zeros(len(y))
d_hat = np.zeros(len(y))

Filter_1 = KalmanFixedFilter(y[0], 1, 1 / 4132.45, 1, 4132.45, 0)
x_hat[0] = y[0] * 4132.45
for i in range(1, len(y), 1):
    d_hat[i-1], x_hat[i] = Filter_1.calculate(y[i])
print("Distance: {}(cm)".format(x_hat))
print("Control signal: {}".format(d_hat))
error = np.subtract(x, x_hat+2.44)
print("Error: {}\nAverage error:{}\nAverage abs error:{}".format(error, np.sum(error)/len(y), np.sum(np.abs(error))/len(y)))
"""np.sqrt(np.sum(error**2)/len(y)))"""
