import requests
import dadosreader

dados = dadosreader.read_ini_file()

"""----------------------Global variables e-Aud Produção-------------------------------"""
url = dados[0]  
header = {"Content-Type": "application/json",
          "chave-api": dados[1]}   # chave eaud produção


server = dados[2]  
database = dados[3]  


login = dados[4]  
password = dados[5]   

teams = dados[6]   
teamsteste = dados[7]  

print("Iniciando o programa...")


def check_url_health(link):
    urlteste = url+f'{link}'

    resp = requests.get(urlteste, headers=header)
    if resp.status_code != 200:
        return resp.status_code
    return resp.status_code

#import requests
#
#
## Dados sensíveis movidos para este arquivo
#url_data = 'https://eaud.cgu.gov.br/api/auth/'
#key_data = '8f3b35d1921298da06ac121bd3bc42a2'
#server_data = '10.15.135.44'
#database_data = 'eAud_teste1'
#masp_data = 'm1503249'
#pswd_data = 'Ri11C@k06'
#teams_data = 'https://cecad365.webhook.office.com/webhookb2/2312fdce-cec5-4868-a4b4-69e73fbf51ba@e5d3ae7c-9b38-48de-a087-f6734a287574/IncomingWebhook/bd39c4b46106455face502ba6e38ffc6/1439ca6d-7a4e-4610-8706-675c6b9d3d6c'
#teamsteste_data = 'https://cecad365.webhook.office.com/webhookb2/6e239511-72d5-4b67-b246-72f816722fc1@e5d3ae7c-9b38-48de-a087-f6734a287574/IncomingWebhook/e5a935383c01424985495a92ce47f60d/1439ca6d-7a4e-4610-8706-675c6b9d3d6c'
## Exportar dados
#dados = {
#    'url': url_data,
#    'key': key_data,
#    'server': server_data,
#    'database': database_data,
#    'masp': masp_data,
#    'pswd': pswd_data,
#    'teams': teams_data,
#    'teamsteste': teamsteste_data
#}
#header = {"Content-Type": "application/json",
#          "chave-api": key_data}  # chave eaud produção}
#print("Iniciando o programa...")
#
#def check_url_health(link):
#    urlteste = url_data + f'{link}'
#    
#    resp = requests.get(urlteste, headers=header)
#    if resp.status_code != 200:
#        return resp.status_code
#    return resp.status_code
