import numpy as np

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

A = np.column_stack([np.ones(len(t_values)), t_values, t_values**2, t_values**3, t_values**4])
# the above is the matrix with the different powers of x's from page 6 of the topic 2 noes (the leftmost matrix)

coefficients = np.linalg.solve(A, prices)

def P4(t):
    return coefficients[0] + coefficients[1]*t + coefficients[2]*(t**2) + coefficients[3]*(t**3) + coefficients[4]*(t**4) 


print("P_4(t) = " + str(P4))

print("P_4(6) = " + str(P4(6)))





# (2) Make a quadratic fit of the data Q_2(t) = a_0 + a_1t + a_2t^2 and compute Q_2(t = 6) using Q_2(t).

# A^TAc = A^Ty
# y = c_1 + c_2t + c_3t^2

A2 = np.column_stack([np.ones(len(t_values)), t_values, t_values**2])

ATA = A2.T @ A2
ATy = A2.T @ prices

qcoefficients = np.linalg.solve(ATA, ATy)

def Q2(t):
    return qcoefficients[0] + qcoefficients[1] * t + qcoefficients[2] * (t**2)
 
print("Q_2(t) = " + str(Q2)) # todo fix the prints of the functions

print("Q_2(6) = " + str(Q2(6)))



