# Digital Art Commission Tracker

class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Commission:
    def __init__(self, commission_id, client, artwork, price):
        self.commission_id = commission_id
        self.client = client
        self.artwork = artwork
        self.price = price
        self.status = "Pending"

    def update_status(self, status):
        self.status = status

    def display_details(self):
        print("\nCommission ID:", self.commission_id)
        print("Client:", self.client.name)
        print("Email:", self.client.email)
        print("Artwork:", self.artwork)
        print("Price: Rs.", self.price)
        print("Status:", self.status)


class CommissionTracker:
    def __init__(self):
        self.commissions = []

    def add_commission(self, commission):
        self.commissions.append(commission)
        print("Commission added successfully.")

    def show_commissions(self):
        if not self.commissions:
            print("No commissions found.")
            return

        for commission in self.commissions:
            commission.display_details()

    def search_commission(self, commission_id):
        for commission in self.commissions:
            if commission.commission_id == commission_id:
                commission.display_details()
                return

        print("Commission not found.")


def main():
    tracker = CommissionTracker()

    client1 = Client("Aarav Sharma", "aarav@gmail.com")
    client2 = Client("Meera Joshi", "meera@gmail.com")

    commission1 = Commission("A101", client1, "Digital Portrait", 1200)
    commission2 = Commission("A102", client2, "Book Cover", 2000)

    tracker.add_commission(commission1)
    tracker.add_commission(commission2)

    commission1.update_status("Completed")

    print("\nAll Art Commissions:")
    tracker.show_commissions()

    print("\nSearch Result:")
    tracker.search_commission("A102")


if __name__ == "__main__":
    main()
