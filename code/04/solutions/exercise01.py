def divide_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a / b
        print(f"Division result is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError:
        print("Error: input not valid. Enter only numbers.")

if __name__ == "__main__":
    divide_numbers()