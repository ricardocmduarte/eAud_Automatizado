import dadosreader_origem_datasarver_env
import dadosreader_destino_datasaver_env

dados1 = dadosreader_origem_datasarver_env.read_env_file_origem()
dados2 = dadosreader_destino_datasaver_env.read_env_file_destino()

"--------------------Global variável eAud Automatizado Produção-----------------"

server1 = dados1[0]
database1 = dados1[1]
login1 = dados1[2]
password1 = dados1[3]

server2 = dados2[0]
database2 = dados2[1]
login2 = dados2[2]
password2 = dados2[3]

print("Iniciando Programa....")