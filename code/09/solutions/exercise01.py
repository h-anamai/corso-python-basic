class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

if __name__ == "__main__":
    car = Car("Ferrari", "Testarossa")
    print(f"Brand: {car.brand}, Model: {car.model}")