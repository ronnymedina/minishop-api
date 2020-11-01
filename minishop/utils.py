import os


def get_rsa_file():
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'id_rsa')
    
    with open(file_path, 'r') as file:
        return file.read()
