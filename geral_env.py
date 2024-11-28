import requests
import dadosreader_env 
import dadosreader_origem_datasarver_env 
import dadosreader_destino_datasaver_env 
import dadosreader_verificador_dados_dataserver_env 

def validate_data(data, expected_length, source_name):
    if len(data) != expected_length:
        raise ValueError(f"Erro ao ler {source_name}: esperado {expected_length} elementos, mas obteve {len(data)}")
    return data

# Leitura e validação dos dados
dados = validate_data(dadosreader_env.read_env_file(), 8, "dadosreader_env")
dados1 = validate_data(dadosreader_origem_datasarver_env.read_env_file_origem(), 4, "dadosreader_origem_datasarver_env")
dados2 = validate_data(dadosreader_destino_datasaver_env.read_env_file_destino(), 4, "dadosreader_destino_datasaver_env")
dados3 = validate_data(dadosreader_verificador_dados_dataserver_env.read_env_file_verificador_dados(), 4, "dadosreader_verificador_dados_dataserver_env")

"-----------------------------Variáveis Glaobais e-Aud Produção----------------------------------------------"

url = dados[0]
header = {
    "Content-Type": "application/json",
    "chave-api": dados[1] # chave eaud produção
}
server = dados[2]
database = dados[3]
login = dados[4]
password = dados[5]
teams = dados[6]
teamsteste = dados[7]
 
server1 = dados1[0]
database1 = dados1[1]
login1= dados1[2]
password1 = dados1[3]
          
server2 = dados2[0]
database2 = dados2[1]
login2 = dados2[2]
password2 = dados2[3]
      
server3 = dados3[0]
database3 = dados3[1]
login3 = dados3[2]
password3 = dados3[3]

print("Iniciando o Programa.......")
    
def check_url_health(link):
    urlteste = url + f'{link}'
    resp = requests.get(urlteste, headers=header)
    if resp.status_code != 200:
        return resp.status_code
    return resp.status_code