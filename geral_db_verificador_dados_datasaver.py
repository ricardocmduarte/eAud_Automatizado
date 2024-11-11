#import requests
import dadosreader_verificador_dados_datasaver


dados = dadosreader_verificador_dados_datasaver.read_ini_file()


"""----------------------Global variables e-Aud Produção-------------------------------"""

server = dados[0]
database = dados[1]
login = dados[2]
password = dados[3]

#teams = dados[6]
#teamsteste = dados[7]

print("Iniciando o programa...")
