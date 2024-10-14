class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, item):
        new_node = Node(item, self.head)
        if self.head is None:
            self.head = new_node
            self.count += 1
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.count += 1

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def search(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        found = False
        current = self.head
        previous = None
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
            if found:
                if previous is None:
                    self.head = current.next
                else:
                    previous.set_next(current.next)
                self.count -= 1

    def __str__(self):
        res = ""
        current = self.head
        while current:
            res += str(current.data)
            current = current.next
        return res


l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
print(l.is_empty())
print("The list size is {}".format(l.size()))
print("The search of 3 is {}".format(l.search(3)))
l.remove(2)
print("The list size is {}".format(l.size()))
