def guess_number():
    secret_number = 7
    while True:
        guess = int(input("Guess a number "))
        print(guess)
        if guess == secret_number:
            print("You guessed it!")
            break
        else:
            print("Try again.")

if __name__ == "__main__":
    guess_number()