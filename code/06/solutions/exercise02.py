def read_names():
    with open("names.txt", "r") as file:
        rows = file.readlines()
        print(f"File contains {len(rows)} names.")

if __name__ == "__main__":
    read_names()