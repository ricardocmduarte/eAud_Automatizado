import pymsteams
import dadosreader_env as dadosreader

from log import get_log
from datetime import datetime


def send_message():
    dados = dadosreader.read_env_file()
    try:
        get_log(f"Iniciando envio de mensagem automática".upper())
        msg = f'''
            ### Envio automático de mensagem {datahora()} ###

            Os dados da API do eAud foram baixados com sucesso

            Os arquivos estão armazenados na pasta de rede no formato csv e excel: 
                - U:\30_Dashboards para E-aud\4_Dados do E-aud
            Na nuvem no formato csv e excel:
                - https://cecad365-my.sharepoint.com/:f:/r/personal/m1503249_ca_mg_gov_br/Documents/Planilha%20e-Aud?csf=1&web=1&e=Tzjg2v
            
            O banco de dados do eAud foi feito o backup automatico com sucesso 
            
            Os arquivos estão armazenados no computador local pasta:
                - C:\\Users\\M1503249\\Desktop\\Backup_BD_eAud
            Na nuvem na pasta:
                - C:\\Users\\M1503249\\OneDrive - Cidade Administrativa MG\\Backup_BD_eAud
            
               
            Caso não consiga acessar a pasta na nuvem, gentileza encaminhar uma mensagem e-mail para
            ricardo.duarte@cge.mg.gov.br

            Atenciosamente,
            Ricardo via Python AutoMessage
        '''
        myTeamsMessage = pymsteams.connectorcard(dados[6])
        myTeamsMessage.text(msg)
        myTeamsMessage.send()
        get_log(f"Mensagem automática enviada com sucesso".upper())

    except NameError as err:
        get_log(f"Erro {err} ao enviar mensagem automática no teams")
        print(f"Erro {err} ao enviar mensagem automática no teams")


def datahora():
    hora_now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return hora_now
