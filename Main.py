clients = 'tomas,juan,'


def create_client(client_name): #1 "def" -> funciones
    global clients #global me permite acceder a la variable global "clients" --> por 'scope' las variables solo pueden ser usadas donde son definidas

    clients += client_name
    _add_comma()


def list_clients(): #3
    print(clients)#si esta dentro de la funcion uso tab = 4 espacios


def _add_comma(): #2 es una funcion privada, por eso empieza con  ' _ '
    global clients

    clients += ','

""" dejar 2 espacios entre cada FUNCION es buena practica """

if __name__ == '__main__':
    client_name = 'julian'

    list_clients()
    create_client(client_name)

    list_clients()
