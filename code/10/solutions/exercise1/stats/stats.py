def calculate_average(list_numbers):
    """Calculates the average of a list of numbers."""
    if not list_numbers:
        raise ValueError("Impossible to calculate the average of an empty list.")
    return sum(list_numbers) / len(list_numbers)