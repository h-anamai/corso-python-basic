class Product:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_discount(self, discount):
        if 0 <= discount <= 100:
            self.__price = self.__price * (1 - discount / 100)
            print(f"New pricew: {self.__price}")
        else:
            print("Discount not valid. Enter a value between 0 and 100.")

if __name__ == "__main__":
    p = Product(200)
    print(f"Initial Prices: {p.get_price()}")
    p.set_discount(10)
    p.set_discount(150)