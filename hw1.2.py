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
prices = np.array([5015,5190,5400,5396,4865])

P4_coefficients = np.polyfit(t_values, prices, 4)

a_4 = P4_coefficients[0]
a_3 = P4_coefficients[1]
a_2 = P4_coefficients[2]
a_1 = P4_coefficients[3]
a_0 = P4_coefficients[4]


P4 = np.poly1d(P4_coefficients)

print("P_4(t) = " + str(P4))

print("P_4(6) = " + str(P4(6)))





# (2) Make a quadratic fit of the data Q_2(t) = a_0 + a_1t + a_2t^2 and compute Q_2(t = 6) using Q_2(t).

Q2_coefficients = np.polyfit(t_values, prices, 2)

Q2 = np.poly1d(Q2_coefficients)

print("Q_2(t) = " + str(Q2))

print("Q_2(6) = " + str(Q2(6)))



