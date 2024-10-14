class Toy:
    def __init__(self, name, colour, cost, toy_type):
        self.name = name
        self.colour = colour
        self.cost = cost
        self.toy_type = toy_type


class ToyBox:
    def __init__(self):
        self.all_toys = []

    def add_toy(self, name, colour, cost, toy_type):
        a_toy = Toy(name, colour, cost, toy_type)
        self.all_toys.append(a_toy)

    def get_total_toys(self):
        return len(self.all_toys)

    def get_total_cost(self):
        total_cost = 0
        for a_toy in self.all_toys:
            total_cost += a_toy.cost
        return total_cost

    def get_cheapest_toy(self):
        if (total_toys := self.get_total_toys()) > 0:
            cheapest_toy = 'The toy box is empty'
            cheap_value = 200
            for a_toy in self.all_toys:
                if a_toy.cost < cheap_value:
                    cheap_value = a_toy.cost
                    cheapest_toy = a_toy.name
            return cheapest_toy
        else:
            return 'The toy box is empty'

    def __str__(self):
        total_count = len(self.all_toys)
        msg = 'The toy box contains {} toys\n'.format(total_count)
        if total_count > 0:
            for a_toy in self.all_toys:
                msg += 'A {} {} called {} is present and costs {}\n'.format(a_toy.colour, a_toy.toy_type, a_toy.name,
                                                                          a_toy.cost)

            return msg
        else:
            return 'The box is empty'


red_toybox = ToyBox()
print(red_toybox)
cheapest_toy = red_toybox.get_cheapest_toy()
print('{}'.format(cheapest_toy))
print('Adding toys')
red_toybox.add_toy('Funny Ted', 'Grey', 14.99, 'Teddy Bear')
red_toybox.add_toy('Buzz Lightyear', 'Yellow', 12.99, 'Action Figure')
red_toybox.add_toy('Rocking horse', 'Green', 19.99, 'Wooden Toy')
print(red_toybox)
print('Adding a cheap toy')
red_toybox.add_toy('Lego car', 'Green', 9.99, 'Lego model')
print(red_toybox)
cheapest_toy = red_toybox.get_cheapest_toy()
print('{}'.format(cheapest_toy))
