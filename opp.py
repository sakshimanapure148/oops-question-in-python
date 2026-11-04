"""OOP fundamentals: inheritance, overriding and polymorphism."""


class Vehicle:
    """Base class shared by different types of vehicles."""

    def __init__(self, brand):
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Brand cannot be empty.")
        self.brand = brand.strip()

    def start(self):
        print(f"{self.brand} vehicle is starting.")

    def move(self):
        print("The vehicle is moving.")


class Car(Vehicle):
    """A car inherits common vehicle behaviour."""

    def __init__(self, brand, fuel_type):
        super().__init__(brand)
        if not isinstance(fuel_type, str) or not fuel_type.strip():
            raise ValueError("Fuel type cannot be empty.")
        self.fuel_type = fuel_type.strip()

    def move(self):
        print(f"{self.brand} car is driving.")

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Fuel type: {self.fuel_type}")


class Bicycle(Vehicle):
    """A bicycle provides its own move() implementation."""

    def move(self):
        print(f"{self.brand} bicycle is being pedalled.")


def demonstrate_polymorphism(vehicles):
    for vehicle in vehicles:
        vehicle.move()


if __name__ == "__main__":
    car = Car("Toyota", "Petrol")
    bicycle = Bicycle("Firefox")

    print("=== CAR DETAILS ===")
    car.show_details()
    car.start()

    print("\n=== POLYMORPHISM DEMO ===")
    demonstrate_polymorphism([car, bicycle])
