class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Entry(Car):
    def __init__(self, make, model, year, driver, number):
        super(Entry, self).__init__(make, model, year)
        self.driver = driver
        self.number = number

    def printEntry(self):
        print("{} {} {} {} {}".format(self.make, self.model, self.year, self.driver, self.number))


entry = Entry("ABC", "AXED234", 2013, "John", "65498712")
entry.printEntry()
entry = Entry("DEF", "BCSD234", 2018, "Smith", "9876541")
entry.printEntry()