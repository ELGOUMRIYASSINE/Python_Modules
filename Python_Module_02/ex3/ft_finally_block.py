class Error(Exception):
    pass


def water_plants(plant_list):

    print("Opening watering system")
    for plant in plant_list:
        if plant and isinstance(plant, str):
            print(f"Watering {plant}")
        else:
            raise Error


def test_watering_system():
    good_list = ["tomato", "jelbana", "batata", "dela7"]
    print("=== Garden Watering System ===")
    print("Testing normal watering...")
    try:
        water_plants(good_list)
        print("Watering completed successfully!")
    except Error:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)\n")

    print("Testing normal watering...")

    good_list = ["tomato", 120, "batata", "dela7"]
    try:
        water_plants(good_list)
        print("Watering completed successfully!")
    except Error:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


test_watering_system()
