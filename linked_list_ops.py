class Node:
    def __init__(self, initial_data=None):
        self.data = initial_data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node


if __name__ == '__main__':
    num_list = linked_list()
    num_a = Node(66)
    num_b = Node(99)
    num_c = Node(44)
    num_d = Node(95)
    num_e = Node(42)
    num_f = Node(17)

    num_list.append(num_b)
    num_list.append(num_c)
    num_list.append(num_e)

    num_list.prepend(num_a)

    num_list.insert_after(num_c, num_d)
    num_list.insert_after(num_e, num_f)

    print('List after adding nodes: ', end=' ')
    node = num_list.head
    while node is not None:
        print(node.data, end=' ')
        node = node.next

    print()
