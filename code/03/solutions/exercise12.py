def first_letter():
    words = ['python', 'ai', 'data']
    first_letters = {word[0] for word in words}
    print(first_letters)

if __name__ == "__main__":
    first_letter()