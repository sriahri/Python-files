# PROBLEM 1
import time


# This is the provided primitive operation. Do NOT modify.
def ops():
    time.sleep(0.0001)


# Constant Time Algorithm
def your_constant_func(n):
    ops()


# Linear Time Algorithm
# Instead of having a simple for loop, we are using multiple for loops to actually see
# a difference in the running time while running.
def your_linear_func(n):
    l = []
    for i in range(n):
        l.append(i)
    maximum = l[0]
    for i in l:
        if i > maximum:
            maximum = i
    res = maximum
    for i in range(n):
        res += i


# Instead of having a simple for loop, we are using multiple for loops to actually see
# a difference in the running time while running as n increases.
def your_quad_func(n):
    l = []
    for i in range(n):
        x = []
        for j in range(n):
            x.append(j)
        l.append(x)
    maximums = []
    for i in range(n):
        maximum = 0
        for j in range(n):
            if l[i][j] > maximum:
                maximum = l[i][j]
        maximums.append(maximum)
    res = 0
    for i in range(n):
        for j in range(n):
            res += i + j


for n in [10, 20, 40, 80, 160]:
    start_time = time.time()
    your_quad_func(n)
    end_time = time.time()
    quadratic_running_time = end_time - start_time

    start_time = time.time()
    your_linear_func(n)
    end_time = time.time()
    linear_running_time = end_time - start_time
    print("n: %s | " % f"{n:5d}", end="")
    print("quad: %s | " % f"{quadratic_running_time:9.6f}", end="")
    print("linear: %s" % f"{linear_running_time:9.6f}")
