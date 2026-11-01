# OOP Project: Event Ticket Booking System
# Concepts: classes, objects, constructors, methods, validation,
# object interaction, exception handling, and encapsulation basics.

from decimal import Decimal, InvalidOperation


class Event:
    def __init__(self, name, ticket_price, available_tickets):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Event name cannot be empty.")

        try:
            price = Decimal(str(ticket_price))
        except (InvalidOperation, ValueError):
            raise ValueError("Ticket price must be a valid number.")

        if not price.is_finite() or price <= 0:
            raise ValueError("Ticket price must be greater than zero.")

        if not isinstance(available_tickets, int) or isinstance(available_tickets, bool):
            raise ValueError("Available tickets must be a whole number.")
        if available_tickets < 0:
            raise ValueError("Available tickets cannot be negative.")

        self.name = name.strip()
        self.ticket_price = price
        self.available_tickets = available_tickets

    def book_tickets(self, customer_name, quantity):
        if not isinstance(customer_name, str) or not customer_name.strip():
            raise ValueError("Customer name cannot be empty.")
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("Ticket quantity must be a whole number.")
        if quantity <= 0:
            raise ValueError("Please book at least one ticket.")
        if quantity > self.available_tickets:
            raise ValueError(
                f"Only {self.available_tickets} ticket(s) are available."
            )

        # Reduce availability only after all checks pass.
        self.available_tickets -= quantity
        return TicketBooking(self, customer_name.strip(), quantity)

    def show_event_status(self):
        print(f"Event: {self.name}")
        print(f"Ticket price: Rs. {self.ticket_price:.2f}")
        print(f"Tickets remaining: {self.available_tickets}")


class TicketBooking:
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
            return

        self.event.available_tickets += self.quantity
        self.is_cancelled = True
        print("Booking cancelled successfully. Tickets returned.")

    def display_ticket(self):
        print("\n========== BOOKING RECEIPT ==========")
        print(f"Customer: {self.customer_name}")
        print(f"Event: {self.event.name}")
        print(f"Tickets booked: {self.quantity}")
        print(f"Price per ticket: Rs. {self.event.ticket_price:.2f}")
        print(f"Subtotal: Rs. {self.calculate_subtotal():.2f}")
        print(f"Discount: Rs. {self.calculate_discount():.2f}")
        print(f"Final amount: Rs. {self.calculate_total():.2f}")
        status = "Cancelled" if self.is_cancelled else "Confirmed"
        print(f"Booking status: {status}")
        print("=====================================")


if __name__ == "__main__":
    tech_fest = Event("Tech Fest 2026", 250, 20)

    print("--- EVENT DETAILS ---")
    tech_fest.show_event_status()

    try:
        # Booking 6 tickets gives a 10% group discount.
        booking = tech_fest.book_tickets("Sakshi", 6)

        print("\n--- CONFIRMED BOOKING ---")
        booking.display_ticket()

        print("\n--- AVAILABILITY AFTER BOOKING ---")
        tech_fest.show_event_status()

        # Demonstrate cancellation and ticket restoration.
        print("\n--- CANCELLING BOOKING ---")
        booking.cancel_booking()
        booking.display_ticket()

        print("\n--- AVAILABILITY AFTER CANCELLATION ---")
        tech_fest.show_event_status()

    except ValueError as error:
        print("Booking failed:", error)
