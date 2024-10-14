import sys


class Node(object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    def minimum(self):
        current = self.root
        while current.lChild is not None:
            current = current.lChild
        return current.data

    def maximum(self):
        current = self.root
        while current.rChild is not None:
            current = current.rChild

        return current.data

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        minimum = self.minimum()
        maximum = self.maximum()

        return maximum - minimum

    def get_level_helper(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.data, end=' ')
            return
        self.get_level_helper(node.lChild, level - 1)
        self.get_level_helper(node.rChild, level - 1)

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        self.get_level_helper(self.root, level)

    def left_side_view_helper(self, root, level, d):
        if root is None:
            return
        if level not in d:
            d[level] = root.data

        self.left_side_view_helper(root.lChild, level + 1, d)
        self.left_side_view_helper(root.rChild, level + 1, d)

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        d = {}

        # traverse the tree and fill the dictionary
        self.left_side_view_helper(self.root, 1, d)

        # iterate through the dictionary in sorted order of its keys
        # and print the left view
        res = ' '
        for i in range(1, len(d) + 1):
            res += str(d[i]) + ' '
        return res

    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.

    def isLeaf(self, node):
        if node is None:
            return False
        if node.lChild is None and node.rChild is None:
            return True
        return False

    def leftLeavesSum(self, root):
        res = 0
        if root is not None:
            if self.isLeaf(root.lChild):
                res += root.lChild.data
            else:
                res += self.leftLeavesSum(root.lChild)
            res += self.leftLeavesSum(root.rChild)
        return res

    def rightLeavesSum(self, root):
        res = 0
        if root is not None:
            if self.isLeaf(root.rChild):
                res += root.rChild.data
            else:
                res += self.rightLeavesSum(root.lChild)
            res += self.rightLeavesSum(root.rChild)
        return res

    def sum_leaf_nodes(self):
        total = self.leftLeavesSum(self.root) + self.rightLeavesSum(self.root)
        return total


def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ", t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

    # Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ", t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")
    # Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ", t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()
