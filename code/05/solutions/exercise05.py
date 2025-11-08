def apply_format(str, formatter):
    result = formatter(str)
    print(f"The formatted string is: {result}")

def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()


if __name__ == "__main__":
    apply_format("Hello world", to_uppercase)
    apply_format("Hello world", to_lowercase)