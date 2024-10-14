class MYDataStructure:
    def __init__(self):
        self.structure = {}

    def insert(self, key, value):
        if key not in self.structure:
            self.structure[key] = value

    def delete(self, key):
        if key in self.structure:
            del self.structure[key]

    def range_sum(self, x_left, x_right):
        total = 0
        for key, value in self.structure.items():
            if x_left <= key <= x_right:
                total += value
        return total

    def search(self, key):
        if key in self.structure:
            return self.structure[key]
        return 'Not available'

    def printDataStructure(self):
        res = 'The data structure contains ' + self.structure.__str__()
        return res


ds = MYDataStructure()
ds.insert(12, 83)
ds.insert(11, 65)
ds.insert(13, 40)
ds.insert(14, 99)
ds.insert(15, 28)
print(ds.printDataStructure())
ds.delete(13)
print(ds.printDataStructure())
print('The range sum between {} and {} is {}'.format(12, 14, ds.range_sum(12, 14)))
