def convert_int():
    try:
        number_str = input("Enter an int: ")
        number_int = int(number_str)
        print(f"Int is: {number_int}")
    except ValueError:
        print(f"Error: '{number_str}' is not a valid int.")

if __name__ == "__main__":
    convert_int()