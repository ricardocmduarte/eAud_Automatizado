import pymsteams
import dadosreader

from log import get_log
from datetime import datetime


def send_message():
    dados = dadosreader.read_ini_file()
    try:
        msg = f'''
            ### Envio automático de mensagem {datahora()} ###
            
            Os dados da API do eAud foram baixados com sucesso

            Os arquivos estão armazenados na pasta de rede no formato csv e excel: 
                - R:\\BASES_DADOS\\e-AUD
            Na nuvem no formato csv e excel:
                - C:\\Users\\m1478769\\OneDrive - SEPLAG MG\\Planilha e-Aud

            Caso não consiga acessar a pasta na nuvem, gentileza encaminhar uma mensagem/e-mail para
            endrew.barbosa@cge.mg.gov.br

            Atenciosamente,
            Endrew via Python AutoMessage
        '''
        myTeamsMessage = pymsteams.connectorcard(dados[6])
        myTeamsMessage.text(msg)
        myTeamsMessage.send()

    except NameError as err:
        get_log(f"Erro {err} ao enviar mensagem automática no teams")
        print(f"Erro {err} ao enviar mensagem automática no teams")


def datahora():
    hora_now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return hora_now
