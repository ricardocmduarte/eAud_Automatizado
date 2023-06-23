import pymsteams
import dadosreader

from log import get_log
from datetime import datetime


def send_message():
    dados = dadosreader.read_ini_file()
    try:
        get_log(f"Iniciando envio de mensagem automática".upper())
        msg = f'''
            ### Envio automático de mensagem {datahora()} ###

            Os dados da API do eAud foram baixados com sucesso

            Os arquivos estão armazenados na pasta de rede no formato csv e excel: 
                - R:\\BASES_DADOS\\e-AUD
            Na nuvem no formato csv e excel:
                - https://cecad365-my.sharepoint.com/:f:/g/personal/m1478769_ca_mg_gov_br/EhYDn_fjqzdCmAJitmpRXoEBw160x22B9x2XNBnGX-E1yw

            Caso não consiga acessar a pasta na nuvem, gentileza encaminhar uma mensagem/e-mail para
            endrew.barbosa@cge.mg.gov.br

            Atenciosamente,
            Endrew via Python AutoMessage
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
