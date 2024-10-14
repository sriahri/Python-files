class A():
    x = 1

    def __init__(self, n):
        self.y = n
        A.x += 1

    def p(self):
        print(self.y)
        self.y += 3
        self.r()

    def r(self):
        self.y += 2
        print(self.y)


class B(A):
    x = 10

    def __init__(self, n):
        super().__init__(n)
        sum = self.y + B.x
        self.m = sum

    def r(self):
        self.y += self.x
        print(self.m)


a = A(1)
b = B(2)
a.p()
a.r()
b.r()
