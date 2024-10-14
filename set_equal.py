l1 = [[1,[2,[3,4]]]]
l2 = [[[[4,3],2],1]]
s1 = set(tuple(i) for i in l1)
s2 = set(tuple(i) for i in l2)
if (s1 == s2):
    print("true")
else:
    print('False')