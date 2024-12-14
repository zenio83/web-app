FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read text file to be able to show
    the list of todo-items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the new todo list to the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == ""'__main__':
    print('kiekeboe... van waar kom ik nu weer????? pss functions')