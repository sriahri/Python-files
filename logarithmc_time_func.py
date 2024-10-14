# PROBLEM 2
# ------------- IMPLEMENT ON YOUR OWN -------------
import time


# This is the provided primitive operation. Do NOT modify.
def ops():
    time.sleep(0.1)


# Logarithmic (Base 2) Time Algorithm
def your_logn_func(n):
    i = 1
    res = 0
    while i < n:
        res += i
        i *= 2

    i = n
    while i > 0:
        res += i
        i = i // 2
    i = 1
    while i < n:
        res += i
        i = i * 2

    i = n
    while i > 0:
        res += i
        i = i // 2

    i = 1
    while i < n:
        res += i
        i = i * 2

    i = n
    while i > 0:
        res += i
        i = i // 2

    i = 1
    while i < n:
        res += i
        i = i * 2

    i = n
    while i > 0:
        res += i
        i = i // 2


# ------------- YOUR CODE GOES HERE -------------

# -----------------------------------------------

# n log n Time Algorithm
def your_nlogn_func(n):
    res = 0
    for i in range(n):
        j = 1
        while j < n:
            res += i + j
            j = j * 2

    for i in range(n):
        j = n
        while j > 0:
            res += i + j
            j = j // 2

    for i in range(n):
        j = 1
        while j < n:
            res += i + j
            j = j * 2

    for i in range(n):
        j = n
        while j > 0:
            res += i + j
            j = j // 2

    for i in range(n):
        j = 1
        while j < n:
            res += i + j
            j = j * 2

    for i in range(n):
        j = n
        while j > 0:
            res += i + j
            j = j // 2

    for i in range(n):
        j = 1
        while j < n:
            res += i + j
            j = j * 2

    for i in range(n):
        j = n
        while j > 0:
            res += i + j
            j = j // 2


# ------------- YOUR CODE GOES HERE -------------

# -----------------------------------------------

import math

for n in [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10480, 20960, 41920, 83840]:
    start_time = time.time()
    your_logn_func(n)
    end_time = time.time()
    logn_running_time = end_time - start_time

    print("n: %s | " % f"{n:5d}", end="")
    print("logn: %s | " % f"{logn_running_time:9.6f}", end="")
    print("each iteration took %s sec" % f"{logn_running_time / math.log2(n):9.6f}")
print()
for n in [10, 20, 40]:
    start_time = time.time()
    your_nlogn_func(n)
    end_time = time.time()
    nlogn_running_time = end_time - start_time

    print("n: %s | " % f"{n:5d}", end="")
    print("nlogn: %s | " % f"{nlogn_running_time:9.6f}", end="")
    print("each iteration took %s sec" % f"{nlogn_running_time / (n * math.log2(n)):9.6f}")
