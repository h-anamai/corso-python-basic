import unittest
import os
from inventory_manager import InventoryManager
from models import Item, FoodItem, ElectronicItem

class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        # Runs before each test.
        # Ensures a clean test environment by removing the save file.
        self.manager = InventoryManager()
        if os.path.exists(self.manager.FILE_NAME):
            os.remove(self.manager.FILE_NAME)
        # Initializes a new manager that will start with an empty inventory
        self.manager = InventoryManager()
        self.test_item = Item("Test Item", 10.0, 5)

    def tearDown(self):
        # Runs after each test.
        # Cleans up by removing the save file created.
        if os.path.exists(self.manager.FILE_NAME):
            os.remove(self.manager.FILE_NAME)

    def test_add_item_success(self):
        self.assertTrue(self.manager.add_item(self.test_item))
        self.assertEqual(len(self.manager.inventory), 1)
        self.assertIn("Test Item", self.manager.inventory)

    def test_add_existing_item(self):
        self.manager.add_item(self.test_item)
        duplicate_item = Item("Test Item", 12.0, 3)
        self.assertFalse(self.manager.add_item(duplicate_item))
        self.assertEqual(self.manager.inventory['Test Item'].quantity, 5)

    def test_sell_item_success(self):
        self.manager.add_item(self.test_item)
        self.assertTrue(self.manager.sell_item("Test Item", 3))
        self.assertEqual(self.manager.inventory['Test Item'].quantity, 2)

    def test_sell_item_insufficient_quantity(self):
        self.manager.add_item(self.test_item)
        self.assertFalse(self.manager.sell_item("Test Item", 10))
        self.assertEqual(self.manager.inventory['Test Item'].quantity, 5)

    def test_sell_nonexistent_item(self):
        self.assertFalse(self.manager.sell_item("Nonexistent Item", 1))

    def test_save_and_load_inventory(self):
        food_item = FoodItem("Milk", 1.50, 10, "30-12-2025")
        electronic_item = ElectronicItem("Laptop", 1200.0, 2, 2)
        self.manager.add_item(food_item)
        self.manager.add_item(electronic_item)
        self.manager.save_inventory()

        # Create a new instance of InventoryManager to simulate a new program start
        new_manager = InventoryManager()

        # Verify that the inventory was loaded correctly
        self.assertIn("Milk", new_manager.inventory)
        self.assertIn("Laptop", new_manager.inventory)
        self.assertEqual(new_manager.inventory['Milk'].quantity, 10)
        self.assertEqual(new_manager.inventory['Laptop'].get_price(), 1200.0)
        self.assertIsInstance(new_manager.inventory['Milk'], FoodItem)
        self.assertIsInstance(new_manager.inventory['Laptop'], ElectronicItem)

if __name__ == '__main__':
    unittest.main()
