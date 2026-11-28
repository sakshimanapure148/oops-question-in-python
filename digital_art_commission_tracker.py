"""
Digital Art Commission Tracker
------------------------------
A console-based OOP mini-project for managing custom digital art requests.

Concepts: classes, encapsulation, composition, properties, enums, validation,
status transitions, filtering, sorting and exception handling.
"""

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class CommissionStatus(Enum):
    REQUESTED = "Requested"
    ACCEPTED = "Accepted"
    IN_PROGRESS = "In Progress"
    REVIEW = "Waiting for Review"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


@dataclass
class Client:
    name: str
    email: str

    def __post_init__(self):
        self.name = self.name.strip()
        self.email = self.email.strip().lower()
        if not self.name:
            raise ValueError("Client name cannot be empty.")
        if "@" not in self.email or "." not in self.email.split("@")[-1]:
            raise ValueError("Enter a valid email address.")


@dataclass
class Commission:
    commission_id: str
    client: Client
    artwork_type: str
    description: str
    base_price: float
    due_date: date
    rush_fee: float = 0.0
    status: CommissionStatus = CommissionStatus.REQUESTED
    revision_limit: int = 2
    revisions_used: int = 0
    notes: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.commission_id = self.commission_id.strip().upper()
        self.artwork_type = self.artwork_type.strip().title()
        self.description = self.description.strip()
        if not self.commission_id or not self.artwork_type or not self.description:
            raise ValueError("ID, artwork type and description are required.")
        if self.base_price <= 0 or self.rush_fee < 0:
            raise ValueError("Price must be positive and rush fee cannot be negative.")
        if self.due_date < date.today():
            raise ValueError("Due date cannot be in the past.")
        if self.revision_limit < 0:
            raise ValueError("Revision limit cannot be negative.")

    @property
    def total_price(self):
        return round(self.base_price + self.rush_fee, 2)

    @property
    def revisions_remaining(self):
        return self.revision_limit - self.revisions_used

    def add_note(self, note):
        note = note.strip()
        if not note:
            raise ValueError("Note cannot be empty.")
        self.notes.append(note)

    def request_revision(self, note):
        if self.status not in (CommissionStatus.REVIEW, CommissionStatus.IN_PROGRESS):
            raise ValueError("Revisions are available only during review or work.")
        if self.revisions_remaining <= 0:
            raise ValueError("No revisions remaining.")
        self.revisions_used += 1
        self.add_note(f"Revision {self.revisions_used}: {note}")

    def change_status(self, new_status):
        allowed = {
            CommissionStatus.REQUESTED: {CommissionStatus.ACCEPTED, CommissionStatus.CANCELLED},
            CommissionStatus.ACCEPTED: {CommissionStatus.IN_PROGRESS, CommissionStatus.CANCELLED},
            CommissionStatus.IN_PROGRESS: {CommissionStatus.REVIEW, CommissionStatus.CANCELLED},
            CommissionStatus.REVIEW: {CommissionStatus.IN_PROGRESS, CommissionStatus.COMPLETED},
            CommissionStatus.COMPLETED: set(),
            CommissionStatus.CANCELLED: set(),
        }
        if new_status not in allowed[self.status]:
            raise ValueError(
                f"Cannot move from {self.status.value} to {new_status.value}."
            )
        self.status = new_status


class CommissionStudio:
    def __init__(self, studio_name):
        self.studio_name = studio_name.strip()
        if not self.studio_name:
            raise ValueError("Studio name cannot be empty.")
        self._commissions = {}

    def add_commission(self, commission):
        if commission.commission_id in self._commissions:
            raise ValueError("A commission with this ID already exists.")
        self._commissions[commission.commission_id] = commission
        print(f"Added commission {commission.commission_id}.")

    def get_commission(self, commission_id):
        commission_id = commission_id.strip().upper()
        if commission_id not in self._commissions:
            raise KeyError(f"Commission {commission_id} was not found.")
        return self._commissions[commission_id]

    def update_status(self, commission_id, status):
        commission = self.get_commission(commission_id)
        commission.change_status(status)
        print(f"{commission.commission_id}: {status.value}")

    def search_by_client(self, name):
        keyword = name.strip().casefold()
        return [
            item for item in self._commissions.values()
            if keyword in item.client.name.casefold()
        ]

    def pending_commissions(self):
        finished = {CommissionStatus.COMPLETED, CommissionStatus.CANCELLED}
        return sorted(
            (item for item in self._commissions.values() if item.status not in finished),
            key=lambda item: item.due_date
        )

    def revenue_summary(self):
        completed = [
            item for item in self._commissions.values()
            if item.status == CommissionStatus.COMPLETED
        ]
        return {
            "completed_count": len(completed),
            "completed_value": round(sum(item.total_price for item in completed), 2),
            "active_count": len(self.pending_commissions()),
        }

    def display_commissions(self, commissions=None):
        items = commissions if commissions is not None else self._commissions.values()
        print(f"\n--- {self.studio_name}: Commission List ---")
        if not items:
            print("No commissions found.")
            return
        for item in sorted(items, key=lambda entry: entry.due_date):
            print(
                f"{item.commission_id} | {item.client.name} | {item.artwork_type} | "
                f"₹{item.total_price:.2f} | Due: {item.due_date} | {item.status.value}"
            )


def demo():
    studio = CommissionStudio("Pixel Palette Studio")

    client_one = Client("Aarav Sharma", "aarav@example.com")
    client_two = Client("Meera Joshi", "meera@example.com")

    first = Commission(
        "ART-101", client_one, "Character Portrait",
        "A colourful character portrait with a simple background.",
        1200, date.today(), rush_fee=200
    )
    second = Commission(
        "ART-102", client_two, "Book Cover",
        "A fantasy-inspired digital book cover.",
        2500, date.today()
    )

    studio.add_commission(first)
    studio.add_commission(second)

    studio.update_status("ART-101", CommissionStatus.ACCEPTED)
    studio.update_status("ART-101", CommissionStatus.IN_PROGRESS)
    first.add_note("Initial sketch prepared.")
    studio.update_status("ART-101", CommissionStatus.REVIEW)
    first.request_revision("Adjust the background colours.")
    studio.update_status("ART-101", CommissionStatus.COMPLETED)

    studio.display_commissions()
    print("\nRevenue summary:", studio.revenue_summary())
    print("\nSearch results for Meera:")
    studio.display_commissions(studio.search_by_client("Meera"))


if __name__ == "__main__":
    try:
        demo()
    except (ValueError, KeyError) as error:
        print("Error:", error)
