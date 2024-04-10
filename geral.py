import requests
import dadosreader

dados = dadosreader.read_ini_file()
#url_data = 'https://eaud.cgu.gov.br/api/auth/'
#key_data = '83'
#server_data = '10.15.1'
#database_data = 'eAu'
#masp_data = 'm1503'
#pswd_data = 'Ri11'
#teams_data = https://cecad365.webhook.office.com/webhookb2/2312fdce-cec5-4868-a4b4-69e73fbf51ba@e5d3ae7c-9b38-48de-a087-f6734a287574/IncomingWebhook/bd39c4b46106455face502ba6e38ffc6/1439ca6d-7a4e-4610-8706-675c6b9d3d6c 
#teamsteste_data = https://cecad365.webhook.office.com/webhookb2/6e239511-72d5-4b67-b246-72f816722fc1@e5d3ae7c-9b38-48de-a087-f6734a287574/IncomingWebhook/e5a935383c01424985495a92ce47f60d/1439ca6d-7a4e-4610-8706-675c6b9d3d6c

"""----------------------Global variables e-Aud Produção-------------------------------"""
url = dados[0] #url_data 
header = {"Content-Type": "application/json",
          "chave-api": dados[1]} #key_data}   # chave eaud produção


server = dados[2] #server_data 
database = dados[3] #database_data 


login = dados[4] #masp_data 
password = dados[5] #pswd_data 

#teams = dados[6] #teams_data 
teamsteste = dados[6]

print("Iniciando o programa...")


def check_url_health(link):
    urlteste = url+f'{link}'

    resp = requests.get(urlteste, headers=header)
    if resp.status_code != 200:
        return resp.status_code
    return resp.status_code