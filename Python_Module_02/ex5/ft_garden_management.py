class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    adding_process = 0

    def __init__(self):
        self.plants = []

    def add(self, object):
        if (self.adding_process == 0):
            print("Adding plants to garden...")
        if (object.name == ""):
            raise PlantError("Error adding plant: Plant name cannot be empty!\n")
        else:
            self.plants.append(object)
            print(f"Added {object.name} successfully")
            self.adding_process += 1

    def water_plants(self):
        print("Opening watering system")
        for plant in self.plants:
            if (not (plant.water >= 1 and plant.water <= 10)):
                if (plant.water < 1):
                    raise WaterError(f"Error: Water level"
                                     f" {plant.water} is too low (min 1)\n")
                else:
                    raise WaterError(f"Error: Water level"
                                     f" {plant.water} is too high (max 10)\n")
            plant.water += 1
            print(f"Watering {plant.name} - success")

    def check_health(self):
        for plant in self.plants:
            if (not (plant.water >= 1 and plant.water <= 10)):
                if (plant.water < 1):
                    raise PlantError(f"Error: Water level"
                                     f" {plant.water} is too low (min 1)\n")
                else:
                    raise PlantError(f"Error: Water level"
                                     f" {plant.water} is too high (max 10)\n")
            elif (not (plant.sun >= 2 and plant.sun <= 12)):
                if (plant.sun < 2):
                    raise PlantError(f"Error: Sunlight hours "
                                     f"{plant.sun} is too low (min 2)\n")
                else:
                    raise PlantError(f"Error: Sunlight hours "
                                     f"{plant.sun} is too high (max 12)\n")
            else:
                print(f"{plant.name}: healthy (water: "
                      f"{plant.water}, sun: {plant.water})")


class Plant:
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun

print("=== Garden Management System ===\n")
p1 = Plant("maticha", 10, 4)
p2 = Plant("dela7", 9, 2)

manager = GardenManager()
manager.add(p1)
manager.add(p1)

