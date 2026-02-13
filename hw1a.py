import numpy as np

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

t = np.arange(1,11)

# prices (y)
prices = np.array([410.50, 415.80, 422.30, 428.15, 432.60, 435.20, 430.90, 431.46, 416.56, 430.41])

A = np.column_stack([np.ones(len(t)), t, t**2, t**3])

ATA = A.T @ A
ATy = A.T @ prices

cofficients = np.linalg.solve(ATA, ATy)

def C(t):
    return cofficients[0] + cofficients[1] * t + cofficients[2] * (t**2) + cofficients[3] * (t**3)

print("Cubic fit for Tesla stock: " + str(cofficients[0]) + " + " + str(cofficients[1]) + " * t" + " + " + str(cofficients[2]) + " * (t^2) " + str(cofficients[3]) + " * (t^3)")


# todo are we supposed to plot?