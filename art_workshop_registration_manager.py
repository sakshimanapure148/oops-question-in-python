"""Art Workshop Registration Manager
OOP practice: inheritance, encapsulation, polymorphism, composition,
validation, Decimal calculations and exception handling.

Run:
    python art_workshop_registration_manager.py
"""

from decimal import Decimal, InvalidOperation


class Workshop:
    """Base class containing common workshop information."""

    def __init__(self, workshop_id, title, base_fee, capacity):
        workshop_id = workshop_id.strip().upper()
        title = title.strip()
        if not workshop_id:
            raise ValueError("Workshop ID cannot be empty.")
        if not title:
            raise ValueError("Workshop title cannot be empty.")
        if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive whole number.")

        try:
            fee = Decimal(str(base_fee))
        except (InvalidOperation, ValueError):
            raise ValueError("Base fee must be a valid number.") from None
        if not fee.is_finite() or fee < 0:
            raise ValueError("Base fee cannot be negative.")

        self.workshop_id = workshop_id
        self.title = title
        self._base_fee = fee
        self.capacity = capacity
        self._registrations = {}

    @property
    def base_fee(self):
        """Return the base fee without exposing mutable internal state."""
        return self._base_fee

    @property
    def available_seats(self):
        return self.capacity - len(self._registrations)

    def calculate_fee(self):
        """Return the fee; subclasses can customize this calculation."""
        return self.base_fee

    def add_registration(self, registration):
        if registration.participant.participant_id in self._registrations:
            raise ValueError("This participant is already registered.")
        if self.available_seats <= 0:
            raise ValueError("No seats are available for this workshop.")
        self._registrations[registration.participant.participant_id] = registration

    def remove_registration(self, participant_id):
        key = participant_id.strip().upper()
        if key not in self._registrations:
            raise ValueError("Registration not found.")
        del self._registrations[key]

    def show_details(self):
        return (
            f"{self.workshop_id} | {self.title} | "
            f"Fee: Rs. {self.calculate_fee():.2f} | "
            f"Seats: {self.available_seats}/{self.capacity}"
        )


class OnlineWorkshop(Workshop):
    """Workshop delivered online with a platform fee."""

    def __init__(self, workshop_id, title, base_fee, capacity, platform_fee):
        super().__init__(workshop_id, title, base_fee, capacity)
        self._platform_fee = self._validate_extra_fee(platform_fee)

    @staticmethod
    def _validate_extra_fee(value):
        try:
            fee = Decimal(str(value))
        except (InvalidOperation, ValueError):
            raise ValueError("Additional fee must be a valid number.") from None
        if not fee.is_finite() or fee < 0:
            raise ValueError("Additional fee cannot be negative.")
        return fee

    def calculate_fee(self):
        return super().calculate_fee() + self._platform_fee


class InPersonWorkshop(Workshop):
    """In-person workshop with a venue-material charge."""

    def __init__(self, workshop_id, title, base_fee, capacity, material_fee):
        super().__init__(workshop_id, title, base_fee, capacity)
        self._material_fee = self._validate_extra_fee(material_fee)

    @staticmethod
    def _validate_extra_fee(value):
        try:
            fee = Decimal(str(value))
        except (InvalidOperation, ValueError):
            raise ValueError("Material fee must be a valid number.") from None
        if not fee.is_finite() or fee < 0:
            raise ValueError("Material fee cannot be negative.")
        return fee

    def calculate_fee(self):
        return super().calculate_fee() + self._material_fee


class Participant:
    """Stores the details of one workshop participant."""

    def __init__(self, participant_id, name, email):
        participant_id = participant_id.strip().upper()
        name = name.strip()
        email = email.strip().lower()

        if not participant_id:
            raise ValueError("Participant ID cannot be empty.")
        if not name:
            raise ValueError("Participant name cannot be empty.")
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Enter a valid email address.")

        self.participant_id = participant_id
        self.name = name.title()
        self.email = email


