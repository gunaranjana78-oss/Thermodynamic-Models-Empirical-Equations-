import math

# Coefficients
d0 = -0.125
d1 = 1.464
d2 = -1.440

e0 = -5.382
e1 = 1.695
e2 = -0.580

f0 = 0.081
f1 = 0.477
f2 = -0.406

# Number of data points
n = int(input("Enter the number of data points: "))

# Input values for x1, x2, and x3
x1 = []
x2 = []
x3 = []

for i in range(n):
    print(f"\nData point {i + 1}:")
    x1.append(float(input("Enter x1: ")))
    x2.append(float(input("Enter x2: ")))
    x=1-(x1[i]+x2[i])
    x3.append(x)
    
v123=[]
print (" x1\tx2\tx3\tv123")
# Calculate interaction values
for i in range(n):
    v12 = x1[i] * x2[i] * (d0 + d1 * pow(x1[i], 3) + d2 * pow(x2[i], 3))
    v13 = x1[i] * x3[i] * (e0 + e1 * pow(x1[i], 3) + e2 * pow(x3[i], 3))
    v23 = x2[i] * x3[i] * (f0 + f1 * pow(x2[i], 3) + f2 * pow(x3[i], 3))
    v123.append(v12 + v13 + v23)
    #print (x1[i], x2[i], x3[i], v123[i])
    print(f"{x1[i]:.4f} {x2[i]:.4f} {x3[i]:.4f} {v123[i]:.4f}" )
    
