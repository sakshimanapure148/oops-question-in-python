"""Daily OOP Task - 15 November 2026: Smart Home Energy Monitor.

Register smart devices, control their power state and estimate daily energy use.
Concepts: inheritance, polymorphism, encapsulation, composition and validation.
"""


class SmartDevice:
    """Base class for a controllable home device."""

    def __init__(self, device_id, name, power_watts):
        if not isinstance(device_id, str) or not device_id.strip():
            raise ValueError("Device ID cannot be empty.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Device name cannot be empty.")
        if isinstance(power_watts, bool) or not isinstance(power_watts, (int, float)):
            raise TypeError("Power rating must be a number.")
        if power_watts <= 0:
            raise ValueError("Power rating must be greater than zero.")

        self.device_id = device_id.strip().upper()
        self.name = name.strip().title()
        self.power_watts = float(power_watts)
        self.__is_on = False

    @property
    def is_on(self):
        """Read-only power state."""
        return self.__is_on

    def turn_on(self):
        if self.__is_on:
            raise ValueError(f"{self.name} is already on.")
        self.__is_on = True

    def turn_off(self):
        if not self.__is_on:
            raise ValueError(f"{self.name} is already off.")
        self.__is_on = False

    def estimate_daily_energy(self, hours):
        """Estimate energy in kWh for the supplied number of hours."""
        if isinstance(hours, bool) or not isinstance(hours, (int, float)):
            raise TypeError("Usage hours must be a number.")
        if not 0 <= hours <= 24:
            raise ValueError("Usage hours must be between 0 and 24.")
        if not self.is_on:
            return 0.0
        return self.power_watts * hours / 1000

    def details(self):
        state = "ON" if self.is_on else "OFF"
        return f"{self.device_id} | {self.name} | {self.power_watts:.0f} W | {state}"


class SmartLight(SmartDevice):
    """A smart light with adjustable brightness."""

    def __init__(self, device_id, name, power_watts, brightness=100):
        super().__init__(device_id, name, power_watts)
        self.set_brightness(brightness)

    def set_brightness(self, brightness):
        if isinstance(brightness, bool) or not isinstance(brightness, int):
            raise TypeError("Brightness must be an integer.")
        if not 1 <= brightness <= 100:
            raise ValueError("Brightness must be between 1 and 100.")
        self.__brightness = brightness

    @property
    def brightness(self):
        return self.__brightness

    def estimate_daily_energy(self, hours):
        base_energy = super().estimate_daily_energy(hours)
        return base_energy * self.brightness / 100

    def details(self):
        return f"{super().details()} | Brightness: {self.brightness}%"


class SmartFan(SmartDevice):
    """A smart fan with three speed settings."""

    def __init__(self, device_id, name, power_watts, speed=1):
        super().__init__(device_id, name, power_watts)
        self.set_speed(speed)

    def set_speed(self, speed):
        if isinstance(speed, bool) or not isinstance(speed, int):
            raise TypeError("Fan speed must be an integer.")
        if speed not in (1, 2, 3):
            raise ValueError("Fan speed must be 1, 2 or 3.")
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    def estimate_daily_energy(self, hours):
        speed_factor = {1: 0.5, 2: 0.75, 3: 1.0}[self.speed]
        return super().estimate_daily_energy(hours) * speed_factor

    def details(self):
        return f"{super().details()} | Speed: {self.speed}"


class SmartHome:
    """Manage smart devices using composition."""

    def __init__(self, home_name):
        if not isinstance(home_name, str) or not home_name.strip():
            raise ValueError("Home name cannot be empty.")
        self.home_name = home_name.strip()
        self.__devices = {}

    def add_device(self, device):
        if not isinstance(device, SmartDevice):
            raise TypeError("Only SmartDevice objects can be registered.")
        if device.device_id in self.__devices:
            raise ValueError("A device with this ID already exists.")
        self.__devices[device.device_id] = device

    def find_device(self, device_id):
        if not isinstance(device_id, str) or not device_id.strip():
            raise ValueError("Device ID cannot be empty.")
        return self.__devices.get(device_id.strip().upper())

    def switch_device(self, device_id, turn_on):
        device = self.find_device(device_id)
        if device is None:
            raise LookupError("Device was not found.")
        if not isinstance(turn_on, bool):
            raise TypeError("turn_on must be True or False.")
        if turn_on:
            device.turn_on()
        else:
            device.turn_off()

    @property
    def total_devices(self):
        return len(self.__devices)

    @property
    def active_devices(self):
        return sum(device.is_on for device in self.__devices.values())

    def energy_report(self, usage_hours):
        """Use polymorphism to calculate each device's energy estimate."""
        print(f"\\n===== Energy Report: {self.home_name} =====")
        total_kwh = 0.0
        for device in self.__devices.values():
            energy = device.estimate_daily_energy(usage_hours)
            total_kwh += energy
            print(f"{device.details()} | Estimated energy: {energy:.3f} kWh")
        print(f"Active devices: {self.active_devices}/{self.total_devices}")
        print(f"Estimated total: {total_kwh:.3f} kWh")
        return total_kwh


def main():
    home = SmartHome("Sakshi's Smart Home")

    living_room_light = SmartLight("L101", "Living Room Light", 12, 75)
    bedroom_fan = SmartFan("F201", "Bedroom Fan", 60, 2)
    study_light = SmartLight("L102", "Study Light", 9, 100)

    for device in (living_room_light, bedroom_fan, study_light):
        home.add_device(device)

    home.switch_device("l101", True)
    home.switch_device("F201", True)
    home.switch_device("L102", True)

    # Each subclass calculates energy according to its own settings.
    total = home.energy_report(5)

    print("\\nChanging fan speed and light brightness...")
    bedroom_fan.set_speed(3)
    living_room_light.set_brightness(50)
    updated_total = home.energy_report(5)

    # Validation and state-management checks.
    try:
        home.add_device(SmartLight("L101", "Duplicate Light", 10))
    except ValueError as error:
        print("\\nDuplicate check passed:", error)

    try:
        study_light.set_brightness(120)
    except ValueError as error:
        print("Brightness validation passed:", error)

    try:
        home.switch_device("UNKNOWN", True)
    except LookupError as error:
        print("Missing-device check passed:", error)

    assert home.total_devices == 3
    assert home.active_devices == 3
    assert round(total, 3) == 0.297
    assert round(updated_total, 3) == 0.24
    assert home.find_device("l101") is living_room_light
    assert home.find_device("missing") is None
    print("\\nAll smart home energy checks passed successfully.")


if __name__ == "__main__":
    main()
