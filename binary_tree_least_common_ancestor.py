# Resources
# Binary Tree Node structure
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BSTree():
    def __init__(self, rootdata):
        self.root = Node(rootdata)

    def insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(data)
            else:
                self.insert(data, cur_node.left)

        elif data > cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(data)
            else:
                self.insert(data, cur_node.right)
        else:
            print("Duplicate value!")


def ancestor(root, node1, node2):
    if root is None:
        return None
    if (root.data > node1 and root.data > node2):
        return ancestor(root.left, node1, node2)
    if (root.data < node1 and root.data < node2):
        return ancestor(root.right, node1, node2)

    return root


if __name__ == '__main__':
    datalist = [550, 596, 395, 420, 730, 79, 87, 447, 611, 90, 240, 263, 29, 462, 158, 149, 611, 676, 273, 130, 137,
                446, 579, 333, 661, 385, 268, 606, 313, 112, 589, 91, 166, 267, 198, 280, 376, 323, 389, 741, 354, 799,
                733, 771, 290, 179, 564, 762, 417, 636, 366, 342, 51, 343, 28, 143, 261, 376, 80, 25, 711, 758, 747, 37,
                624, 239, 311, 255, 648, 345, 320, 248, 659, 700, 683, 684, 770, 560, 277, 214, 319, 76, 714, 274, 125,
                459, 502, 282, 481, 361, 386, 152, 310, 27, 372, 701, 473, 222, 360, 60, 261, 439, 387, 553, 181, 584,
                42, 740, 506, 242, 738, 114, 296, 24, 100, 537, 375, 439, 297, 170, 735, 635, 295, 330, 414, 492, 607,
                458, 157, 62, 321, 266, 332, 599, 155, 174, 102, 492, 555, 332, 110, 777, 249, 315, 294, 420, 597, 762,
                654, 153, 432, 526, 580, 156, 157, 360, 534, 108, 498, 373, 713, 599, 589, 301, 505, 103, 239, 706, 162,
                761, 563, 287, 421, 157, 442, 289, 735, 206, 329, 155, 609, 609, 178, 662, 249, 478, 119, 257, 178, 122,
                274, 734, 78, 791, 645, 76, 783, 144, 496, 499, 609, 470, 413, 320, 338, 62, 235, 708, 167, 270]

    bstree = BSTree(datalist[0])
    for data in datalist[1:]:
        bstree.insert(data, bstree.root)

    print('Lowest common ancestor for  (376, 770) is ', ancestor(bstree.root, 376, 770).data)
    print('Lowest common ancestor for  (589, 103) is ', ancestor(bstree.root, 589, 103).data)
    print('Lowest common ancestor for  (506, 991) is ', ancestor(bstree.root, 506, 991).data)
