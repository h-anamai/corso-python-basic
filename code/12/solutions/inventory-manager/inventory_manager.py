import json
from colorama import Fore, Style
from models import Item, FoodItem, ElectronicItem
from functools import wraps

# Decorator to log actions
def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('actions.log', 'a') as f:
            f.write(f'{func.__name__} called with args={args[1:]}, kwargs={kwargs}\n')
        return result
    return wrapper

class InventoryManager:
    """Class that manages all operations on the inventory."""
    FILE_NAME = "inventory.json"

    def __init__(self):
        self.inventory = {}
        self.load_inventory()

    @log_action
    def add_item(self, item):
        if item.name in self.inventory:
            print(f"{Fore.YELLOW}Warning: Item {item.name} already exists.{Style.RESET_ALL}")
            return False
        else:
            self.inventory[item.name] = item
            print(f"{Fore.GREEN}Item {item.name} added.{Style.RESET_ALL}")
            return True

    @log_action
    def sell_item(self, name: str, sold_quantity: int):
        if name in self.inventory:
            item = self.inventory[name]
            if item.quantity >= sold_quantity:
                item.quantity -= sold_quantity
                print(f"{Fore.GREEN}{sold_quantity} {name} sold. There are left {item.quantity}.{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}Error: Not enough quantity. Ramaining: {item.quantity}{Style.RESET_ALL}")
                return False
        else:
            print(f"{Fore.RED}Error: Item {name} not exist.{Style.RESET_ALL}")
            return False

    def show_inventory(self):
        print("\n--- Current Inventory ---")
        if not self.inventory:
            print("Inventory is empty.")
        for item in self.inventory.values():
            print(item)
        print("--------------------------")

    def save_inventory(self):
        try:
            with open(self.FILE_NAME, 'w') as f:
                inventory_to_save = {}
                for name, item in self.inventory.items():
                    item_details = item.to_dict()
                    item_details['item_type'] = item.__class__.__name__
                    inventory_to_save[name] = item_details
                json.dump(inventory_to_save, f, indent=4)
            print(f"{Fore.GREEN}Inventory saved.{Style.RESET_ALL}")
        except IOError:
            print(f"{Fore.RED}Error saving the file.{Style.RESET_ALL}")

    def load_inventory(self):
        try:
            with open(self.FILE_NAME, 'r') as f:
                inventory_loaded = json.load(f)
                self.inventory = {}
                for name, item_details in inventory_loaded.items():
                    item_type = item_details.pop('item_type')
                    if item_type == 'FoodItem':
                        self.inventory[name] = FoodItem.from_dict(item_details)
                    elif item_type == 'ElectronicItem':
                        self.inventory[name] = ElectronicItem.from_dict(item_details)
                    elif item_type == 'Item':
                        self.inventory[name] = Item.from_dict(item_details)
            print(f"{Fore.GREEN}Inventory loaded.{Style.RESET_ALL}")
        except (IOError, json.JSONDecodeError, TypeError) as e:
            print(f"{Fore.YELLOW}No inventory existing or corrupted file. Error details: {e}{Style.RESET_ALL}")
            self.inventory = {}