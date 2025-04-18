import os

def get_todos(filepath = (os.path.join(os.path.dirname(__file__), 'todo.txt'))):
    """ Read a text file and return a list of
    to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath = os.path.join(os.path.dirname(__file__), 'todo.txt')):
    """ Write the To-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")