#!/usr/bin/python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def base_info(self):
        return f"{self.name} ({self.plant_type}): {self.height}cm, {self.age} days"

class Flower(Plant):
    plant_type = "Flower"
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    def bloom(self):
        print(f"{self.name} blooming 🌼")
    def get_data(self):
        base_data = self.base_info()
        print(f"{base_data}, {self.color} color")

class Tree(Plant):
    plant_type = "Tree"
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade")
    def get_data(self):
        base_data = self.base_info()
        print(f"{base_data}, {self.trunk_diameter}cm diameter")

class Vegetable(Plant):
    plant_type = "Vegetable"
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def benefits(self):
        print(f"{self.name} is rich in {self.nutritional_value}")
    def get_data(self):
        base_data = self.base_info()
        print(f"{base_data}, {self.harvest_season} harvest")

print("=== Garden Plant Types ===")
print()
flower1 = Flower("Rose", 25, 30, "red")
flower2 = Flower("Tulip", 30, 20, "yellow")
flower2.get_data()
flower2.bloom()
# Tree type
print()
tree1 = Tree("Oak", 500, 1825, 50)
tree2 = Tree("Pine", 600, 2500, 40)
tree2.get_data()
tree2.produce_shade()
# Vegetable type
print()
vegetable1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
vegetable2 = Vegetable("Carrot", 40, 70, "winter", "vitamin A")
vegetable2.get_data()
vegetable2.benefits()