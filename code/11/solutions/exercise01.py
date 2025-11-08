# Logging Decorator
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(5, 3))