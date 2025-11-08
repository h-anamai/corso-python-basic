import math

def calculate_square_root():
    number = float(input("Enter a number: "))
    square_root = math.sqrt(number)
    print(f"The square root of {number} is {square_root}")

if __name__ == "__main__":
    calculate_square_root()