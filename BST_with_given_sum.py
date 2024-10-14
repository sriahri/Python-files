class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    if (data < root.data):
        root.left = insert(root.left, data)
    if (data > root.data):
        root.right = insert(root.right, data)
    return root


def inorderTraversal(root):
    result = []
    if root:
        result = inorderTraversal(root.left)
        result.append(root.data)
        result += inorderTraversal(root.right)
    return result


def checkPair(root, x):
    result = inorderTraversal(root)
    for i in result:
        if x - i in result:
            return True
    return False


root = None
root = insert(root, 15)
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 8)
root = insert(root, 12)
root = insert(root, 16)
root = insert(root, 25)
x = 33
print(checkPair(root, x))
