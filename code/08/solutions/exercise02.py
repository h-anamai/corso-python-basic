import pandas as pd

def inventory():
    data = {'Product': ['Apples', 'Bananas', 'Oranges'], 'Quantity': [10, 5, 15], 'Price': [1.20, 0.80, 1.50]}
    df = pd.DataFrame(data)
    df['Total Price'] = df['Quantity'] * df['Price']
    print(df)

if __name__ == "__main__":
    inventory()