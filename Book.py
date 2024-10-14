class Book:
    def __init__(self, id, name, author, type, price):
        self.id = id
        self.name = name
        self.author = author
        self.type = type
        self.price = price
    def applyDiscount(self, discount):
        self.price = (self.price - self.price*discount)/100

class Bookstore:
    def __init__(self, books, name_rating):
        self.books = books
        self.name_rating = {}
    def search(self, type):
        l = []
        for i in self.books:
            if i.type == type:
                if i.author in self.name_rating:
                    if self.name_rating[i.author] > 4:
                        if i.type.lower() == 'fiction':
                            i.applydiscount(20)
                        else:
                            i.applyDiscount(10)
                        l.append(i)
        if l:
            return l
        return None
    def countBooks(self, price):
        for i in self.books:
            if i.type.lower() == 'fiction':
                i.applydiscount(20)
            else:
                i.applyDiscount(10)
        d = {}
        for i in self.books:
            if i.price < price:
                if i.author in d:
                    d[i.author] += 1
                else:
                    d[i.author] = 1
        return d if d else None
