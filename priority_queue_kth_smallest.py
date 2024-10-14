class PriorityQueue:

    def __init__(self, values=None):
        self.binary_heap = [0]
        self.size = 0

        if values != None:
            for value in values:
                self.insert(value)

    def __str__(self):
        return str(self.binary_heap)

    def __len__(self):
        return self.size

    def percolate_up(self, i):
        while i // 2 > 0 and self.binary_heap[i] < self.binary_heap[i // 2]:
            self.binary_heap[i], self.binary_heap[i // 2] = self.binary_heap[i // 2], self.binary_heap[i]
            i = i // 2

    def get_smaller_child_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.binary_heap[i * 2] < self.binary_heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolate_down(self, i):
        while (i * 2) <= self.size:
            mc = self.get_smaller_child_index(i)
            if self.binary_heap[i] > self.binary_heap[mc]:
                self.binary_heap[mc], self.binary_heap[i] = self.binary_heap[i], self.binary_heap[mc]
            i = mc

    def insert(self, item):
        self.binary_heap.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def get_minimum(self):
        if self.binary_heap[1] != None:
            return self.binary_heap[1]

    def delete_minimum(self):
        root_index = 1
        min_v = self.binary_heap[root_index]
        self.binary_heap[root_index] = self.binary_heap[self.size]
        self.binary_heap.pop()
        self.size -= 1
        self.percolate_down(root_index)
        return min_v

    def heap_update(self, index, value):
        if index < len(self.binary_heap):
            self.binary_heap[index - 1] = value


def get_kth_smallest(priority_queue, k):
    if k >= priority_queue.size:
        return None
    for i in range(k - 1):
        priority_queue.delete_minimum()
    return priority_queue.get_minimum()


priority_queue = PriorityQueue([2, 3, 4])
print("Before: ", priority_queue)
priority_queue.heap_update(4, 1)
print("After:  ", priority_queue)

priority_queue = PriorityQueue([2, 3, 4])
print("Before: ", priority_queue)
priority_queue.heap_update(2, 1)
print("After:  ", priority_queue)

priority_queue = PriorityQueue([2, 3, 4])
print("Before: ", priority_queue)
priority_queue.heap_update(1, 5)
print("After:  ", priority_queue)
