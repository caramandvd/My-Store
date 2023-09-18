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
