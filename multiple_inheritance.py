class First:
    def __init__(self, name) -> None:
        self.name = name
class Second:
    def __init__(self, surname) -> None:
        self.surname = 'There'
class Third(First, Second):
    def __init__(self, name, surname) -> None:
        super(Third, self).__init__(name)
        print(self.name)
        print(self.surname)
x = Third('Hi', 'Hey')