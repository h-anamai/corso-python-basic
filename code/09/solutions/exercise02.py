class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
            print(f"I own a {self.brand} {self.model}.")

if __name__ == "__main__":
    car = Car("Ferrari", "Testarossa")
    car.show_details()