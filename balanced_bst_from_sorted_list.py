class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


def BST_from_sorted_values(values):
    if not values:
        return None
    middle = len(values) // 2
    root = BinarySearchTree(values[middle])
    root.left = BST_from_sorted_values(values[:middle])
    root.right = BST_from_sorted_values(values[middle + 1:])

    return root


def traversal(root):
    if not root:
        return None
    print(root.data)
    traversal(root.left)
    traversal(root.right)


values = [1, 2, 3, 4, 5, 6, 7]
root = BST_from_sorted_values(values)
traversal(root)
# printTree(root)
