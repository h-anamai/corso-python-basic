import matplotlib.pyplot as plt

def plot_products():
    products = ['Apples', 'Bananas', 'Oranges']
    quantity = [10, 5, 15]

    plt.bar(products, quantity, color=['red', 'yellow', 'orange'])
    plt.title('Fruits into the store')
    plt.xlabel('Product')
    plt.ylabel('Quantity')
    plt.show()

if __name__ == "__main__":
    plot_products()