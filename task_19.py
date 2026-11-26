"""Unit tests for the Parcel Delivery Tracking System.

Run with:
    python -m unittest -v
"""

import unittest

from daily_task_2026_11_09 import (
    DeliveryHub,
    ExpressParcel,
    FragileParcel,
    Parcel,
)


class ParcelTests(unittest.TestCase):
    def test_regular_shipping_cost(self):
        parcel = Parcel("NGP201", "Riya", 2.5)
        self.assertEqual(parcel.shipping_cost(), 90)

    def test_express_shipping_cost(self):
        parcel = ExpressParcel("NGP202", "Aman", 1.2)
        self.assertEqual(parcel.shipping_cost(), 139)

    def test_fragile_shipping_cost(self):
        parcel = FragileParcel("NGP203", "Neha", 3)
        self.assertEqual(parcel.shipping_cost(), 150)

    def test_invalid_weight_is_rejected(self):
        with self.assertRaises(ValueError):
            Parcel("NGP204", "Ira", 0)

    def test_delivery_status_cannot_move_backwards(self):
        parcel = Parcel("NGP205", "Dev", 1)
        parcel.update_status("In Transit")
        with self.assertRaises(ValueError):
            parcel.update_status("Booked")

    def test_duplicate_tracking_id_is_rejected(self):
        hub = DeliveryHub("Test Hub")
        hub.register(Parcel("NGP206", "Asha", 1))
        with self.assertRaises(ValueError):
            hub.register(Parcel("NGP206", "Karan", 2))

    def test_total_shipping_collection(self):
        hub = DeliveryHub("Test Hub")
        hub.register(Parcel("NGP207", "Mira", 2))
        hub.register(ExpressParcel("NGP208", "Arjun", 1))
        self.assertEqual(hub.total_collection(), 80 + 135)


if __name__ == "__main__":
    unittest.main()
