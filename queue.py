class Queue:
    def __init__(self):
        self.q = []
    def sizeQ(self):
        return len(self.q)
    def enqueue(self,elt):
        self.q.append(elt)
    def dequeue(self):
        if self.q:
            return self.q[0]
    def popqueue(self):
        for r in range(self.sizeQ(), -1, -1):
            return self.q[r-1]

q = Queue()
q.enqueue(32)
q.enqueue(64)
q.enqueue(21)
print(q.popqueue())