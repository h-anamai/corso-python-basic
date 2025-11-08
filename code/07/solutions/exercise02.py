import random

def random_number():
    numbers = [10, 20, 30, 40, 50]
    selected_number = random.choice(numbers)
    print(f"Random number is: {selected_number}")

if __name__ == "__main__":
    random_number()