class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(root, data):
    if root is None:
        return TreeNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
    return root


def inorderTraversal(root):
    result = []
    if root:
        result = inorderTraversal(root.left)
        result.append(root.data)
        result += inorderTraversal(root.right)
    return result


def tree_sum(root, k):
    all_values = inorderTraversal(root)
    sum_values = 0
    for i in all_values:
        if i <= k:
            sum_values += i

    return sum_values


if __name__ == '__main__':
    root = None
    root = insert(root, 11)
    root = insert(root, 19)
    root = insert(root, 10)
    root = insert(root, 18)
    root = insert(root, 2)
    root = insert(root, 6)
    root = insert(root, 5)

    key = 7
    print('The sum of all values in the BST less than {} is {}'.format(key, tree_sum(root, key)))

    key = 15
    print('The sum of all values in the BST less than {} is {}'.format(key, tree_sum(root, key)))

    key = 20
    print('The sum of all values in the BST less than {} is {}'.format(key, tree_sum(root, key)))
