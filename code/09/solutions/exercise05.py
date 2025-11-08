class Dog:
    def __init__(self, name, species):
        self.name = name
        self.species = species

if __name__ == "__main__":
    elements = [10, "hello", Dog("Fido", "Labrador"), 50.5]

    for element in elements:
        if isinstance(element, Dog):
            print(f"Found a dog! {element.name}.")
        else:
            print(f"It is not a dog. It is a {type(element)}.")