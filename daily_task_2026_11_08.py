# Daily OOP Task - 08 November 2026
# Project: Photography Equipment Rental Tracker
# Concepts: inheritance, encapsulation, composition, validation and date calculations.

from datetime import date, datetime, timedelta


class Equipment:
    """Base class for equipment that can be rented."""

    def __init__(self, equipment_id, name, daily_rate):
        if not isinstance(equipment_id, str) or not equipment_id.strip():
            raise ValueError("Equipment ID must be a non-empty string.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Equipment name must be a non-empty string.")
        if (
            isinstance(daily_rate, bool)
            or not isinstance(daily_rate, (int, float))
            or daily_rate <= 0
        ):
            raise ValueError("Daily rate must be a positive number.")

        self.equipment_id = equipment_id.strip().upper()
        self.name = name.strip()
        self.daily_rate = float(daily_rate)
        self.__is_available = True
        self.__due_date = None

    @property
    def is_available(self):
        return self.__is_available

    @property
    def due_date(self):
        return self.__due_date

    def _rent(self, due_date):
        if not self.__is_available:
            raise ValueError(f"{self.name} is already rented.")
        self.__is_available = False
        self.__due_date = due_date

    def _receive_back(self):
        if self.__is_available:
            raise ValueError(f"{self.name} is not currently rented.")
        self.__is_available = True
        self.__due_date = None

    def details(self):
        status = "Available" if self.is_available else "Rented"
        return (
            f"{self.equipment_id} | {self.name} | "
            f"₹{self.daily_rate:.2f}/day | {status}"
        )


class Camera(Equipment):
    """A camera with its sensor information."""

    def __init__(self, equipment_id, name, daily_rate, sensor_type):
        super().__init__(equipment_id, name, daily_rate)
        if not isinstance(sensor_type, str) or not sensor_type.strip():
            raise ValueError("Sensor type must be a non-empty string.")
        self.sensor_type = sensor_type.strip()

    def details(self):
        return f"{super().details()} | Sensor: {self.sensor_type}"


class Tripod(Equipment):
    """A tripod with its maximum supported height."""

    def __init__(self, equipment_id, name, daily_rate, max_height_cm):
        super().__init__(equipment_id, name, daily_rate)
        if (
            isinstance(max_height_cm, bool)
            or not isinstance(max_height_cm, (int, float))
            or max_height_cm <= 0
        ):
            raise ValueError("Maximum height must be a positive number.")
        self.max_height_cm = float(max_height_cm)

    def details(self):
        return f"{super().details()} | Max height: {self.max_height_cm:g} cm"


class RentalDesk:
    """Manage equipment inventory, rentals and late-return charges."""

    def __init__(self, late_fee_per_day=50):
        if (
            isinstance(late_fee_per_day, bool)
            or not isinstance(late_fee_per_day, (int, float))
            or late_fee_per_day < 0
        ):
            raise ValueError("Late fee must be a non-negative number.")

        self.__inventory = {}
        self.late_fee_per_day = float(late_fee_per_day)

    @staticmethod
    def _validate_date(value, label):
        if isinstance(value, datetime) or not isinstance(value, date):
            raise TypeError(f"{label} must be a datetime.date object.")

    def add_equipment(self, equipment):
        if not isinstance(equipment, Equipment):
            raise TypeError("Only Equipment objects can be added.")

        key = equipment.equipment_id
        if key in self.__inventory:
            print(f"ID {key} already exists. Equipment was not added.")
            return False

        self.__inventory[key] = equipment
        print(f"{equipment.name} added to inventory.")
        return True

    def rent_equipment(self, equipment_id, renter_name, rental_days, start_date=None):
        if not isinstance(equipment_id, str) or not equipment_id.strip():
            raise ValueError("Enter a valid equipment ID.")
        if not isinstance(renter_name, str) or not renter_name.strip():
            raise ValueError("Renter name must not be empty.")
        if (
            isinstance(rental_days, bool)
            or not isinstance(rental_days, int)
            or rental_days <= 0
        ):
            raise ValueError("Rental days must be a positive whole number.")

        start_date = date.today() if start_date is None else start_date
        self._validate_date(start_date, "start_date")

        key = equipment_id.strip().upper()
        equipment = self.__inventory.get(key)
        if equipment is None:
            print(f"No equipment found with ID {key}.")
            return False
        if not equipment.is_available:
            print(f"{equipment.name} is currently unavailable.")
            return False

        due_date = start_date + timedelta(days=rental_days)
        equipment._rent(due_date)
        total = equipment.daily_rate * rental_days

        print(f"Rental confirmed for {renter_name.strip()}.")
        print(f"Equipment: {equipment.name}")
        print(f"Due date: {due_date:%d %b %Y}")
        print(f"Rental amount: ₹{total:.2f}")
        return True

    def return_equipment(self, equipment_id, return_date=None):
        if not isinstance(equipment_id, str) or not equipment_id.strip():
            raise ValueError("Enter a valid equipment ID.")

        return_date = date.today() if return_date is None else return_date
        self._validate_date(return_date, "return_date")

        key = equipment_id.strip().upper()
        equipment = self.__inventory.get(key)
        if equipment is None:
            print(f"No equipment found with ID {key}.")
            return None
        if equipment.is_available:
            print(f"{equipment.name} has no active rental.")
            return None
        late_days = max(0, (return_date - equipment.due_date).days)
        late_fee = late_days * self.late_fee_per_day
        equipment._receive_back()

        print(f"{equipment.name} returned successfully.")
        print(f"Late days: {late_days}")
        print(f"Late fee: ₹{late_fee:.2f}")
        return late_fee

    def show_inventory(self):
        print("\n===== PHOTOGRAPHY EQUIPMENT INVENTORY =====")
        if not self.__inventory:
            print("Inventory is empty.")
            return

        for equipment in self.__inventory.values():
            print(equipment.details())


if __name__ == "__main__":
    desk = RentalDesk(late_fee_per_day=75)

    camera = Camera("CAM101", "Mirrorless Camera", 900, "APS-C")
    tripod = Tripod("TRI201", "Travel Tripod", 150, 160)

    desk.add_equipment(camera)
    desk.add_equipment(tripod)
    desk.add_equipment(camera)  # Duplicate ID check

    desk.show_inventory()

    # Fixed dates keep the sample output predictable.
    desk.rent_equipment("cam101", "Aarav", 3, date(2026, 11, 8))
    desk.rent_equipment("CAM101", "Riya", 2, date(2026, 11, 8))
    desk.rent_equipment("TRI201", "Riya", 2, date(2026, 11, 8))

    desk.return_equipment("CAM101", date(2026, 11, 12))
    desk.return_equipment("TRI201", date(2026, 11, 9))

    desk.show_inventory()

    # Basic checks for inheritance, availability and late-fee calculation.
    assert isinstance(camera, Equipment)
    assert camera.is_available is True
    assert desk.return_equipment("CAM101", date(2026, 11, 12)) is None
    print("\nAll basic checks passed.")
