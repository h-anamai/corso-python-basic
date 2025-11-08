# Repeat Decorator with parameter
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Execution {i+1}/{n}")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

if __name__ == "__main__":
    say_hi()