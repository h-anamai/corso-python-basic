def iter_colours():
    colours = ['red', 'green', 'blue']

    # obtain the iterator from the list
    iter_colours = iter(colours)

    # Simulate a for loop using a while loop with try-except.
    while True:
        try:
            colour = next(iter_colours)
            print(colour)
        except StopIteration:
            # The iterator has exhausted its elements, so we exit the loop.
            break

if __name__ == "__main__":
    iter_colours()