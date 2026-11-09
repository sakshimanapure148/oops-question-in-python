"""Daily OOP Task - 09 November 2026: Parcel Delivery Tracking System."""


class Parcel:
    STATUSES = ("Booked", "In Transit", "Out for Delivery", "Delivered")

    def __init__(self, tracking_id, receiver, weight):
        if not tracking_id.strip() or not receiver.strip():
            raise ValueError("Tracking ID and receiver are required.")
        if weight <= 0:
            raise ValueError("Weight must be greater than zero.")
        self.tracking_id = tracking_id.strip().upper()
        self.receiver = receiver.strip()
        self.weight = weight
        self.__status = "Booked"

    @property
    def status(self):
        return self.__status

    def update_status(self, status):
        if status not in self.STATUSES:
            raise ValueError("Invalid delivery status.")
        if self.STATUSES.index(status) < self.STATUSES.index(self.__status):
            raise ValueError("Status cannot move backwards.")
        self.__status = status

    def shipping_cost(self):
        return 40 + self.weight * 20

    def display(self):
        print(f"{self.tracking_id} | {self.receiver} | {self.weight} kg")
        print(f"Status: {self.status} | Shipping: Rs. {self.shipping_cost():.2f}")


class ExpressParcel(Parcel):
    def shipping_cost(self):
        return super().shipping_cost() + 75


class FragileParcel(Parcel):
    def shipping_cost(self):
        return super().shipping_cost() + 50


class DeliveryHub:
    def __init__(self, name):
        self.name = name
        self._parcels = {}

    def register(self, parcel):
        if not isinstance(parcel, Parcel):
            raise TypeError("Register a Parcel object.")
        if parcel.tracking_id in self._parcels:
            raise ValueError("Duplicate tracking ID.")
        self._parcels[parcel.tracking_id] = parcel
        print(f"{parcel.tracking_id} registered.")

    def track(self, tracking_id):
        parcel = self._parcels.get(tracking_id.strip().upper())
        if parcel is None:
            print("Parcel not found.")
            return
        parcel.display()

    def show_all(self):
        print(f"\n--- {self.name}: Parcel List ---")
        for parcel in self._parcels.values():
            parcel.display()
            print("-" * 35)

    def total_collection(self):
        return sum(p.shipping_cost() for p in self._parcels.values())


def main():
    hub = DeliveryHub("Nagpur Central Hub")
    parcels = [
        Parcel("NGP101", "Aarav", 2.5),
        ExpressParcel("NGP102", "Meera", 1.2),
        FragileParcel("NGP103", "Kabir", 3.0),
    ]

    for parcel in parcels:
        hub.register(parcel)

    hub.show_all()
    print("\nTracking NGP102:")
    hub.track("ngp102")

    parcels[1].update_status("In Transit")
    parcels[1].update_status("Out for Delivery")
    print(f"\nUpdated status: {parcels[1].status}")
    print(f"Total shipping collection: Rs. {hub.total_collection():.2f}")

    assert parcels[0].shipping_cost() == 90
    assert parcels[1].shipping_cost() == 139
    assert parcels[2].shipping_cost() == 150
    assert parcels[1].status == "Out for Delivery"

    try:
        parcels[0].update_status("Delivered")
        parcels[0].update_status("In Transit")
    except ValueError as error:
        print(f"Validation test passed: {error}")

    print("All checks passed successfully.")


if __name__ == "__main__":
    main()
