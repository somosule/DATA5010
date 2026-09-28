import unittest
from vending_machine import VendingMachine


class TestVendingMachine(unittest.TestCase):
    def test_assignment_example(self):
        machine = VendingMachine()
        machine.purchase(5)
        machine.restock(2)
        machine.purchase(7)
        self.assertEqual(machine.inventory, 10)

    def test_default_inventory_is_20(self):
        self.assertEqual(VendingMachine().inventory, 20)

    def test_too_many_is_declined(self):
        machine = VendingMachine(initial_inventory=3)
        self.assertFalse(machine.purchase(10))
        self.assertEqual(machine.inventory, 3)

    def test_equal_inventory_is_equal(self):
        self.assertEqual(VendingMachine(10), VendingMachine(10))
        self.assertNotEqual(VendingMachine(10), VendingMachine(5))


if __name__ == "__main__":
    unittest.main(verbosity=2)