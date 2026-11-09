"""Unit tests for the Parcel Delivery Tracking System.

Run with: python -m unittest test_parcel_delivery.py
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
        parcel = FragileParcel("NGP203", "Neha", 3.0)
        self.assertEqual(parcel.shipping_cost(), 150)

    def test_invalid_weight_is_rejected(self):
        with self.assertRaises(ValueError):
            Parcel("NGP204", "Dev", 0)

    def test_status_cannot_move_backwards(self):
        parcel = Parcel("NGP205", "Ira", 1.0)
        parcel.update_status("In Transit")
        with self.assertRaises(ValueError):
            parcel.update_status("Booked")

    def test_hub_rejects_duplicate_tracking_id(self):
        hub = DeliveryHub("Nagpur Central Hub")
        hub.register(Parcel("NGP206", "Aarav", 1.5))
        with self.assertRaises(ValueError):
            hub.register(Parcel("NGP206", "Meera", 2.0))

    def test_total_shipping_collection(self):
        hub = DeliveryHub("Nagpur Central Hub")
        hub.register(Parcel("NGP207", "Aarav", 2.5))
        hub.register(ExpressParcel("NGP208", "Meera", 1.2))
        self.assertEqual(hub.total_collection(), 229)


if __name__ == "__main__":
    unittest.main()
