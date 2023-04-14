import dadosreader
import requests

dados = dadosreader.read_ini_file()

"""----------------------Global variables e-Aud Produção-------------------------------"""
url = dados[0]
header = {"Content-Type": "application/json",
          "chave-api": dados[1]}  # chave eaud produção


server = dados[2]
database = dados[3]


login = dados[4]
password = dados[5]

print("Iniciando o programa...")


def check_url_health():

    response = requests.get(url)
    if response.status_code != 200:
        return response.status_code
    return response.status_code
