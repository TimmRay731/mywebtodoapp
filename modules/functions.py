def get_todos(filename='todos.txt'):
    """ Get List From Files """
    with open(filename, 'r') as file_local:
        toDos_local = file_local.readlines()
        return toDos_local


def write_todos(todos_local, filename='todos.txt'):
    """ Write Todos To A TXT File """
    with open(filename, 'w') as file_local:
        file_local.writelines(todos_local)
