class MaxHeap:
    def __init__(self,maximum):
        self.maximum = maximum
        self.size = 0
        self.l = [0] * ((self.maximum)+1)
        self.l[0] = 99999999
        self.f = 1
    def parentOfChild(self,position):
        return position//2
    def insert(self,x):
        if self.size >= self.maximum:
            return
        else:
            self.size += 1
            self.l[self.size] = x
            c = self.size
            while self.l[c] > self.l[self.parentOfChild(c)]:
                temp = self.l[c]
                self.l[c] = self.l[self.parentOfChild(c)]
                self.l[self.parentOfChild(c)] = temp
                c = self.parentOfChild(c)
    def printHeap(self):
        for i in range(1,self.size//2):
            print('Parent - ',self.l[i])
            print('Left Child - ',self.l[2*i])
            print('Right Child - ',self.l[2*i+1])

heapObj = MaxHeap(11)
heapObj.insert(35)
heapObj.insert(33)
heapObj.insert(42)
heapObj.insert(10)
heapObj.insert(14)
heapObj.insert(19)
heapObj.insert(27)
heapObj.insert(44)
heapObj.insert(26)
heapObj.insert(31)
heapObj.printHeap()