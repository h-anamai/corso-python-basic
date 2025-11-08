def write_names():
    names = ["Mario", "Filippo", "Paolo", "Sofia"]

    with open("names.txt", "w") as file:
        for name in names:
            file.write(name + "\n")

if __name__ == "__main__":
    write_names()