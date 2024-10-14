class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def largest(root):
    count = [0]
    helper(root, count)


def helper(root, count):
    if root is None or count[0] >= 2:
        return

    helper(root.right, count)
    count[0] += 1

    if count[0] == 2:
        print('Second largest element is {}'.format(root.data))
        return

    helper(root.left, count)


def insert_into_bst(node, data):
    if node is None:
        return Node(data)

    if data < node.data:
        node.left = insert_into_bst(node.left, data)
    elif data > node.data:
        node.right = insert_into_bst(node.right, data)

    return node


if __name__ == '__main__':
    root = None
    root = insert_into_bst(root, 12)
    insert_into_bst(root, 38)
    insert_into_bst(root, 21)
    insert_into_bst(root, 46)
    insert_into_bst(root, 77)
    insert_into_bst(root, 61)
    insert_into_bst(root, 89)

    largest(root)
