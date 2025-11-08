def gen_numbers():
    gen = (x**3 for x in range(5))
    for value in gen:
        print(value)

if __name__ == "__main__":
    gen_numbers()