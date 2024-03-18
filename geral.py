import requests
import dadosreader

dados = dadosreader.read_ini_file()
#url_data = 'https://eaud.cgu.gov.br/api/auth/'
#key_data = '49186fb733c34d21c1bd8b37beef17ce'
#server_data = '10.15.135.44'
#database_data = 'eAud'
#masp_data = 'm1503249'
#pswd_data = 'Ri11@Ck06'
#teams_data = 'https://cecad365.webhook.office.com/webhookb2/6e239511-72d5-4b67-b246-72f816722fc1@e5d3ae7c-9b38-48de-a087-f6734a287574/IncomingWebhook/00d73a4c522f42a1b436d91d6ff3e3f7/1439ca6d-7a4e-4610-8706-675c6b9d3d6c'

"""----------------------Global variables e-Aud Produção-------------------------------"""
url = dados[0] #url_data 
header = {"Content-Type": "application/json",
          "chave-api": dados[1]} #key_data}   # chave eaud produção


server = dados[2] #server_data 
database = dados[3] #database_data 


login = dados[4] #masp_data 
password = dados[5] #pswd_data 

#teams = #teams_data #dados[6]
#teamsteste = dados[7]

print("Iniciando o programa...")


def check_url_health(link):
    urlteste = url+f'{link}'

    resp = requests.get(urlteste, headers=header)
    if resp.status_code != 200:
        return resp.status_code
    return resp.status_code