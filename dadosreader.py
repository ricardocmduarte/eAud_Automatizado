import configparser
from getpass import getuser, getpass

# Função responsável por ler extrair os dados sensíveis


def read_ini_file():
    filename = "dados.pyc"

    lista_dados = []

    # Reading data
    config = configparser.ConfigParser()
    config.read(filename)

    keys = [
        'url',
        'key',
        'server',
        'database',
        'masp',
        'pswd',
        'teams',
        'teamsteste'
    ]

    for key in keys:
        try:
            value = config.get("SETTINGS", key)
            lista_dados.append(value)
        except configparser.NoOptionError:
            print(f"No option '{key}' in section 'SETTINGS'")
    return lista_dados


# Função para verificar o usuário e senha
"""class login():
    def username(masp):
        if masp == 'm1503249':
            print("Welcome back, Ricardo! Please type your password below to continue...")
        else:
            print("Hello there! Please type your password bellow to continue...")
        return masp
    def password():
        return getpass()"""
