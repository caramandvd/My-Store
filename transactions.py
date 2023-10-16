import csv
import datetime
from random import choice, randint

from clients import find_max_client_id
from products import find_max_product_id

TRANSACTION_MENU = """
1. Add transaction
2. Read ALL transactions
3. Read one transaction by transaction ID
x. Exit to Main Menu
"""


def read_transactions():
    try:
        with open('transactions.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        data = []
    return data


def read_transaction(transaction_id):
    data = read_transactions()
    for transaction in data:
        if int(transaction.get('transaction_id')) == transaction_id:
            return transaction
    print("The selected transaction doesn't exist")


def write_transactions(data):
    with open('transactions.csv', 'w', newline='') as file:
        fieldnames = ['transaction_id', 'client_id', 'product_id', 'quantity', 'time_of_transaction']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def add_transaction():
    data = read_transactions()
    current_time = datetime.datetime.now()
    client_transaction = int(input('Please provide the Client ID:'))
    product_transaction = int(input('Please provide the product ID:'))
    quantity = int(input('Please provide a quantity:'))

    if not data:
        transaction_id = 1
    else:
        max_transaction = max(data, key=lambda x: int(x['transaction_id']))
        transaction_id = int(max_transaction['transaction_id']) + 1

    transaction_info = {
        'transaction_id': transaction_id,
        'client_id': client_transaction,
        'product_id': product_transaction,
        'quantity': quantity,
        'time_of_transaction': current_time.strftime("%X %x")
    }
    data.append(transaction_info)
    write_transactions(data)


def dummy_time(given_range):
    second_list = []
    minute_list = []
    hour_list = []
    day_list = []
    month_list = []
    year_list = []

    second = 0
    minute = 0
    hour = 0
    day = 1
    month = 1
    year = 2010

    for transaction_id in range(given_range):
        new_second = randint(1, 10_000)
        second_list.append(second)
        minute_list.append(minute)
        hour_list.append(hour)
        day_list.append(day)
        month_list.append(month)
        year_list.append(year)

        if (new_second + second) > 59:
            minutes_added = (new_second + second) // 60
            second = (new_second + second) % 60
            minute += minutes_added

        if minute > 59:
            hours_added = minute // 60
            minute %= 60
            hour += hours_added

        if hour > 23:
            days_added = hour // 24
            hour %= 24
            day += days_added

        if day > 30:
            months_added = day // 30
            day %= 30
            month += months_added

        if month > 12:
            years_added = month // 12
            month %= 12
            year += years_added

    return second_list, minute_list, hour_list, day_list, month_list, year_list


def generate_dummy_transactions(nr_transactions):
    max_client_id = find_max_client_id()
    max_product_id = find_max_product_id()
    generated_data = []

    # 14:53:21 09/27/23
    second_list, minute_list, hour_list, day_list, month_list, year_list = dummy_time(nr_transactions)

    for transaction_id in range(nr_transactions):
        hour = str(hour_list[transaction_id]).zfill(2)
        minute = str(minute_list[transaction_id]).zfill(2)
        second = str(second_list[transaction_id]).zfill(2)
        month = str(month_list[transaction_id]).zfill(2)
        day = str(day_list[transaction_id]).zfill(2)
        year = str(year_list[transaction_id]).zfill(2)
        date_of_transaction = hour + ":" + minute + ":" + second + " " + month + '/' + day + '/' + year

        transaction = [transaction_id + 1,
                       randint(1, max_client_id),
                       randint(1, max_product_id),
                       randint(1, 10),
                       date_of_transaction
                       ]
        generated_data.append(transaction)

    with open('transactions.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Transaction_ID', 'Client_ID', 'Product_ID', 'Quantity', 'Transaction'])

        for transaction in generated_data:
            writer.writerow(transaction)

generate_dummy_transactions(100_000)
