import random
from datetime import datetime, timedelta


class RandomValues:
    first_names = ["Lisa", "Otto", "Max", "Herbert", "Peter", "Thomas", "Stephan"]
    last_names = ["Mustermann", "Grönemeyer", "Lustig", "Müller", "Paßlack", "Simpson"]
    now = datetime.now()

    def __init__(self, seed):
        random.seed(seed)

    def boolean_value(self):
        return random.randint(0, 1) == 0

    def int_value(self, start=1, end=100):
        return random.randint(start, end)

    def first_name(self):
        return self.first_names[random.randint(0, len(self.first_names) - 1)]

    def last_name(self):
        return self.last_names[random.randint(0, len(self.last_names) - 1)]

    def float_value(self):
        return round(random.uniform(0.1, 10.0), 2)

    def date(self, today=False):
        if today:
            d = datetime(self.now.year - self.int_value(18, 60), self.now.month, self.now.day)
        else:
            d = self.now - timedelta(days=self.int_value(18 * 365, 60 * 365))
        return d.strftime('%Y-%m-%d')


Dishes = ["Lasagne", "Folienkartoffeln", 'Pizza', 'Burger']
