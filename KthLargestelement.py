class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 

# A function to do inorder tree traversal
def Inorder(root, l):
    if root:
        Inorder(root.left, l)
        l.append(root.val),
        Inorder(root.right, l)
    else:
        return l        