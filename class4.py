def func(X,a,b):
    return a * X +b

import numpy as np
import matplotlib.pyplot as plt
scale_data = 10
scale_noise = 5
X = np.random.rand(20) * scale_data
y_noise = np.random.rand(20) * scale_noise
y_ideal = func(X, 5, 2)
y_real = y_ideal + y_noise

X_mean = np.mean(X)
y_mean = np.mean(y_real)
a = np.sum((X-X_mean)*(y_real-y_mean))/np.sum((X-X_mean)**2)
b = y_mean - a *X_mean
y_pred = a * X + b

a_init = 0
b_init = 0
a = a_init
b = b_init
learning_rate = 0.001
n = len(X)
a_arr = np.zeros(10000+1)
b_arr = np.zeros(10000+1)
a_arr[0]=a
b_arr[0]=b
def loss_func (y,y_pred):
    return np.sum((y - y_pred)**2)/len(y)
for i in range(10000):
    y_pred = func(X,a,b)
    loss = loss_func(y_real,y_pred)
    grad_a = -(2/n) *np.sum((y_real-y_pred)*X)
    grad_b = -(2/n)*np.sum(y_real-y_pred)
    a = a - learning_rate * grad_a
    b = b - learning_rate * grad_b
print("a_real =5",a)
print("breal =2",b)
#plt.show()
#plt.plot(b_arr)
#plt.show()
plt.scatter(X,y_real)
plt.scatter(X,y_pred)
plt.plot(X,y_pred)
plt.show()