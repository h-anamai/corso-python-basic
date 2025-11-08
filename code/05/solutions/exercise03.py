import datetime

def current_time():
    current_time = datetime.datetime.now()
    print(f"The current date and time are: {current_time}")

if __name__ == "__main__":
    current_time()