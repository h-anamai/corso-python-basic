from datetime import date

def print_today():
    today_str = date.today()
    print(today_str.strftime('%d-%m-%Y'))

if __name__ == "__main__":
    print_today()