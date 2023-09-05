from pprint import pprint
from products import PRODUCTS_MENU, products, add_product, remove_product, update_product
from clients import CLIENTS_MENU, clients, add_client, remove_client, update_client
from transactions import TRANSACTION_MENU, transactions, add_transaction, remove_transaction


MAIN_MENU = """
1. Products
2. Clients
3. Transactions
4. Reports
X. Exit
"""


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
        case '3':
            display_transaction_menu = True
            while display_transaction_menu:
                print(TRANSACTION_MENU)
                option = input('Select an option from the transactions menu: ').lower()

                match option:
                    case '1':
                        add_transaction()
                    case '2':
                        remove_transaction()
                    case '3':
                        pprint(transactions)
                    case 'x':
                        print('Going back to MAIN MENU')
                        display_transaction_menu = False
        case 'x':
            print('Exit!')
            break
        case _:
            print('No such option!')
