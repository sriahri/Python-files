class First_Last_PascalTriangle:
    def __init__(self, rows):
        self.rows = rows
        self.triangle = []

# Method for generating and printing the triangle
    def generate_triangle(self):
        for i in range(self.rows):
            self.triangle.append([])
            # print(self.triangle)
            self.triangle[i].append(1)
            for j in range(1, i):
                self.triangle[i].append(self.get_choices(i, j))
            if self.rows != 0:
                self.triangle[i].append(1)
        for i in range(self.rows):
            print(" " * (self.rows - i), end=" ", sep=" ")
            for j in range(0, i + 1):
                print('{}'.format(self.triangle[i][j]), end=" ", sep=" ")
            print()

# Method for returning the value for each element
    def get_choices(self, n, k):
        return self.triangle[n - 1][k - 1] + self.triangle[n - 1][k]


number_of_rows = int(input('Enter the number of rows: '))
pascal_triangle = First_Last_PascalTriangle(number_of_rows)
pascal_triangle.generate_triangle()
