import numpy as np

def redlich_kister_binary(x1, x2, A):
    summation = 0
    for k in range(len(A)):
        summation += A[k] * (x1 - x2)**k
    return x1 * x2 * summation


# ---------------------------
# User Input
# ---------------------------

print("BINARY LIQUID MIXTURE CALCULATION\n")

x1 = float(input("Enter mole fraction x1: "))
x2 = 1-x1

# Check
if not np.isclose(x1 + x2, 1.0):
    print("Warning: x1 + x2 should be 1")

coeffs = input("Enter Redlich-Kister coefficients (A0 A1 A2 ...): ")
A = list(map(float, coeffs.split()))

# ---------------------------
# Calculation
# ---------------------------

GE = redlich_kister_binary(x1, x2, A)

print("\nExcess Gibbs Energy (GE) =", GE)
