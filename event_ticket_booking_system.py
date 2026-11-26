"""Mini-project: event ticket booking with safe validation and cancellation."""

from decimal import Decimal, InvalidOperation


class Event:
    """Represent an event and manage its available ticket count."""

    def __init__(self, name, ticket_price, available_tickets):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Event name cannot be empty.")

        try:
            price = Decimal(str(ticket_price))
        except (InvalidOperation, ValueError):
            raise ValueError("Ticket price must be a valid number.") from None

        if not price.is_finite() or price <= 0:
            raise ValueError("Ticket price must be greater than zero.")
        if (
            isinstance(available_tickets, bool)
            or not isinstance(available_tickets, int)
            or available_tickets < 0
        ):
            raise ValueError("Available tickets must be a non-negative whole number.")

        self.name = name.strip()
        self.ticket_price = price
        self.available_tickets = available_tickets

    def book_tickets(self, customer_name, quantity):
        if not isinstance(customer_name, str) or not customer_name.strip():
            raise ValueError("Customer name cannot be empty.")
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Ticket quantity must be a positive whole number.")
        if quantity > self.available_tickets:
            raise ValueError(f"Only {self.available_tickets} ticket(s) are available.")

        self.available_tickets -= quantity
        return TicketBooking(self, customer_name.strip(), quantity)

    def show_event_status(self):
        print(f"Event: {self.name}")
        print(f"Ticket price: Rs. {self.ticket_price:.2f}")
        print(f"Tickets remaining: {self.available_tickets}")


class TicketBooking:
    """Represent one booking linked to its Event object."""

    DISCOUNT_LIMIT = 5
    DISCOUNT_RATE = Decimal("0.10")

    def __init__(self, event, customer_name, quantity):
        self.event = event
        self.customer_name = customer_name
        self.quantity = quantity
        self.is_cancelled = False

    def calculate_subtotal(self):
        return self.event.ticket_price * self.quantity

    def calculate_discount(self):
        if self.quantity >= self.DISCOUNT_LIMIT:
            return self.calculate_subtotal() * self.DISCOUNT_RATE
        return Decimal("0.00")

    def calculate_total(self):
        return self.calculate_subtotal() - self.calculate_discount()

    def cancel_booking(self):
        if self.is_cancelled:
            print("This booking has already been cancelled.")
            return False

        self.event.available_tickets += self.quantity
        self.is_cancelled = True
        print("Booking cancelled. Tickets returned to availability.")
        return True

    def display_ticket(self):
        print("\n========== BOOKING RECEIPT ==========")
        print(f"Customer: {self.customer_name}")
        print(f"Event: {self.event.name}")
        print(f"Tickets: {self.quantity}")
        print(f"Subtotal: Rs. {self.calculate_subtotal():.2f}")
        print(f"Discount: Rs. {self.calculate_discount():.2f}")
        print(f"Final amount: Rs. {self.calculate_total():.2f}")
        print(f"Status: {'Cancelled' if self.is_cancelled else 'Confirmed'}")
        print("=====================================")


if __name__ == "__main__":
    tech_fest = Event("Tech Fest 2026", 250, 20)
    tech_fest.show_event_status()

    try:
        booking = tech_fest.book_tickets("Sakshi", 6)
        booking.display_ticket()
        tech_fest.show_event_status()

        booking.cancel_booking()
        booking.cancel_booking()  # A second cancellation changes nothing.
        booking.display_ticket()
        tech_fest.show_event_status()
    except ValueError as error:
        print("Booking failed:", error)
