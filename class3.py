import numpy as np
import matplotlib.pyplot as plt
def sigmoid (X,a,b):
    t=a*X+b
    return 1/(1+np.exp(-t))
a,b=0,0
learning_rate = 0.1

n=200
X = np.sort(np.random.randn(n))
y = np.zeros(n)
y[(X>0)]=1
y_pred = np.zeros(100)
y_pred[y_pred >= 0.5]= 1


for i in range(1000):
    p_pred = sigmoid(X,a,b)
    grad_a = (1/n) *np.sum((p_pred-y)*X)
    grad_b = (1/n)*np.sum(p_pred-y)
    a = a-learning_rate*grad_a
    b= b - learning_rate*grad_b

accuracy = np.mean(y_pred==y)
print("accuracy",accuracy)
plt.scatter(X,y)
plt.plot(X,sigmoid(X,a,b),"r")
plt.show()