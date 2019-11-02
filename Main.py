VALID_COMMANDS = 'C,L,D'
clients = 'tomas,juan,'


def create_client(client_name): #1 "def" -> funciones
    global clients #global me permite acceder a la variable global "clients" --> por 'scope' las variables solo pueden ser usadas donde son definidas

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already in clients list')


def list_clients(): #3
    print(clients)#si esta dentro de la funcion uso tab = 4 espacios


def _add_comma(): #2 es una funcion privada, por eso empieza con  ' _ '
    global clients

    clients += ','

def update_client():
    client_name = _get_client_name()
    updated_name = input('What is the new client name? ')
    _update_client(client_name, updated_name)


def _update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_name + ',')
    else:
        print('Client not in client\'s list')


def delete_client():
    client_name = _get_client_name()
    _delete_client(client_name)


def _delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client not in client\'s list')

def _get_client_name():
    return input('What is the client name?')

def _print_line():
    print('*' * 50)

""" dejar 2 espacios entre cada FUNCION es buena practica """

def _print_welcome():
    print('WELCOME')
    _print_line()
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[D]elete client')
    print('[L]ist client')


def _show_clients_and_execute_command(command):
    print('Current clients:')
    print('')
    list_clients()
    _print_line()

    command()

    print('')
    _print_line()
    print('Updated clients:')
    list_clients()


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        _show_clients_and_execute_command(update_client)
    elif command == 'D':
        _show_clients_and_execute_command(delete_client)
    else:
        print('Invalid command')
