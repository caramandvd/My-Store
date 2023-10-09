import csv
from datetime import datetime
from random import choice, randint

from stdnum.exceptions import *
from pandas import *
import numpy as np
import matplotlib.pyplot as plt

CLIENTS_MENU = """
1. Add Client
2. Remove Client
3. Update client
4. Display All Clients
5. Display one client
X. Go Back To Main Menu
"""


REPORTS_MENU = """
1. Average client date of birth 
2. Age Distribution Chart
"""

clients = {
    1: {'cnp': '1680213123456',
        'last_name': 'Pop',
        'first_name': 'Ion',
        'date_of_birth': '1968-02-13',
        'email': 'popion@email.com'
        },
    2: {'cnp': '6030221123456',
        'last_name': 'Stan',
        'first_name': 'Ana',
        'date_of_birth': '2003-02-21',
        'email': 'stanana@email.com'
        },
    3: {'cnp': '1760213123456',
        'last_name': 'Popescu',
        'first_name': 'Andrei',
        'date_of_birth': '1976-02-13',
        'email': 'andreipopescu@email.com'
        },
    4: {'cnp': '6041211123456',
        'last_name': 'Iulia',
        'first_name': 'Dancila',
        'date_of_birth': '2004-12-11',
        'email': 'iuliadancila@email.com'
        }
}


def dob_from_cnp(cnp):
    centuries = {
        '1': 1900, '2': 1900, '3': 1800, '4': 1800, '5': 2000, '6': 2000,
    }  # we assume 1900 for the others in order to try to construct a date
    year = int(cnp[1:3]) + centuries.get(cnp[0], 1900)
    month = int(cnp[3:5])
    day = int(cnp[5:7])
    d = str(datetime.date(year, month, day))
    try:
        return d
    except ValueError:
        raise InvalidComponent()


def read_client(selected_id):
    for client in clients.keys():
        if client == selected_id:
            return clients[selected_id]


def add_client():
    # check if the id is used, if yes select another one
    client_id = int(input('Please provide a client_id: '))
    print(client_id in clients.keys())
    client_cnp = input('Please provide the CNP of the client: ')
    last_name = input('Please provide a name: ')
    first_name = input('Please provide a last name: ')
    date_of_birth = dob_from_cnp(client_cnp)
    email = input('Please provide a email: ')
    client_info = {
        'client_cnp': client_cnp,
        'last_name': last_name,
        'first_name': first_name,
        'date_of_birth': date_of_birth,
        'email': email
    }
    clients[client_id] = client_info


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


def remove_client():
    selected_id = int(input('Please select the client ID you want to remove: '))
    clients.pop(selected_id)


def read_id_dob_from_file():
    data = read_csv('clients.csv')
    client_id = data['Client ID'].tolist()
    d_o_b = data['Date of Birth'].tolist()
    id_dob_list = [client_id, d_o_b]
    return id_dob_list


def mean_dob():
    dob = read_id_dob_from_file()[1]
    mean = (np.array(dob, dtype='datetime64[s]')
            .view('i8')
            .mean()
            .astype('datetime64[s]'))
    return mean


def age_distribution_graph():
    dob_list = read_id_dob_from_file()
    client_id = dob_list[0]
    client_dob = dob_list[1]
    dob_datetime = [datetime.strptime(date, "%Y-%m-%d") for date in client_dob]
    current_date = datetime.now()
    ages = [(current_date - dob).days//365 for dob in dob_datetime]
    age_bins = [0, 1, 2, 3, 4, 5]

    plt.scatter(client_id, ages, color='blue', marker='o', s=100)

    # Customize the plot
    plt.title('Age Distribution')
    plt.xlabel('Client ID')
    plt.ylabel('Age')
    plt.xticks(age_bins)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the plot
    plt.show()


def generate_cnp():
    year = randint(1900, 2010)
    if year < 2000:
        firstdigit = randint(1, 2)
    else:
        firstdigit = randint(5, 6)
    month = randint(1, 12)
    if month < 10:
        month = '0' + str(month)
    day = randint(1, 28)
    if day < 10:
        day = '0' + str(day)
    last_digits = str(randint(1, 999999)).zfill(6)
    cnp = str(firstdigit) + str(year)[2:] + str(month) + str(day) + str(last_digits)
    return cnp, year, month, day


def generate_dummy_client_data(nr_clients):
    with open('First Name.txt', 'r') as file:
        firstname = [name.strip() for name in file.readlines()]

    with open('Last Name.txt', 'r') as file:
        lastname = [producer.strip() for producer in file.readlines()]

    # Create a list to hold the generated data
    generated_data = []

    for client_id in range(nr_clients):
        cnp, year, month, day = generate_cnp()
        date = str(year) + "-" + str(month) + '-' + str(day)
        rnd_firstname = choice(firstname)
        rnd_lastname = choice(lastname)
        email = str(rnd_firstname).lower() + str(rnd_lastname).lower() + '@gmail.com'
        client = [
            client_id + 1,
            rnd_firstname,
            rnd_lastname,
            cnp,
            date,
            email
        ]
        generated_data.append(client)

    # Write the data to a CSV file
    with open('clients.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Client ID', 'First Name', 'Last Name', 'CNP', 'Date of Birth', 'email'])

        for client in generated_data:
            writer.writerow(client)


def find_max_client_id():
    max_client_id = -1

    with open('clients.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader, None)

        for row in csv_reader:
            client_id = int(row[0])
            if client_id > max_client_id:
                max_client_id = client_id

        return max_client_id

generate_dummy_client_data(100)
print(mean_dob())