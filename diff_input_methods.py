from sys import stdin

a, b, c = map(int, input().split())

print(a, b, c)

l = list(map(int, input().split()))

print(l)

l = [int(i) for i in input().split()]

print(l)

l = []
for i in stdin.readlines():
    l.append(int(i))

print(l)
