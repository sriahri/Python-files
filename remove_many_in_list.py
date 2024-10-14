class List:
    def __init__(self, elements_list):
        self.elements_list = elements_list

    def remove_many(self, element):
        n = len(self.elements_list)
        temp_list = []
        for i in self.elements_list:
            if i != element:
                temp_list.append(i)

        self.elements_list = temp_list.copy()

    def __str__(self):
        if not self.elements_list:
            return '[]'
        temp = map(str, self.elements_list)
        return ','.join(temp)


if __name__ == '__main__':
    main_list = [5, 1, 7, 4, 5, 4, 3, 2]
    lst = List(main_list)
    print(lst)

    lst.remove_many(5)
    print(lst)

    main_list = [1, 1, 1, 1, 1, 1]
    lst = List(main_list)
    print(lst)

    lst.remove_many(1)
    print(lst)
