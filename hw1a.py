import numpy as np
import matplotlib.pyplot as plt

# Jan 16, 2026 -> $410.50
# Jan 20, 2026 -> $415.80
# Jan 21, 2026 -> $422.30
# Jan 22, 2026 -> $428.15
# Jan 23, 2026 -> $432.60
# Jan 26, 2026 -> $435.20
# Jan 27, 2026 -> $430.90
# Jan 28, 2026 -> $431.46
# Jan 29, 2026 -> $416.56
# Jan 30, 2026 -> $430.41

# Make a cubic fit of the 10-session Tesla stock

# A^TAc = A^Ty

# cubic goes up to 3


t_arr = np.array([16.0, 20.0, 21.0, 22.0, 23.0, 26.0, 27.0, 28.0, 29.0, 30.0]) - 15 # this is b/c some data points have multiple days between
## set the first day as t=1
y_arr = np.array([410.5, 415.8, 422.3, 428.15, 432.6, 435.2, 430.9, 431.46, 416.56, 430.41])

X = np.zeros((y_arr.size, 4))

#establish the matrix
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        X[i,j] += t_arr[i] ** j

# implement OLS

a = np.matmul(np.matmul(np.linalg.inv(np.matmul(X.transpose(), X)), X.transpose()), y_arr)

def Q3(x):
    return (a[0] + a[1]*x + a[2]*x**2 + a[3]*x**3)

x_arr = np.linspace(1.0, 16.0, 100)

plt.ylim(390, 460) # to match providfed figure
plt.scatter(t_arr, y_arr, color='blue', label='Data')
plt.plot(x_arr, Q3(x_arr), color='red', label=r'$Q_3(t)$')
plt.xlabel('t (days)')
plt.ylabel('Gold spot price ($)')
plt.legend()
plt.savefig('./Q3fit.png', dpi=600)






