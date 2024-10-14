from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.container = ArrayDeque()
    def add(self,data):
        self.container.add_list(data)
    def remove(self):
        return self.delete_first()
    def get_size(self):
        return len(self.container)
    def __str__(self):
        return f'size of container is {self.get_size()}'

qobj = Queue()
qobj.add(23)
qobj.add(34)
qobj.add(45)
qobj.add(56)
print(qobj.__str__())
qobj.remove()
print(qobj.__str__())