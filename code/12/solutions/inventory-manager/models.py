from abc import ABC, abstractmethod

# Abstract base class for all products
class BaseItem(ABC):
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.__price = price
        self.quantity = quantity

    # Abstract method that each subclass must implement
    @abstractmethod
    def __str__(self):
        pass

    # Method for encapsulating the price
    def get_price(self) -> float:
        return self.__price

    # Method to set the price, with validation
    def set_price(self, new_price: float):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be greater than 0.")

    def to_dict(self):
        return {'name': self.name, 'price': self.get_price(), 'quantity': self.quantity}

    @classmethod
    def from_dict(cls, data):
        return cls(name=data['name'], price=data['price'], quantity=data['quantity'])


# Subclass for food products
class FoodItem(BaseItem):
    def __init__(self, name: str, price: float, quantity: int, expiration_date: str):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def __str__(self):
        return f"Food Item: {self.name.capitalize()} | Price: {self.get_price():.2f}€ | Quantity: {self.quantity} | Expiration Date: {self.expiration_date}"

    def to_dict(self):
        data = super().to_dict()
        data['expiration_date'] = self.expiration_date
        return data

# Subclass for electronic products
class ElectronicItem(BaseItem):
    def __init__(self, name: str, price: float, quantity: int, warranty_years: int):
        super().__init__(name, price, quantity)
        self.warranty_years = warranty_years

    def __str__(self):
        return f"Electronic Item: {self.name.capitalize()} | Price: {self.get_price():.2f}€ | Quantity: {self.quantity} | Years of warranty: {self.warranty_years}"

    def to_dict(self):
        data = super().to_dict()
        data['warranty_years'] = self.warranty_years
        return data

# Item class, as a reference for the previous version of the project
class Item:
    """Class to represent a single product in the inventory."""
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Returns a string representation of the object."""
        return f"Item: {self.name.capitalize()} | Price: {self.price:.2f}€ | Quantity: {self.quantity}"

    def to_dict(self):
        """Converts the object into a dictionary for saving."""
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        """Creates an Item object from a dictionary."""
        return cls(**data)