class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('Error: The stack is empty')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Error: The stack is empty')
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)[:-1] + ' <-'

    def clear(self):
        self.items = []


def remove_negatives(stack):
    for item in stack.items:
        if item < 0:
            stack.items.remove(item)


s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(-3)
s1.push(4)
s1.push(5)

print(s1)
remove_negatives(s1)
print(s1)

print()
s1 = Stack()
s1.push(-1)
s1.push(2)
s1.push(-3)
s1.push(4)
s1.push(-5)

print(s1)
remove_negatives(s1)
print(s1)