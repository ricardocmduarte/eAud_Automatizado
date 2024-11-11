#import requests
import dadosreader_origem_datasaver
import dadosreader_destino_datasaver

dados1 = dadosreader_origem_datasaver.read_ini_file_origem()
dados2 = dadosreader_destino_datasaver.read_ini_file_destino()


"""----------------------Global variables e-Aud Produção-------------------------------"""

server1 = dados1[0]
database1 = dados1[1]
login1 = dados1[2]
password1 = dados1[3]

server2 = dados2[0]
database2 = dados2[1]
login2 = dados2[2]
password2 = dados2[3]

#teams = dados[6]
#teamsteste = dados[7]

print("Iniciando o programa...")
