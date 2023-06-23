import geral
import db
import requests
import json
from log import get_log

tipo_arquivo = 'get_interacao'


def get_interacao():
    banco = db.db_connection()
    resultado = db.get_idtarefas_status(banco)
    return resultado


def tratamento_dados(lista):
    pass


def salvar_dados(resultado_array):

    banco = db.db_connection()
    cur = banco.cursor()


def get_auditoria_requisicao(id):
    try:
        url = geral.url + \
            f"tarefa/{id}/interacao/listar"
        resp = requests.get(url, headers=geral.header)

        if resp.status_code != 200:
            get_log(
                f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP: {str(resp.status_code)}".upper())
            print(
                f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP: {str(resp.status_code)}")
            return None

        if resp.text == '[]':
            get_log(f"Requisição {tipo_arquivo} não contém dados".upper())
            return print(f"Requisição {tipo_arquivo} não contém dados")

        response_text = json.loads(resp.text)

        return response_text

    except requests.exceptions.HTTPError as errh:
        get_log(errh)
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        get_log(errc)
        print(errc)
    except requests.exceptions.Timeout as errt:
        get_log(errt)
        print(errt)
    except requests.exceptions.RequestException as err:
        get_log(err)
        print(err)


get_interacao()
