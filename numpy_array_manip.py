import random
import numpy as np

Q1 = np.zeros((1, 1, 20), dtype=float)
print(Q1)
Q2 = np.ones((4, 5), dtype=int)
print(Q2)
Q3 = np.array([[2 for col in range(2)] for row in range(5)])
print(Q3)
Q4 = np.array([float(i) for i in range(50)])
print(Q4)
Q5 = np.linspace(4, 18)
print(Q5)
Q6 = np.diag([1]*5)
print(Q6)
random.seed(10)
Q7 = np.array([[random.randrange(0, 1) for ____ in range(4)] for __ in range(2)])
print(Q7)
Q9 = Q7.size
print(Q9)
