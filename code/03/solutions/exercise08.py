def sum_three_numbers(a, b, c):
    return a + b + c

if __name__ == "__main__":
    numbers = [10, 20, 30]
    result = sum_three_numbers(*numbers)
    print(f"Sum is: {result}")