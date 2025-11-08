import numpy as np

def random_numbers():
    random_numbers = np.random.randint(1, 51, 10)
    print(f"Array: {random_numbers}")
    print(f"Max Value: {random_numbers.max()}")
    print(f"Min Value: {random_numbers.min()}")
    print(f"Average: {random_numbers.mean():.2f}")

if __name__ == "__main__":
    random_numbers()