import configparser
# from getpass import getuser, getpass

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
        'pswd'
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
        if masp == 'm1478769':
            print("Welcome back, Drew! Please type your password below to continue...")
        else:
            print("Hello there! Please type your password bellow to continue...")
        return masp
    def password():
        return getpass()"""
