"""Daily OOP Task — Travel Booking Management System.

Practise inheritance, encapsulation, composition, properties, validation,
and Decimal-based price calculations.
"""

from decimal import Decimal, InvalidOperation


class TravelPackage:
    """Store details and pricing for a travel package."""

    def __init__(self, package_id, destination, duration_days, price):
        if not package_id.strip():
            raise ValueError("Package ID cannot be empty.")
        if not destination.strip():
            raise ValueError("Destination cannot be empty.")
        if not isinstance(duration_days, int) or duration_days <= 0:
            raise ValueError("Duration must be a positive whole number.")

        try:
            package_price = Decimal(str(price))
        except (InvalidOperation, ValueError):
            raise ValueError("Price must be a valid number.") from None

        if not package_price.is_finite() or package_price <= 0:
            raise ValueError("Price must be greater than zero.")

        self.package_id = package_id.strip().upper()
        self.destination = destination.strip().title()
        self.duration_days = duration_days
        self._price = package_price

    @property
    def price(self):
        """Return the package price without exposing internal state."""
        return self._price

    def calculate_total(self, travellers):
        if not isinstance(travellers, int) or travellers <= 0:
            raise ValueError("Number of travellers must be positive.")
        return self._price * travellers

    def package_details(self):
        return (
            f"{self.package_id}: {self.destination} | "
            f"{self.duration_days} days | ₹{self._price:.2f} per person"
        )


class PremiumPackage(TravelPackage):
    """A travel package that includes a premium service charge."""

    def __init__(self, package_id, destination, duration_days, price, service_fee):
        super().__init__(package_id, destination, duration_days, price)
        try:
            self._service_fee = Decimal(str(service_fee))
        except (InvalidOperation, ValueError):
            raise ValueError("Service fee must be a valid number.") from None

        if not self._service_fee.is_finite() or self._service_fee < 0:
            raise ValueError("Service fee cannot be negative.")

    def calculate_total(self, travellers):
        base_total = super().calculate_total(travellers)
        return base_total + self._service_fee * travellers

    def package_details(self):
        return (
            f"{super().package_details()} | "
            f"Premium service fee: ₹{self._service_fee:.2f} per person"
        )


class TravelBooking:
    """Represent a booking made for a travel package."""

    def __init__(self, booking_id, customer_name, package, travellers):
        if not booking_id.strip():
            raise ValueError("Booking ID cannot be empty.")
        if not customer_name.strip():
            raise ValueError("Customer name cannot be empty.")
        if not isinstance(package, TravelPackage):
            raise TypeError("A valid TravelPackage object is required.")
        if not isinstance(travellers, int) or travellers <= 0:
            raise ValueError("Number of travellers must be positive.")

        self.booking_id = booking_id.strip().upper()
        self.customer_name = customer_name.strip().title()
        self.package = package
        self.travellers = travellers
        self._status = "Confirmed"
        self._total_amount = package.calculate_total(travellers)

    @property
    def status(self):
        return self._status

    @property
    def total_amount(self):
        return self._total_amount

    def cancel(self):
        if self._status == "Cancelled":
            raise ValueError("This booking is already cancelled.")
        self._status = "Cancelled"

    def booking_details(self):
        return (
            f"Booking: {self.booking_id} | Customer: {self.customer_name} | "
            f"Destination: {self.package.destination} | "
            f"Travellers: {self.travellers} | "
            f"Total: ₹{self.total_amount:.2f} | Status: {self.status}"
        )


class TravelAgency:
    """Manage available packages and customer bookings."""

    def __init__(self, agency_name):
        if not agency_name.strip():
            raise ValueError("Agency name cannot be empty.")
        self.agency_name = agency_name.strip()
        self._packages = {}
        self._bookings = {}

    def add_package(self, package):
        if not isinstance(package, TravelPackage):
            raise TypeError("Only TravelPackage objects can be added.")
        if package.package_id in self._packages:
            raise ValueError("Package ID already exists.")
        self._packages[package.package_id] = package

    def create_booking(self, booking_id, customer_name, package_id, travellers):
        booking_key = booking_id.strip().upper()
        if booking_key in self._bookings:
            raise ValueError("Booking ID already exists.")
        if package_id.strip().upper() not in self._packages:
            raise ValueError("Package not found.")

        package = self._packages[package_id.strip().upper()]
        booking = TravelBooking(booking_key, customer_name, package, travellers)
        self._bookings[booking.booking_id] = booking
        return booking

    def cancel_booking(self, booking_id):
        key = booking_id.strip().upper()
        if key not in self._bookings:
            raise ValueError("Booking not found.")
        self._bookings[key].cancel()

    def show_packages(self):
        print(f"\nAvailable packages at {self.agency_name}")
        for package in self._packages.values():
            print("-", package.package_details())

    def show_bookings(self):
        print("\nBooking summary")
        if not self._bookings:
            print("No bookings available.")
            return
        for booking in self._bookings.values():
            print("-", booking.booking_details())


def main():
    agency = TravelAgency("Explore India Travels")

    agency.add_package(TravelPackage("TR101", "Goa", 4, "8500"))
    agency.add_package(TravelPackage("TR102", "Manali", 6, "12500"))
    agency.add_package(PremiumPackage("TR103", "Kashmir", 7, "18000", "2500"))

    agency.show_packages()

    booking1 = agency.create_booking("BK001", "Aarav Sharma", "TR101", 2)
    agency.create_booking("BK002", "Riya Patil", "TR103", 3)

    print("\nNew booking created:")
    print(booking1.booking_details())

    agency.cancel_booking("BK001")
    agency.show_bookings()


if __name__ == "__main__":
    main()
