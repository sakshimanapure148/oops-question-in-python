"""Smart Home Energy Monitor
=========================

Daily OOP practice project — 15 November 2026.

Demonstrates inheritance, encapsulation, polymorphism, composition,
input validation and basic runtime assertions.
"""

from __future__ import annotations

from typing import Dict, Optional


class SmartDevice:
    """Base model for a controllable smart-home device."""

    def __init__(self, device_id: str, name: str, power_watts: float) -> None:
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
    def is_on(self) -> bool:
        """Return the current power state without exposing internal storage."""
        return self.__is_on

    def turn_on(self) -> None:
        """Switch the device on."""
        if self.__is_on:
            raise ValueError(f"{self.name} is already on.")
        self.__is_on = True

    def turn_off(self) -> None:
        """Switch the device off."""
        if not self.__is_on:
            raise ValueError(f"{self.name} is already off.")
        self.__is_on = False

    def estimate_daily_energy(self, hours: float) -> float:
        """Estimate consumption in kWh for up to 24 hours of use."""
        if isinstance(hours, bool) or not isinstance(hours, (int, float)):
            raise TypeError("Usage hours must be a number.")
        if not 0 <= hours <= 24:
            raise ValueError("Usage hours must be between 0 and 24.")
        if not self.is_on:
            return 0.0
        return self.power_watts * hours / 1000

    def details(self) -> str:
        """Return a concise, human-readable device summary."""
        state = "ON" if self.is_on else "OFF"
        return f"{self.device_id} | {self.name} | {self.power_watts:.0f} W | {state}"


class SmartLight(SmartDevice):
    """Smart light with adjustable brightness."""

    def __init__(
        self, device_id: str, name: str, power_watts: float, brightness: int = 100
    ) -> None:
        super().__init__(device_id, name, power_watts)
        self.set_brightness(brightness)

    def set_brightness(self, brightness: int) -> None:
        """Set brightness to a whole-number percentage from 1 to 100."""
        if isinstance(brightness, bool) or not isinstance(brightness, int):
            raise TypeError("Brightness must be an integer.")
        if not 1 <= brightness <= 100:
            raise ValueError("Brightness must be between 1 and 100.")
        self.__brightness = brightness

    @property
    def brightness(self) -> int:
        """Return the configured brightness percentage."""
        return self.__brightness

    def estimate_daily_energy(self, hours: float) -> float:
        base_energy = super().estimate_daily_energy(hours)
        return base_energy * self.brightness / 100

    def details(self) -> str:
        return f"{super().details()} | Brightness: {self.brightness}%"


class SmartFan(SmartDevice):
    """Smart fan with three speed settings."""

    SPEED_FACTORS = {1: 0.50, 2: 0.75, 3: 1.00}

    def __init__(
        self, device_id: str, name: str, power_watts: float, speed: int = 1
    ) -> None:
        super().__init__(device_id, name, power_watts)
        self.set_speed(speed)

    def set_speed(self, speed: int) -> None:
        """Set fan speed to level 1, 2 or 3."""
        if isinstance(speed, bool) or not isinstance(speed, int):
            raise TypeError("Fan speed must be an integer.")
        if speed not in self.SPEED_FACTORS:
            raise ValueError("Fan speed must be 1, 2 or 3.")
        self.__speed = speed

    @property
    def speed(self) -> int:
        """Return the current fan speed level."""
        return self.__speed

    def estimate_daily_energy(self, hours: float) -> float:
        base_energy = super().estimate_daily_energy(hours)
        return base_energy * self.SPEED_FACTORS[self.speed]

    def details(self) -> str:
        return f"{super().details()} | Speed: {self.speed}"


