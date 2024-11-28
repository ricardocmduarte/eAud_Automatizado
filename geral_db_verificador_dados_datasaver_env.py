import dadosreader_verificador_dados_dataserver_env

dados = dadosreader_verificador_dados_dataserver_env.read_env_file_verificador_dados()

"---------------------------Global Variáveis eAud Automtizado Produção-------------------------------------"

server = dados[0]
database = dados[1]
login = dados[2]
password = dados[3]

print("Iniciando o Programa............")