class list135:
    def __init__(self, first_item=None, rest_of_list=None):
        self._first_item = first_item
        self._rest_of_list = rest_of_list

    def cons(self, first_item):
        return list135(first_item)

    def first(self):
        return self._first_item

    def rest(self):
        return self._rest_of_list

    def empty(self):
        return self._rest_of_list == None

    def __str__(self):
        result = "["
        cur = self
        if cur._rest_of_list != None:
            result = result + str(cur._first_item)
            cur = cur._rest_of_list

        while cur._rest_of_list != None:
            result = result + ',' + str(cur._first_item)
            cur = cur._rest_of_list

        return result + "]"

    def sorted(self):
        copy_list = []
        for item in self._rest_of_list:
            copy_list.append(item)
        copy_list.sort()

        if copy_list[0] > self.first():
            copy_list = list(self.first()) + copy_list
        else:
            copy_list.append(self.first())

        return copy_list


if __name__ == '__main__':
    list_item = list135(65, [22, 12, 16, 76, 89, 99])
    sorted_list = list_item.sorted()
    print(sorted_list)
