class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __str__(self):
        return "Error adding plant: Plant name cannot be empty!\n"


class WaterError(GardenError):
    pass


class GardenManager:
    adding_process = 0

    def __init__(self, tank):
        self.plants = []
        self.tank = tank

    def add(self, object):
        try:
            if (self.adding_process == 0):
                print("Adding plants to garden...")
            if (object.name == ""):
                raise PlantError
            else:
                self.plants.append(object)
                print(f"Added {object.name} successfully")
                self.adding_process += 1
        except PlantError as e:
            print(e)

    def water_plants(self):
        print("Watering plants...")
        try:
            if self.tank <= 0:
                raise GardenError("Error: Not enough water in tank")
            print("Opening watering system")
            for plant in self.plants:
                if self.tank <= 0:
                    raise GardenError("Error: Not enough water in tank")
                plant.water += 1
                self.tank -= 1
                print(f"Watering {plant.name} - success")
        except GardenError as e:
            print(e)
        finally:
            print("Closing watering system\n")

    def check_health(self):
        try:
            print("Checking plant health...")
            for plant in self.plants:
                if (not (plant.water >= 1 and plant.water <= 10)):
                    if (plant.water < 1):
                        raise WaterError(f"Error: Water level {plant.water}"
                                         f"is too low(min 1) \n")
                    else:
                        raise WaterError(f"Error: Water level {plant.water}"
                                         f"is too high (max 10)\n")
                elif (not (plant.sun >= 2 and plant.sun <= 12)):
                    if (plant.sun < 2):
                        raise GardenError(f"Error: Sunlight hours "
                                          f"{plant.sun} is too low (min 2)\n")
                    else:
                        raise GardenError(f"Error: Sunlight hours {plant.sun}"
                                          f"is too high (max 12)\n")
                else:
                    print(f"{plant.name}: healthy (water: "
                          f"{plant.water}, sun: {plant.sun})")
        except Exception as e:
            print(e)
        finally:
            print("Checking plant health systeme closed")


class Plant:
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun


def systeme():
    print("=== Garden Management System ===\n")
    p1 = Plant("maticha", 0, 4)
    p2 = Plant("dela7", -10, 12)

    manager = GardenManager(100)
    manager.add(p1)
    manager.add(p2)
    print()
    manager.water_plants()
    print()
    manager.check_health()
    print()

    try:
        print("Testing error recovery...")
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...\n")
    print("Garden management system test complete!")


systeme()
