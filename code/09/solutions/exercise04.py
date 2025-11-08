from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Lion(Animal):
    def sound(self):
        print("Roarrrr!")

class Cow(Animal):
    def sound(self):
        print("Muuu!")

if __name__ == "__main__":
    animals = [Lion(), Cow()]

    for animal in animals:
        animal.sound()