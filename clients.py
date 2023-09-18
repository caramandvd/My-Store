CLIENTS_MENU = """
1. Add Client
2. Remove Client
3. Update client
4. Display All Clients
5. Display one client
X. Go Back To Main Menu
"""


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


def read_client(selected_id):
    for client in clients.keys():
        if client == selected_id:
            return clients[selected_id]


def add_client():
    # check if the id is used, if yes select another one
    client_id = int(input('Please provide a client_id: '))
    print(client_id in clients.keys())
    last_name = input('Please provide a name: ')
    first_name = input('Please provide a last name: ')
    date_of_birth = input('Please provide a date of birth: ')
    email = input('Please provide a email: ')
    client_info = {
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
