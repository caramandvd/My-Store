import datetime
transactions = {}
transaction_counter = 1

TRANSACTION_MENU = """
1. Add transaction
2. Remove transaction
x. Exit to Main Menu
"""


def add_transaction():
    global transaction_counter
    current_time = datetime.datetime.now()
    client_transaction = int(input('Please provide the Client ID:'))
    product_transaction = int(input('Please provide the product ID:'))
    quantity = int(input('Please provide a quantity:'))
    transaction_id = transaction_counter
    transaction_counter += 1

    transaction_info = {
        'client_id': client_transaction,
        'product_if': product_transaction,
        'quantity': quantity,
        'time_of_transaction': current_time.strftime("%X %x")
    }
    transactions[transaction_id] = transaction_info


def remove_transaction():
    selected_id = int(input('Please select a transaction id: '))
    transactions.pop(selected_id)
