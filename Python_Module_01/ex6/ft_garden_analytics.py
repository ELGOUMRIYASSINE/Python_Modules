class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []
    def add_plant(self,plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name} garden")
    def get_growth(self,plant):
        return plant.total_growth()
    def grow_plants(self):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew {plant.growth}cm")
    def plants_in_garden(self):
        print("Plants in garden:")
        for plant in self.plants:
            if (plant.plant_type == "regular"):
                print(f"- {plant.base_data()}")
                # print(plant.plant_type)
            else:
                print(plant.show_data())
                # print(plant.plant_type)
    # def show_plants(self):
    #     for plant in self.plants:
    #         print(plant.name)
    # class GardenStats:
    #     pass
    
class Plant:
    plant_type = "regular"
    plant_count = 0
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0
        Plant.plant_count += 1
    def grow(self):
        self.height += 1
        self.growth += 1
    def total_growth(self):
        return (self.growth)
    def base_data(self):
        return f"{self.name}: {self.height}"
        
class FloweringPlant(Plant):
    plant_type = "flowering"
    plant_count = 0
    def __init__(self, name, height, age, color, bloom_status):
        super().__init__(name, height, age)
        self.color = color
        self.bloom_status = bloom_status
        FloweringPlant.plant_count += 1
    def show_data(self):
        base_data = self.base_data()
        return f"- {base_data} {self.color} flowers ({self.bloom_status})"

class PrizeFlower(FloweringPlant):
    plant_type = "prize flowers"
    plant_count = 0
    def __init__(self, name, height, age, color, bloom_status, prize):
        super().__init__(name, height, age, color, bloom_status)
        self.prize = prize
        PrizeFlower.plant_count += 1
    def show_data(self):
        base_data = self.base_data()
        return f"- {base_data} {self.color} flowers ({self.bloom_status}), Prize points: {self.prize}"

        
print("=== Garden Management System Demo ===")


p1 = Plant("Oak Tree", 20, 19)
p2 = FloweringPlant("Rose", 4, 30, "green", "blooming")
p3 = PrizeFlower("Sunflower", 4, 30, "red", "blooming", 20)

g1 = Garden("Alice's")
g1.add_plant(p1)
g1.add_plant(p2)
g1.add_plant(p3)

print()

g1.grow_plants()

print("=== Alice's Garden Report ===")
g1.plants_in_garden()