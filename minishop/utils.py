from os import path

def get_rsa_files():
    module_dir = path.dirname(__file__)  # get current directory
    rsa_files = {'private': None, 'public': None}

    with open(path.join(module_dir, 'id_rsa'), 'r') as file:
        rsa_files['private'] = file.read()

    with open(path.join(module_dir, 'id_rsa.pub'), 'r') as file:
        rsa_files['public'] = file.read()

    return rsa_files
