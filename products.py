import csv
from random import choice, randint

PRODUCTS_MENU = """
1. Add
2. Remove
3. Update
4. Display All
5. Display selected product
X. Go Back To Main Menu
"""

products = {
    1: {
        'name': 'Monitor 21 inch',
        'manufacturer': 'Philips',
        'category': 'Monitors',
        'price': 675,
        'stock': 3
    },
    2: {
        'name': 'HDMI cable',
        'manufacturer': 'HAMA',
        'category': 'Cables',
        'price': 30.99,
        'stock': 10
    }
}


def add_product():
    # check if the id is used, if yes select another one
    product_id = int(input('Please provide a product_id: '))
    print(product_id in products.keys())
    name = input('Please provide a name: ')
    manufacturer = input('Please provide a manufacturer: ')
    category = input('Please provide a category: ')
    price = int(input('Please provide a price: '))
    stock = int(input('Please provide a stock: '))
    product_info = {
        'name': name,
        'manufacturer': manufacturer,
        'category': category,
        'price': price,
        'stock': stock
    }
    products[product_id] = product_info
    print(products[product_id]['category'])


def read_product(selected_id):
    for client in products.keys():
        if client == selected_id:
            return products[selected_id]


def remove_product():
    selected_id = int(input('Please select the product you want to remove: '))
    products.pop(selected_id)


def update_product():
    selected_id = int(input('Please select the product you want to update: '))
    new_name = input('Please provide a name: ')
    new_manufacturer = input('Please provide a manufacturer: ')
    new_category = input('Please provide a category: ')
    new_price = int(input('Please provide a price: '))
    new_stock = int(input('Please provide a stock: '))
    product_info = {
        'name': new_name,
        'manufacturer': new_manufacturer,
        'category': new_category,
        'price': new_price,
        'stock': new_stock
    }
    products[selected_id] = product_info


def generate_dummy_product_data(quantity):
    with open('electronics.txt', 'r') as file:
        electronics_names = [name.strip() for name in file.readlines()]

    with open('producers.txt', 'r') as file:
        producers = [producer.strip() for producer in file.readlines()]

    # Create a list to hold the generated data
    generated_data = []

    for product_id in range(quantity):
        product = [product_id + 1,
                   choice(['', 'Super ', 'Ultra ', 'Black Series ']) + choice(electronics_names),
                   choice(producers),
                   choice(['IT', 'Constructions', 'Appliance', 'House Items']),
                   randint(50, 3000),
                   randint(1, 15)
                   ]
        generated_data.append(product)

    # Write the data to a CSV file
    with open('products.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Product_id', 'Name', 'Manufacturer', 'Category', 'Price', 'Stock'])

        for product in generated_data:
            writer.writerow(product)


def find_max_product_id():
    max_product_id = -1

    with open('products.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader, None)

        for row in csv_reader:
            product_id = int(row[0])
            if product_id > max_product_id:
                max_product_id = product_id

        return max_product_id

generate_dummy_product_data(1000)