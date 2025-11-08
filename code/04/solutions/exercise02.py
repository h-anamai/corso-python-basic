def index_fruits():
    fruits = ['apple', 'banana', 'kiwi']
    try:
        index = int(input(f"Enter an index (0-{len(fruits)-1}): "))
        print(f"Element at index {index} is: {fruits[index]}")
    except ValueError:
        print("Error: Input is not an int.")
    except IndexError:
        print(f"Error: Index out of range (0-{len(fruits)-1}).")

if __name__ == "__main__":
    index_fruits()