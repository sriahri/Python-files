class Calory:
    def __init__(self, lettuce, spinach, celery, cucumber, radish):
        self.lettuce = lettuce
        self.spinach = spinach
        self.celery = celery
        self.cucumber = cucumber
        self.radish = radish

    def calculate_total(self, lettuce=0, spinach=0, celery=0, cucumber=0, radish=0):
        total_calories = lettuce / 100 * self.lettuce
        total_calories += spinach / 100 * self.spinach
        total_calories += celery / 100 * self.celery
        total_calories += cucumber / 100 * self.cucumber
        total_calories += radish / 100 * self.radish

        return total_calories


veggie_calories = Calory(15, 23, 14, 12, 16)
print("The total calories for your vegetable intake is {}".format(
    veggie_calories.calculate_total(celery=200, cucumber=360)))
print("The total calories for your vegetable intake is {}".format(
    veggie_calories.calculate_total(lettuce=150, spinach=50, radish=300)))
