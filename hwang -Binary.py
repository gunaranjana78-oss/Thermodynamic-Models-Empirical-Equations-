import math

# Coefficients
d0 = -0.294
d1 = -0.658
d2 = -0.179


# Number of data points
n = int(input("Enter the number of data points: "))

# Input values for x1, x2, and x3
x1 = []
x2 = []

for i in range(n):
    print(f"\nData point {i + 1}:")
    x1.append(float(input("Enter x1: ")))
    x=1- x1[i]
    x2.append(x)
    
v123=[]
print (" x1\tx2\tv123")
# Calculate interaction values
for i in range(n):
    v12 = x1[i] * x2[i] * (d0 + d1 * pow(x1[i], 3) + d2 * pow(x2[i], 3))
    v123.append(v12)
    #print (x1[i], x2[i], x3[i], v123[i])
    print(f"{x1[i]:.4f} {x2[i]:.4f} {v123[i]:.4f}" )
    
