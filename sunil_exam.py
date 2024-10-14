import numpy as np
from sys import stdin, argv
A = []
B = []
n = int(input("Enter the number of variable sto solve : "))
for i in range(n):
    l = list(map(float,input().split()))
    A.append(l[:-1])
    B.append(l[-1])
coefficients = np.array(A)
constants = np.array(B)
X = np.linalg.inv(coefficients).dot(constants)
for i in range(len(X)):
  print(X[i])