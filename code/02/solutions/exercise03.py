def ask_grade():
    grade = int(input("Enter a grade: "))
    if grade >= 60:
        print("Passed")
    elif grade >= 40:
        print("Remedial")
    else:
        print("Failed")

if __name__ == "__main__":
    ask_grade()