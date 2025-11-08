def guess_numbers():
    a = int(input("First number: "))
    b = int(input("Second number: "))
    if a > b:
        print("First number is greater.")
    elif a < b:
        print("First number is less.")
    else:
        print("Numbers are equal.")
        print(f"Hi, my name is {user_name} and I am {age} years old.")

if __name__ == "__main__":
    guess_numbers()