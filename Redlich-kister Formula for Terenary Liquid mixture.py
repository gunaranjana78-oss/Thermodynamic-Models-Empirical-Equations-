import numpy as np
c=0
while True:
    def redlich_kister_binary(xi, xj, A):
        summation = 0
        for k in range(len(A)):
            summation += A[k] * (xi - xj)**k
        return xi * xj * summation


    def redlich_kister_ternary(x1, x2, x3, A12, A13, A23, L123=0):
        term12 = redlich_kister_binary(x1, x2, A12)
        term13 = redlich_kister_binary(x1, x3, A13)
        term23 = redlich_kister_binary(x2, x3, A23)

        ternary_term = x1 * x2 * x3 * L123
        return term12, term13, term23
        GE = term12 + term13 + term23 + ternary_term
        return GE


    # ---------------------------
    # User Input
    # ---------------------------

    print("TERNARY LIQUID MIXTURE CALCULATION\n")

    x1 = float(input("Enter x1: "))
    x2 = float(input("Enter x2: "))
    x3 = 1-(x1+x2)

    if not np.isclose(x1 + x2 + x3, 1.0):
        print("Warning: x1 + x2 + x3 should be 1")



    # A12
    a12 = input("Enter the A12 coeff a0 a1 a2 ")
    A12 = list(map(float, a12.split()))
    # A13
    a13 = input("Enter the A13 coeff a0 a1 a2 ")
    A13 = list(map(float, a13.split()))
    # A23
    a23 = input("Enter the A23 coeff a0 a1 a2 ")
    A23 = list(map(float, a23.split()))
         

    L123 = 0

    # ---------------------------
    # Calculation
    # ---------------------------

    GE = redlich_kister_ternary(x1, x2, x3, A12, A13, A23, L123)

    print("/n X3 Value : ", round (x3,4))
    print("\nExcess Gibbs Energy (GE) =",round(GE,4))
    print ("A B C", term12, term13, term23 )
    c+=1
