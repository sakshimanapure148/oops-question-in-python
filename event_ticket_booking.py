# Today's OOP Practice: Event Ticket Booking System
# Concepts: class, object, constructor, instance attributes, methods, and conditions.

class EventTicket:
    def __init__(self, event_name, ticket_price, quantity):
        if ticket_price <= 0:
            raise ValueError("Ticket price must be greater than zero.")
        if quantity <= 0:
            raise ValueError("Ticket quantity must be at least one.")

        self.event_name = event_name
        self.ticket_price = ticket_price
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.ticket_price * self.quantity

    def calculate_discount(self):
        # Give a 10% discount when 5 or more tickets are booked.
        if self.quantity >= 5:
            return self.calculate_subtotal() * 0.10
        return 0

    def calculate_final_amount(self):
        return self.calculate_subtotal() - self.calculate_discount()

    def display_booking(self):
        print("\n--- EVENT TICKET BOOKING ---")
        print("Event:", self.event_name)
        print("Ticket Price: Rs.", self.ticket_price)
        print("Number of Tickets:", self.quantity)
        print("Subtotal: Rs.", self.calculate_subtotal())
        print("Discount: Rs.", self.calculate_discount())
        print("Final Amount: Rs.", self.calculate_final_amount())


if __name__ == "__main__":
    booking1 = EventTicket("Tech Fest 2026", 250, 6)
    booking1.display_booking()

    booking2 = EventTicket("Music Night", 400, 2)
    booking2.display_booking()
