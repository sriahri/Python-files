def find_common(n, a, m, b, s, c):
    s1 = set(a)
    s2 = set(b)
    s3 = set(c)
    res = s1.intersection(s2, s3)
    l = list(res)
    print(min(l))

a = [1,2,3,4,5]
b = [2,3,4]
c = [1,3,7]
n = 5
m = 3
s = 3
find_common(n, a, m, b, s, c)