from colorama import Fore, Style
from inventory_manager import InventoryManager
from models import Item, FoodItem, ElectronicItem

def menu():
    """Displays the menu and handles user input."""
    manager = InventoryManager()
    while True:
        manager.show_inventory()
        print("\nOptions: (a)dd, (r)emove, (s)ave, (l)oad, (q)uit")
        choice = input("Choose an option: ").lower()

        if choice == 'a':
            item_type = input("What type of item do you want to add? (f)ood, (e)lectronic or (s)imple: ").lower()
            name = input("Item name: ")
            try:
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                if price <= 0 or quantity <= 0:
                    print(f"{Fore.RED}Error: Price and quantity must be greater than zero.{Style.RESET_ALL}")
                    continue

                if item_type == 'f':
                    expiration = input("Expiration date (dd-mm-yyyy): ")
                    new_item = FoodItem(name, price, quantity, expiration)
                elif item_type == 'e':
                    warranty = int(input("Warranty (years): "))
                    new_item = ElectronicItem(name, price, quantity, warranty)
                elif item_type == 's':
                    new_item = Item(name, price, quantity)
                else:
                    print(f"{Fore.RED}Invalid item type.{Style.RESET_ALL}")
                    continue

                manager.add_item(new_item)
            except ValueError:
                print(f"{Fore.RED}Error: Price, quantity and warranty must be valid numbers.{Style.RESET_ALL}")

        elif choice == 'r':
            name = input("Item name to sell: ")
            manager.sell_item(name)

        elif choice == 's':
            manager.save_inventory()

        elif choice == 'l':
            manager.load_inventory()

        elif choice == 'q':
            print("Thank you, program terminated.")
            break

        else:
            print(f"{Fore.RED}Invalid option, try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    menu()