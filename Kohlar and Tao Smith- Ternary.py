c=0
while True:
    x1 = float(input("Enter X1: "))
    x2 = float(input("Enter X2: "))
    x3 = 1 - x1 - x2

    # A12
    a12 = input("Enter the A12 coeff a0 a1 a2 ")
    A12 = list(map(float, a12.split()))
    # A13
    a13 = input("Enter the A13 coeff a0 a1 a2 ")
    A13 = list(map(float, a13.split()))
    # A23
    a23 = input("Enter the A23 coeff a0 a1 a2 ")
    A23 = list(map(float, a23.split()))
         
    def RK(x, A):
        return x * (1-x) * (
            A[0] +
            A[1] * (2*x-1) +
            A[2] * (2*x-1)**2
        )


    # Kohler
    V12 = RK(x1/(x1+x2), A12)
    V13 = RK(x1/(x1+x3), A13)
    V23 = RK(x2/(x2+x3), A23)

    K = ((x1+x2)**2 * V12 +
         (x1+x3)**2 * V13 +
         (x2+x3)**2 * V23)


    # Tsao-Smith
    V12 = RK(x1, A12)
    V13 = RK(x1, A13)
    V23 = RK(x2/(x2+x3), A23)

    TS = ((x2/(1-x1))*V12 +
          (x3/(1-x1))*V13 +
          (1-x1)*V23)


    print("\nX3 =", round(x3, 4))
    print("Kohler =",round(K, 4))
    print("Tsao-Smith =",round(TS, 4))
    c+=1
