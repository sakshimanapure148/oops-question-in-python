# Daily OOP Task - 04 November 2026
# Project: Smart Plant Care Tracker
# Concepts: classes, objects, encapsulation, validation, properties and methods.

from datetime import date


class Plant:
    """Store a plant's details and track its watering schedule."""

    def __init__(self, name, species, watering_interval):
        if not name.strip() or not species.strip():
            raise ValueError("Plant name and species cannot be empty.")
        if not isinstance(watering_interval, int) or watering_interval <= 0:
            raise ValueError("Watering interval must be a positive whole number.")

        self.name = name.strip()
        self.species = species.strip()
        self.watering_interval = watering_interval
        self.__last_watered = None
        self.__watering_count = 0

    @property
    def last_watered(self):
        """Return the last watering date without exposing private data."""
        return self.__last_watered

    @property
    def watering_count(self):
        return self.__watering_count

    def water(self, watering_date=None):
        """Record watering; an optional date makes the class easy to test."""
        watering_date = watering_date or date.today()

        if not isinstance(watering_date, date):
            raise TypeError("watering_date must be a date object.")
        if self.__last_watered and watering_date < self.__last_watered:
            raise ValueError("Watering date cannot be earlier than the last record.")

        self.__last_watered = watering_date
        self.__watering_count += 1
        print(f"{self.name} was watered on {watering_date:%d %b %Y}.")

    def days_since_watering(self, today=None):
        """Return None if the plant has never been watered."""
        if self.__last_watered is None:
            return None

        today = today or date.today()
        return (today - self.__last_watered).days

    def needs_water(self, today=None):
        days = self.days_since_watering(today)

        if days is None:
            return True

        return days >= self.watering_interval

    def display_status(self, today=None):
        days = self.days_since_watering(today)
        print(f"\nPlant: {self.name} ({self.species})")

        if days is None:
            print("Status: Watering not recorded yet.")
        else:
            print(f"Last watered: {self.last_watered:%d %b %Y}")
            print(f"Days since watering: {days}")

        if self.needs_water(today):
            print("Care reminder: This plant needs watering.")
        else:
            remaining = self.watering_interval - days
            print(f"Care reminder: Check again in {remaining} day(s).")

        print(f"Total watering records: {self.watering_count}")


class PlantCareTracker:
    """Manage multiple Plant objects."""

    def __init__(self):
        self.__plants = {}

    def add_plant(self, plant):
        if not isinstance(plant, Plant):
            raise TypeError("Only Plant objects can be added.")

        key = plant.name.lower()
        if key in self.__plants:
            print(f"{plant.name} is already registered.")
            return

        self.__plants[key] = plant
        print(f"{plant.name} added to the care tracker.")

    def water_plant(self, name, watering_date=None):
        plant = self.__plants.get(name.lower())
        if plant is None:
            print(f"No plant named '{name}' was found.")
            return

        plant.water(watering_date)

    def show_all_plants(self, today=None):
        if not self.__plants:
            print("No plants have been added yet.")
            return

        print("\n===== PLANT CARE DASHBOARD =====")
        for plant in self.__plants.values():
            plant.display_status(today)


if __name__ == "__main__":
    tracker = PlantCareTracker()

    money_plant = Plant("Money Plant", "Epipremnum aureum", 4)
    aloe_vera = Plant("Aloe Vera", "Succulent", 10)
    peace_lily = Plant("Peace Lily", "Spathiphyllum", 3)

    tracker.add_plant(money_plant)
    tracker.add_plant(aloe_vera)
    tracker.add_plant(peace_lily)
    tracker.add_plant(money_plant)  # Check duplicate registration

    # Fixed sample dates keep the demonstration output predictable.
    tracker.water_plant("Money Plant", date(2026, 11, 1))
    tracker.water_plant("Aloe Vera", date(2026, 10, 30))
    tracker.water_plant("Peace Lily", date(2026, 11, 3))
    tracker.water_plant("Unknown Plant")  # Check missing-plant handling

    tracker.show_all_plants(today=date(2026, 11, 4))
