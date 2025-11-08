def dict_student():
    student = {"name": "Mario", "age": 21, "course": "Relational Databases"}
    print(*student.values()) # Python 3 .values, it returns a view object, not a list, unpack the object

if __name__ == "__main__":
    dict_student()