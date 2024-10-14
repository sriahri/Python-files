import random
import math


def is_inside_circle(x, y, r):
    return x ** 2 + y ** 2 <= r ** 2


def is_inside_rectangle(x, y, w, h):
    return 0 <= x <= w and 0 <= y <= h


def monte_carlo_intersection(r, w, h, num_points=1000000):
    count = 0
    for _ in range(num_points):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if is_inside_circle(x, y, r) and is_inside_rectangle(x + r, y + r, w, h):
            count += 1
    area_circle = math.pi * r ** 2
    return (count / num_points) * area_circle


# Example usage
r = 50
w = 100
h = 100
intersection_area = monte_carlo_intersection(r, w, h)
print(f"Approximate area of intersection: {intersection_area}")
