def format_data():
    name = "Luca"
    balance = 1234.567
    print(f'Hi {name} Your balance is {balance:.2f} €')
    print(f'Hi {name} Your balance is now {balance + 100:.2f} €')


if __name__ == "__main__":
    format_data()