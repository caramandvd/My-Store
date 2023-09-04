from pprint import pprint

MAIN_MENU = """
1. Products
2. Clients
3. Transactions
4. Reports
X. Exit
"""

PRODUCTS_MENU = """
1. Add
2. Remove
3. Update
4. Display All
X. Go Back To Main Menu
"""

CLIENTS_MENU = """
1. Add Client
2. Remove Client
3. Update client
4. Display All Clients
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

clients = {
    1: {'last_name': 'Pop',
        'first_name': 'Ion',
        'date_of_birth': '21/08/1968',
        'email': 'popion@email.com'
        },
    2: {
        'last_name': 'Stan',
        'first_name': 'Ana',
        'date_of_birt': '14/06/2001',
        'email': 'stanana@email.com'
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


def remove_client():
    selected_id = int(input('Please select the client id to remove: '))
    clients.pop(selected_id)


def add_client():
    # check if the id is used, if yes select another one
    client_id = int(input('Please provide a client_id: '))
    print(client_id in clients.keys())
    last_name = input('Please provide a name: ')
    first_name = input('Please provide a last name: ')
    date_of_birth = input('Please provide a date of birth: ')
    email = input('Please provide a stock: ')
    client_info = {
        'last_name': last_name,
        'first_name': first_name,
        'date_of_birth': date_of_birth,
        'email': email
    }
    clients[client_id] = client_info
    print(products[product_id]['category'])


def update_client():
    selected_id = int(input('please provide the id to update: '))
    last_name = input('Please provide a name: ')
    first_name = input('Please provide a last name: ')
    date_of_birth = input('Please provide a date of birth: ')
    email = input('Please provide an email: ')
    client_info = {
        'last_name': last_name,
        'first_name': first_name,
        'date_of_birth': date_of_birth,
        'email': email
    }
    clients[selected_id] = client_info

while True:
    print(MAIN_MENU)

    option = input('Select an option from the menu: ').lower()

    match option:
        case '1':
            display_products_menu = True
            while display_products_menu:
                print(PRODUCTS_MENU)
                option = input('Select an option from the product menu: ').lower()

                match option:
                    case '1':
                        add_product()
                    case '2':
                        remove_product()
                    case '3':
                        update_product()
                    case '4':
                        pprint(products)
                    case 'x':
                        print('Going back to MAIN MENU')
                        display_products_menu = False
                    case _:
                        print('No such option!')
        case '2':
            display_clients_menu = True
            while display_clients_menu:
                print(CLIENTS_MENU)
                option = input('Select an option from the clients menu: ').lower()

                match option:
                    case '1':
                        add_client()
                    case '2':
                        remove_client()
                    case '3':
                        update_client()
                    case '4':
                        pprint(clients)
                    case 'x':
                        print('Going back to MAIN MENU')
                        display_clients_menu = False
                    case _:
                        print('No such option!')


        case 'x':
            print('Exit!')
            break
        case _:
            print('No such option!')