"""Tours and Travels Management System
OOP practice: classes, objects, inheritance, encapsulation and composition.
"""

from decimal import Decimal, InvalidOperation


class TourPackage:
    """Stores information about one tour package."""

    def __init__(self, package_id, destination, days, price_per_person):
        if not package_id.strip():
            raise ValueError("Package ID cannot be empty.")
        if not destination.strip():
            raise ValueError("Destination cannot be empty.")
        if not isinstance(days, int) or days <= 0:
            raise ValueError("Tour days must be a positive whole number.")

        try:
            price = Decimal(str(price_per_person))
        except (InvalidOperation, ValueError):
            raise ValueError("Price must be a valid number.") from None

        if not price.is_finite() or price <= 0:
            raise ValueError("Price must be greater than zero.")

        self.package_id = package_id.strip().upper()
        self.destination = destination.strip().title()
        self.days = days
        self._price_per_person = price

    @property
    def price_per_person(self):
        return self._price_per_person

    def calculate_cost(self, travellers):
        if not isinstance(travellers, int) or travellers <= 0:
            raise ValueError("Travellers must be a positive whole number.")
        return self.price_per_person * travellers

    def show_details(self):
        return (
            f"{self.package_id} | {self.destination} | "
            f"{self.days} days | Rs. {self.price_per_person:.2f} per person"
        )


class PremiumTourPackage(TourPackage):
    """Tour package with an additional per-person service charge."""

    def __init__(self, package_id, destination, days, price_per_person, service_charge):
        super().__init__(package_id, destination, days, price_per_person)
        try:
            charge = Decimal(str(service_charge))
        except (InvalidOperation, ValueError):
            raise ValueError("Service charge must be a valid number.") from None

        if not charge.is_finite() or charge < 0:
            raise ValueError("Service charge cannot be negative.")
        self._service_charge = charge

    def calculate_cost(self, travellers):
        return super().calculate_cost(travellers) + self._service_charge * travellers

    def show_details(self):
        return (
            f"{super().show_details()} | "
            f"Premium service: Rs. {self._service_charge:.2f} per person"
        )


class Booking:
    """Stores one customer's tour booking."""

    def __init__(self, booking_id, customer_name, package, travellers):
        if not booking_id.strip():
            raise ValueError("Booking ID cannot be empty.")
        if not customer_name.strip():
            raise ValueError("Customer name cannot be empty.")
        if not isinstance(package, TourPackage):
            raise TypeError("Please select a valid tour package.")
        if not isinstance(travellers, int) or travellers <= 0:
            raise ValueError("Travellers must be a positive whole number.")

        self.booking_id = booking_id.strip().upper()
        self.customer_name = customer_name.strip().title()
        self.package = package
        self.travellers = travellers
        self._total_amount = package.calculate_cost(travellers)
        self._status = "Confirmed"

    @property
    def total_amount(self):
        return self._total_amount

    @property
    def status(self):
        return self._status

    def cancel(self):
        if self._status == "Cancelled":
            raise ValueError("This booking is already cancelled.")
        self._status = "Cancelled"

    def show_booking(self):
        return (
            f"{self.booking_id} | {self.customer_name} | "
            f"{self.package.destination} | {self.travellers} traveller(s) | "
            f"Rs. {self.total_amount:.2f} | {self.status}"
        )


class TravelAgency:
    """Manages tour packages and customer bookings."""

    def __init__(self, agency_name):
        if not agency_name.strip():
            raise ValueError("Agency name cannot be empty.")
        self.agency_name = agency_name.strip()
        self._packages = {}
        self._bookings = {}

    def add_package(self, package):
        if not isinstance(package, TourPackage):
            raise TypeError("Only TourPackage objects can be added.")
        if package.package_id in self._packages:
            raise ValueError("This package ID already exists.")
        self._packages[package.package_id] = package

    def create_booking(self, booking_id, customer_name, package_id, travellers):
        booking_key = booking_id.strip().upper()
        package_key = package_id.strip().upper()

        if booking_key in self._bookings:
            raise ValueError("This booking ID already exists.")
        if package_key not in self._packages:
            raise ValueError("Tour package not found.")

        booking = Booking(
            booking_key, customer_name, self._packages[package_key], travellers
        )
        self._bookings[booking_key] = booking
        return booking

    def cancel_booking(self, booking_id):
        key = booking_id.strip().upper()
        if key not in self._bookings:
            raise ValueError("Booking not found.")
        self._bookings[key].cancel()

    def show_packages(self):
        print(f"\n--- {self.agency_name}: Available Tour Packages ---")
        for package in self._packages.values():
            print(package.show_details())

    def show_bookings(self):
        print("\n--- Customer Bookings ---")
        if not self._bookings:
            print("No bookings found.")
            return
        for booking in self._bookings.values():
            print(booking.show_booking())


def main():
    agency = TravelAgency("Explore India Tours and Travels")

    agency.add_package(TourPackage("T101", "Goa", 4, "8500"))
    agency.add_package(TourPackage("T102", "Manali", 6, "12500"))
    agency.add_package(PremiumTourPackage("T103", "Kashmir", 7, "18000", "2500"))

    agency.show_packages()

    first_booking = agency.create_booking("B001", "Aarav Sharma", "T101", 2)
    agency.create_booking("B002", "Riya Patil", "T103", 3)

    print("\nBooking created:")
    print(first_booking.show_booking())

    agency.cancel_booking("B001")
    agency.show_bookings()


if __name__ == "__main__":
    main()
