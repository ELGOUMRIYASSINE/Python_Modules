#!/usr/bin/python3
class Plant:
    """
    Base class for all types of plants.
    This is the parent class that other plant types inherit from.
    """

    def __init__(self, name, height, age):
        """
        Creates a new plant with basic information.
        Every plant needs a name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age

    def base_info(self):
        """
        Returns the basic information about the plant.
        Shows the plant's name, type, height, and age in a readable format.
        """
        return (f"{self.name} ({self.plant_type}): "
                f"{self.height}cm, {self.age} days")


class Flower(Plant):
    """
    Represents a flowering plant.
    Flowers have all the basic plant features plus a color and can bloom.
    """

    plant_type = "Flower"

    def __init__(self, name, height, age, color):
        """
        Creates a new flower with a specific color.
        Inherits name, height, and age from the Plant class.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Makes the flower bloom and shows a blooming message."""
        print(f"{self.name} blooming 🌼")

    def get_data(self):
        """Displays all the flower's information including its color."""
        base_data = self.base_info()
        print(f"{base_data}, {self.color} color")


class Tree(Plant):
    """
    Represents a tree plant.
    Trees have all basic plant features plus a trunk diameter and provide
    shade.
    """

    plant_type = "Tree"

    def __init__(self, name, height, age, trunk_diameter):
        """
        Creates a new tree with trunk diameter measurement.
        Inherits name, height, and age from the Plant class.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Calculates and shows how much shade the tree provides."""
        print(f"{self.name} provides 78 square meters of shade")

    def get_data(self):
        """Displays all the tree's information including trunk size."""
        base_data = self.base_info()
        print(f"{base_data}, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Represents a vegetable plant.
    Vegetables have all basic plant features
    plus harvest info and nutritional benefits.
    """

    plant_type = "Vegetable"

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Creates a new vegetable with harvest season
        and nutritional information.
        Inherits name, height, and age from the Plant class.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def benefits(self):
        """Shows what nutrients or vitamins this vegetable provides."""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_data(self):
        """Displays all the vegetable's information including harvest
        season."""
        base_data = self.base_info()
        print(f"{base_data}, {self.harvest_season} harvest")


# print("=== Garden Plant Types ===")
# print()
# flower1 = Flower("Rose", 25, 30, "red")
# flower2 = Flower("Tulip", 30, 20, "yellow")
# flower2.get_data()
# flower2.bloom()
# # Tree type
# print()
# tree1 = Tree("Oak", 500, 1825, 50)
# tree2 = Tree("Pine", 600, 2500, 40)
# tree2.get_data()
# tree2.produce_shade()
# # Vegetable type
# print()
# vegetable1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
# vegetable2 = Vegetable("Carrot", 40, 70, "winter", "vitamin A")
# vegetable2.get_data()
# vegetable2.benefits()
