import numpy as np
import matplotlib.pyplot as plt

plt.figure()
x_values, y_values = np.meshgrid(np.arange(1, 4, 1), np.arange(1, 4, 1))
c = np.c_[x_values.ravel(), y_values.ravel()]
print(c)
pred = np.array([[ 0  ,0 , 0],
 [ 0 , 1,  1],
 [ 0  ,1  ,1]])

pred.shape = x_values.shape
plt.pcolormesh(x_values, y_values, pred, cmap=plt.cm.Paired)
plt.show()


