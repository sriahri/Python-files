class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
    def getvalue(self):
        return self.value
    def setvalue(self,value):
        self.value = value
    def setnext(self, next):
        self.next = next
    def getnext(self):
        return self.next

########################################

class Stack:

    def __init__(self):
        self.top = None
    def getfirst(self):
        return self.top
    def settop(self, top):
        self.top = top
    def traverse(self):
        current = self.top
        while current != None:
            print(current.getvalue())
            current = current.getnext()
            print("")
    def push(self, to_be_inserted): # This is O(1)
        to_be_inserted.setnext(self.top)
        self.top = to_be_inserted
    def pop(self): # This is O(1)
        if self.top == None:
            return None
        else:
            top_element = self.top
            self.top = self.top.getnext()
            return top_element

########################################

class Queue:

    def __init__(self):
        self.head = None
    def gethead(self):
        return self.head
    def sethead(self, head):
        self.head = head
    def traverse(self):
        current = self.head
        while current != None:
            print(current.getvalue())
            current = current.getnext()
            print("")
    def enqueue(self, to_be_inserted): # This is O(1)
        to_be_inserted.setnext(self.head)
        self.head = to_be_inserted
    def dequeue(self): # This is O(n), where n is the size of the queue
        if self.head == None:
            return False
        if self.head.getnext() == None:
            item = self.head
            self.head = None
            return item
        current = self.head
        previous = self.head
        while current != None:
            if current.getnext() == None:
                previous.setnext(None)
                return current
            previous = current
            current = current.getnext()

    #######################################

    # Your q3() algorithm goes below.

def q3(lst, stack, queue):
    for i in lst:
        node = Node(i)
        stack.push(node)
        queue.enqueue(node)
    # Since the stack uses LIFO manner, the first popped out 
    # element is generally the last element in the list.
    for i in lst:
        if stack.pop().getvalue() != i:
            print('The stack reverse and the list are not equal')
            break
        
    else:
        print('The stack when reversed is the same')
    
    # Since the queue uses FIFO manner, the first popped out element 
    # is the first element in the list. So, we reverse the list and then check.
    for i in lst[::-1]:
        if queue.dequeue().getvalue() != i:
            print('The queue reverse and the list are not same')
            break
    else:
        print('The queue reverse and the list are same.')
########################################

def main():

    stack = Stack()

    queue = Queue()

    # lst = [1, 3, 5, 8, 5 ,8 , 9, 7]
    lst = [1, 2, 3, 2, 1]

    q3(lst, stack, queue)

main()