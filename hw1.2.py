import numpy as np
import matplotlib.pyplot as plt # need to install matplotlib


# time t = 1 --> Jan 26
# t = 2 --> Jan 27. etc.

# Jan 26, 2026 -> ~$5,015
# Jan 27, 2026 -> ~$5,190
# Jan 28, 2026 -> ~$5,400
# Jan 29, 2026 -> ~$5,396
# Jan 30, 2026 -> ~$4,865

# P_4(1) = 5015
# P_4(2) = 5190
# P_4(3) = 5400
# P_4(4) = 5396
# P_4(5) = 4865

# (1) Interpolate the data in a polynomial P_4(t) and compute P_4(t = 6) using your P_4(t).

t_values = np.array([1,2,3,4,5])
prices = np.array([5015,5190,5400,5396,4865]) # the 'y' value, and rightmost matrix on the page 6 of topic 2 notes


def P_4(t):
    func = 0.0
    for i in range(prices.size):
        coefficient = 1
        for j in range(prices.size):
            if j != i:
                coefficient *= (t - t_values[j]) / (t_values[i] - t_values[j])
        func += prices[i] * coefficient
    return func


x_arr = np.linspace(1.0, 6.0, 100)
plt.scatter(t_values, prices, color='blue', label='Data')
plt.plot(x_arr, P_4(x_arr), color='red', label=r'$P_4(t)$')
plt.xlabel('t (days)')
plt.ylabel('Gold spot price ($)')
plt.legend()
plt.savefig('./P4interpolate.png', dpi=600)

print("P_4(6) = " + str(P_4(6)))



# (2) Make a quadratic fit of the data Q_2(t) = a_0 + a_1t + a_2t^2 and compute Q_2(t = 6) using Q_2(t).

X = np.zeros((prices.size, 3))
# establish matrix of data
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        X[i,j] += t_values[i]**j


## implement OLS
a = np.matmul(np.matmul(np.linalg.inv(np.matmul( X.transpose(), X )), X.transpose()), prices)
def Q_2(x):
    return (a[0] + a[1]*x + a[2]*x**2)

plt.figure()
plt.scatter(t_values, prices, color='blue', label='Data')
plt.plot(x_arr, Q_2(x_arr), color='red', label=r'$Q_2(t)$')
plt.xlabel('t (days)')
plt.ylabel('Gold spot price ($)')
plt.legend()
plt.savefig('./Q2fit.png', dpi=600)

print("Q_2(6) = " + str(Q_2(6)))





