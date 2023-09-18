import datetime
import json

transactions = {}
transaction_counter = 1

TRANSACTION_MENU = """
1. Add transaction
2. Read ALL transactions
3. Read one transaction by transaction ID
x. Exit to Main Menu
"""


def read_transactions():
    try:
        with open('transactions_log.json', 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data


def read_transaction(transaction_id):
    try:
        with open('transactions_log.json', 'r') as file:
            data = {}
            data = json.load(file)
            for transaction in data:
                if transaction.get('transaction_id') == transaction_id:
                    return transaction
            print("The selected transaction doesn't exist")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data


def write_transactions(data):
    with open('transactions_log.json', 'w') as file:
        json.dump(data, file, indent=4)


def add_transaction():
    data = list(read_transactions())
    global transaction_counter
    current_time = datetime.datetime.now()
    client_transaction = int(input('Please provide the Client ID:'))
    product_transaction = int(input('Please provide the product ID:'))
    quantity = int(input('Please provide a quantity:'))
    # transaction_id = int(last_id()) + 1
    if not data:
        transaction_id = 1
    else:
        max_transaction = max(data, key=lambda x: x['transaction_id'])
        transaction_id = max_transaction['transaction_id'] + 1

    transaction_info = {
        'transaction_id': transaction_id,
        'client_id': client_transaction,
        'product_if': product_transaction,
        'quantity': quantity,
        'time_of_transaction': current_time.strftime("%X %x")
    }
    data.append(transaction_info)
    write_transactions(data)