class Registration:
    """Connects a participant with a workshop and stores payment details."""

    def __init__(self, registration_id, participant, workshop):
        registration_id = registration_id.strip().upper()
        if not registration_id:
            raise ValueError("Registration ID cannot be empty.")
        if not isinstance(participant, Participant):
            raise TypeError("A valid Participant object is required.")
        if not isinstance(workshop, Workshop):
            raise TypeError("A valid Workshop object is required.")

        self.registration_id = registration_id
        self.participant = participant
        self.workshop = workshop
        self._amount_paid = workshop.calculate_fee()
        self._status = "Confirmed"

    @property
    def amount_paid(self):
        return self._amount_paid

    @property
    def status(self):
        return self._status

    def cancel(self):
        if self._status == "Cancelled":
            raise ValueError("This registration is already cancelled.")
        self.workshop.remove_registration(self.participant.participant_id)
        self._status = "Cancelled"

    def summary(self):
        return (
            f"{self.registration_id} | {self.participant.name} | "
            f"{self.workshop.title} | Rs. {self.amount_paid:.2f} | "
            f"{self.status}"
        )


class WorkshopManager:
    """Manages workshops, participants and registrations."""

    def __init__(self, manager_name):
        manager_name = manager_name.strip()
        if not manager_name:
            raise ValueError("Manager name cannot be empty.")
        self.manager_name = manager_name
        self._workshops = {}
        self._participants = {}
        self._registrations = {}

    def add_workshop(self, workshop):
        if not isinstance(workshop, Workshop):
            raise TypeError("Only Workshop objects can be added.")
        if workshop.workshop_id in self._workshops:
            raise ValueError("Workshop ID already exists.")
        self._workshops[workshop.workshop_id] = workshop

    def register_participant(self, participant):
        if not isinstance(participant, Participant):
            raise TypeError("Only Participant objects can be registered.")
        if participant.participant_id in self._participants:
            raise ValueError("Participant ID already exists.")
        self._participants[participant.participant_id] = participant

    def enroll(self, registration_id, participant_id, workshop_id):
        reg_key = registration_id.strip().upper()
        person_key = participant_id.strip().upper()
        workshop_key = workshop_id.strip().upper()

        if not reg_key:
            raise ValueError("Registration ID cannot be empty.")
        if reg_key in self._registrations:
            raise ValueError("Registration ID already exists.")
        if person_key not in self._participants:
            raise ValueError("Participant not found.")
        if workshop_key not in self._workshops:
            raise ValueError("Workshop not found.")

        participant = self._participants[person_key]
        workshop = self._workshops[workshop_key]
        registration = Registration(reg_key, participant, workshop)
        workshop.add_registration(registration)
        self._registrations[reg_key] = registration
        return registration

    def cancel_registration(self, registration_id):
        key = registration_id.strip().upper()
        if key not in self._registrations:
            raise ValueError("Registration not found.")
        self._registrations[key].cancel()

    def show_workshops(self):
        print("\n--- Available Workshops ---")
        for workshop in self._workshops.values():
            print(workshop.show_details())

    def show_registrations(self):
        print("\n--- Registration Report ---")
        if not self._registrations:
            print("No registrations found.")
            return
        for registration in self._registrations.values():
            print(registration.summary())


def main():
    manager = WorkshopManager("Creative Skills Studio")

    manager.add_workshop(
        OnlineWorkshop("W101", "Digital Illustration", "800", 3, "50")
    )
    manager.add_workshop(
        InPersonWorkshop("W102", "Canvas Painting", "1000", 2, "200")
    )

    participants = [
        Participant("P101", "Aarav Sharma", "aarav@example.com"),
        Participant("P102", "Riya Patil", "riya@example.com"),
        Participant("P103", "Kabir Verma", "kabir@example.com"),
    ]
    for participant in participants:
        manager.register_participant(participant)

    manager.show_workshops()

    first = manager.enroll("R001", "P101", "W101")
    manager.enroll("R002", "P102", "W102")
    manager.enroll("R003", "P103", "W101")

    print("\nNew registration:")
    print(first.summary())

    manager.cancel_registration("R003")
    manager.show_registrations()
    manager.show_workshops()


if __name__ == "__main__":
    main()
