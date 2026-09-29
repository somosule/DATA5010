
# test_vending_machine.py
 
# Unit tests for VendingMachine. These are the "experimental results"
# referenced in the presentation -- they show the class behaves correctly
# on the assignment's example, the default_inventory of 20, the edge cases and a 
# unique inventory case

# First, imports Python’s built-in testing framework (from the standard library)
import unittest 

# Imports the VendingMachine class from the main python module to test its methods
from vending_machine import VendingMachine


class TestVendingMachine(unittest.TestCase): # Test class inheriting from unittest.TestCase
    def test_assignment_example(self): # Instantiates a fresh machine with default stock (20)
        # Tests the standard lifecycle of purchasing and restocking
        # Arrange
        machine = VendingMachine()

        # Act
        machine.purchase(5) # When we purchase 5 drinks: inventory decreases to 15
        machine.restock(2) # Restock 2 drinks: inventory increases to 17
        machine.purchase(7) # Purchase 7 drinks: inventory decreases to 10

        # Assert final inventory matches expected value equal to 10
        self.assertEqual(machine.inventory, 10)
    

    
    # Verifies that every new, uninitialized VendingMachine independently defaults to 20,
    # and modifying one machine does not alter default state for others.
    def test_default_inventory_is_20(self):
        self.assertEqual(VendingMachine().inventory, 20)

    def test_too_many_is_declined(self):
        # Demonstrates Encapsulation:
        # The caller cannot force the inventory below zero. 
        # The public method handles the rejection safely.
        machine = VendingMachine(initial_inventory=3) # Creates machine starting with 3 drinks
        self.assertFalse(machine.purchase(10)) # Fails gracefully, which is what we want
        self.assertEqual(machine.inventory, 3) # Inventory remains protected and frozen at 3
    

    def test_equal_inventory_is_equal(self):
        # Demonstrates Class Customization.
        # Proves that overriding __eq__ allows us to use the '==' operator 
        # to compare two distinct machine instances based on their inventory.
        
        self.assertEqual(VendingMachine(10), VendingMachine(10)) # Tests __eq__: returns True when inventories match
        self.assertNotEqual(VendingMachine(10), VendingMachine(5)) # Tests __eq__: returns False when inventories differ
    
if __name__ == "__main__":
    # Ensures tests only execute when script is run directly
    unittest.main(verbosity=2) # Discovers all tests and prints detailed per-test pass/fail status
