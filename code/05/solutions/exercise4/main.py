# content of main.py file
from operations.geometry import calculate_rectangle_area

def rectangle_area():
    area = calculate_rectangle_area(10, 5)
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    rectangle_area()