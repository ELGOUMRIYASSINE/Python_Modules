#!/usr/bin/python3
class SecurePlant:
    """
    A secure plant class that protects its data from invalid changes.
    Uses private attributes (double underscore) to prevent direct access.
    This ensures height and age can only be changed through safe methods.
    """

    def __init__(self, name, height, age):
        """
        Creates a new secure plant with protected height and age.
        The height and age are stored privately to
        prevent unauthorized changes.
        """
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {name}")

    def show_data(self):
        """
        Displays all the plant's current information.
        Shows name, height, and age in a readable format.
        """
        print(f"Current plant: {self.name} ({self.__height}cm,"
              f"{self.__age} days)")

    def get_height(self):
        """
        Returns the plant's current height.
        This is a safe way to read the private height value.
        """
        return (self.__height)

    def set_height(self, new_height):
        """
        Updates the plant's height with validation.
        Rejects negative values to prevent invalid data.
        Only accepts positive heights for security.
        """
        if (new_height < 0):
            print(f"Invalid operation attempted: height "
                  f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")

    def get_age(self):
        """
        Returns the plant's current age.
        This is a safe way to read the private age value.
        """
        return (self.__age)

    def set_age(self, new_age):
        """
        Updates the plant's age with validation.
        Rejects negative values to prevent invalid data.
        Only accepts positive ages for security.
        """
        if (new_age < 0):
            print(f"Invalid operation attempted: age {new_age}"
                  f"days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")

# print("=== Garden Security System ===")
# Sp1 = SecurePlant("Dela7",10,29)
# Sp1.set_height(25)
# Sp1.set_age(20)
# print()
# Sp1.set_height(-5)
# print()
# Sp1.show_data()
