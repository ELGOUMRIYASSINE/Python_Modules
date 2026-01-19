#!/usr/bin/python3
class Plant:
    """ Represent a plant with a name, height, and age. """
    def __init__(self, name, Height, Age):
        self.name = name
        self.Height = Height
        self.Age = Age
        self.week_grow = 0

    def get_info(self):
        """ Show Plants informations """
        print(f"{self.name}: {self.Height}cm, {self.Age} days old")

    def grow(self):
        """  Make the plant grow """
        self.Height += 1
        self.week_grow += 1

    def age(self):
        """  Increase plant age """
        self.Age += 1

    def day_passed(self):
        """ Simulate one day passing """
        self.grow()
        self.age()

# plant1 = Plant("orange",25,30)
# print("=== Day 1 ===")
# plant1.get_info()
# plant1.day_passed()
# plant1.day_passed()
# plant1.day_passed()
# plant1.day_passed()
# plant1.day_passed()
# plant1.day_passed()
# print("=== Day 7 ===")
# plant1.get_info()
# print(f"Growth this week: +{plant1.week_grow}cm")
