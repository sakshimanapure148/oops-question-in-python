"""Daily OOP Task - 11 November 2026: Smart Home Energy Monitor.

Create devices, switch them on or off, and calculate their electricity use.
This project practises inheritance, encapsulation, polymorphism and validation.
"""


class SmartDevice:
    """Base class for an electrical device in a smart home."""

    def __init__(self, device_id, name, power_rating):
        if not isinstance(device_id, str) or not device_id.strip():
            raise ValueError("Device ID cannot be empty.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Device name cannot be empty.")
        if not isinstance(power_rating, (int, float)) or isinstance(power_rating, bool):
            raise TypeError("Power rating must be a number.")
        if power_rating <= 0:
            raise ValueError("Power rating must be greater than zero.")

        self.device_id = device_id.strip().upper()
        self.name = name.strip()
        self.power_rating = float(power_rating)
        self.__is_on = False

    @property
    def is_on(self):
        """Read-only power state."""
        return self.__is_on

    def switch_on(self):
        self.__is_on = True

    def switch_off(self):
        self.__is_on = False

    def energy_used(self, hours):
        """Return energy consumption in kilowatt-hours."""
        if not isinstance(hours, (int, float)) or isinstance(hours, bool):
            raise TypeError("Hours must be a number.")
        if hours < 0:
            raise ValueError("Hours cannot be negative.")
        if not self.__is_on:
            return 0.0
        return self.power_rating * hours / 1000

    def device_type(self):
        return "General Device"

    def display(self, hours):
        print(
            f"{self.device_id} | {self.name} | {self.device_type()} | "
            f"{'ON' if self.is_on else 'OFF'} | "
            f"{self.energy_used(hours):.3f} kWh"
        )


class SmartLight(SmartDevice):
    def device_type(self):
        return "Smart Light"


class SmartFan(SmartDevice):
    def device_type(self):
        return "Smart Fan"


class SmartAirConditioner(SmartDevice):
    def device_type(self):
        return "Smart AC"


class SmartHome:
    """Stores devices and calculates household energy usage."""

    def __init__(self, home_name):
        if not isinstance(home_name, str) or not home_name.strip():
            raise ValueError("Home name cannot be empty.")
        self.home_name = home_name.strip()
        self._devices = {}

    def add_device(self, device):
        if not isinstance(device, SmartDevice):
            raise TypeError("Only SmartDevice objects can be added.")
        if device.device_id in self._devices:
            raise ValueError("A device with this ID already exists.")
        self._devices[device.device_id] = device

    def find_device(self, device_id):
        return self._devices.get(device_id.strip().upper())

    def show_devices(self, hours):
        print(f"\n--- {self.home_name}: Device Report ---")
        for device in self._devices.values():
            device.display(hours)

    def total_energy(self, hours):
        return sum(device.energy_used(hours) for device in self._devices.values())

    def switch_all_off(self):
        for device in self._devices.values():
            device.switch_off()


def main():
    home = SmartHome("Sakshi's Smart Home")

    devices = [
        SmartLight("L101", "Living Room Light", 12),
        SmartFan("F201", "Bedroom Fan", 75),
        SmartAirConditioner("AC301", "Hall AC", 1500),
    ]

    for device in devices:
        home.add_device(device)

    # Switch on two devices; the AC remains off.
    devices[0].switch_on()
    devices[1].switch_on()

    home.show_devices(hours=5)
    print(f"Total energy for 5 hours: {home.total_energy(5):.3f} kWh")

    # Demonstrate searching and encapsulated state updates.
    found = home.find_device("f201")
    if found:
        print(f"\nFound: {found.name} is {'ON' if found.is_on else 'OFF'}.")

    # Demonstrate validation and duplicate prevention.
    try:
        home.add_device(SmartLight("L101", "Extra Light", 10))
    except ValueError as error:
        print(f"Duplicate check passed: {error}")

    try:
        devices[0].energy_used(-2)
    except ValueError as error:
        print(f"Hours validation passed: {error}")

    home.switch_all_off()
    assert home.total_energy(5) == 0
    print("All checks passed successfully.")


if __name__ == "__main__":
    main()