class SmartHome:
    """Register and manage smart devices through object composition."""

    def __init__(self, home_name: str) -> None:
        if not isinstance(home_name, str) or not home_name.strip():
            raise ValueError("Home name cannot be empty.")
        self.home_name = home_name.strip()
        self.__devices: Dict[str, SmartDevice] = {}

    def add_device(self, device: SmartDevice) -> None:
        """Register a device, rejecting unsupported objects and duplicate IDs."""
        if not isinstance(device, SmartDevice):
            raise TypeError("Only SmartDevice objects can be registered.")
        if device.device_id in self.__devices:
            raise ValueError(f"Device ID '{device.device_id}' is already registered.")
        self.__devices[device.device_id] = device

    def find_device(self, device_id: str) -> Optional[SmartDevice]:
        """Find a device by ID; return None when no match exists."""
        if not isinstance(device_id, str) or not device_id.strip():
            raise ValueError("Device ID cannot be empty.")
        return self.__devices.get(device_id.strip().upper())

    def switch_device(self, device_id: str, turn_on: bool) -> None:
        """Change a registered device's power state."""
        device = self.find_device(device_id)
        if device is None:
            raise LookupError(f"Device '{device_id}' was not found.")
        if not isinstance(turn_on, bool):
            raise TypeError("turn_on must be True or False.")
        device.turn_on() if turn_on else device.turn_off()

    @property
    def total_devices(self) -> int:
        return len(self.__devices)

    @property
    def active_devices(self) -> int:
        return sum(device.is_on for device in self.__devices.values())

    def energy_report(self, usage_hours: float) -> float:
        """Print a polymorphic energy report and return total estimated kWh."""
        if isinstance(usage_hours, bool) or not isinstance(usage_hours, (int, float)):
            raise TypeError("Usage hours must be a number.")
        if not 0 <= usage_hours <= 24:
            raise ValueError("Usage hours must be between 0 and 24.")

        print(f"\n{' SMART HOME ENERGY REPORT ':=^72}")
        print(f"Home: {self.home_name} | Usage period: {usage_hours:g} hour(s)")
        print("-" * 72)

        total_kwh = 0.0
        for device in self.__devices.values():
            energy = device.estimate_daily_energy(usage_hours)
            total_kwh += energy
            print(f"{device.details()} | Estimated use: {energy:.3f} kWh")

        print("-" * 72)
        print(f"Active devices : {self.active_devices}/{self.total_devices}")
        print(f"Total estimate: {total_kwh:.3f} kWh")
        print("=" * 72)
        return total_kwh


def main() -> None:
    """Run the sample smart-home scenario and its validation checks."""
    home = SmartHome("Sakshi's Smart Home")

    living_room_light = SmartLight("L101", "Living Room Light", 12, 75)
    bedroom_fan = SmartFan("F201", "Bedroom Fan", 60, 2)
    study_light = SmartLight("L102", "Study Light", 9, 100)

    for device in (living_room_light, bedroom_fan, study_light):
        home.add_device(device)

    for device_id in ("L101", "F201", "L102"):
        home.switch_device(device_id, True)

    initial_total = home.energy_report(5)

    print("\nUpdating device settings...")
    bedroom_fan.set_speed(3)
    living_room_light.set_brightness(50)
    updated_total = home.energy_report(5)

    # Demonstrate clear validation errors for common invalid operations.
    validation_checks = (
        (
            "Duplicate registration",
            lambda: home.add_device(SmartLight("L101", "Duplicate Light", 10)),
            ValueError,
        ),
        ("Invalid brightness", lambda: study_light.set_brightness(120), ValueError),
        ("Unknown device", lambda: home.switch_device("UNKNOWN", True), LookupError),
    )

    for label, operation, expected_error in validation_checks:
        try:
            operation()
        except expected_error as error:
            print(f"[PASS] {label}: {error}")
        else:
            raise AssertionError(f"{label} validation did not raise an error.")

    assert home.total_devices == 3
    assert home.active_devices == 3
    assert round(initial_total, 3) == 0.315
    assert round(updated_total, 3) == 0.375
    assert home.find_device("l101") is living_room_light
    assert home.find_device("missing") is None

    print("\n[PASS] All smart-home energy checks completed successfully.")


if __name__ == "__main__":
    main()
