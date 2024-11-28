import db
import requests
import geral_env as geral
from log import get_log
import json
from datetime import datetime

tipo_arquivo = 'get_interacao'

def get_interacao():
    response = geral.check_url_health('tarefa')
    get_log(f"Iniciado {tipo_arquivo}")

    if response != 200:
        get_log(f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP:  {str(response)}".upper())
        return print(f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP:  {str(response)}")

    try:
        lista_dados = []
        lista_final = []
        banco = db.db_connection()
        lista_ids = db.get_idtarefas('tarefas_id_auxiliar', banco)
        
        if lista_ids:
            for i, id in enumerate(lista_ids):
                dados = get_interacao_requisicao(id['id'])
                if dados is not None:
                    lista_dados.append(dados)
                print(f"Iteração {tipo_arquivo} {str(i)} registrada com sucesso")
        
        get_log(f"Esta requisicao {tipo_arquivo} contém {len(lista_dados)} itens".upper())

        if lista_dados:
            lista_final = tratamento_dados(lista_dados)

        if lista_final:
            salvar_dados(lista_final)

        get_log(f"Lista de {tipo_arquivo} ok".upper())
        return print(f"Lista de {tipo_arquivo} ok")
    except Exception as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)

def tratamento_dados(data):
    try:
        lista_final = []
        for i, tarefa in enumerate(data):
            if tarefa is None:
                continue  # Pula a tarefa se for None
            for j, teste in enumerate(tarefa):
                if teste is None:
                    continue  # Pula o teste se for None
                try:
                    idtarefa = teste['idTarefa']
                    tipointeracao = teste['tipoInteracao']
                    autor = teste['autor']
                    unidadeautor = teste['unidadeAutor']
                    date = datetime.strptime(teste['data'][0:10], '%Y-%m-%d') if teste['data'][0:10] else None
                    teste_data = strftime_date(date)

                    lista_final.append({
                        'id': idtarefa,
                        'tipointeracao': tipointeracao,
                        'autor': autor,
                        'idtarefa': idtarefa,
                        'unidadeautor': unidadeautor,
                        'datamodificacao': teste_data,
                    })
                except KeyError as e:
                    get_log(f"Chave ausente: {e} em {teste}")
                except ValueError as e:
                    get_log(f"Erro de valor: {e} em {teste}")
        get_log(f"Lista {tipo_arquivo} tratada com sucesso".upper())
        return lista_final
    except Exception as err:
        get_log(f"Erro ao tratar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao tratar os dados {tipo_arquivo}", err)

def salvar_dados(resultado_array):
    try:
        banco = db.db_connection()
        cur = banco.cursor()

        if resultado_array:
            for tarefa in resultado_array:
                lista = [(
                    tarefa['tipointeracao'],
                    tarefa['autor'],
                    tarefa['unidadeautor'],
                    tarefa['idtarefa'],
                    tarefa['datamodificacao']
                )]
                array_records = ", ".join(["%s"] * len(lista))
                insert_query = (
                    f"""INSERT INTO interacoes_auxiliar (tipointeracao, autor, unidadeautor, idtarefa, datamodificacao) VALUES {array_records}""")

                cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso".upper())
        banco.commit()
        banco.close()
    except Exception as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)

def get_interacao_requisicao(id):
    try:
        url = geral.url + f"tarefa/{id}/interacao/listar"
        resp = requests.get(url, headers=geral.header)

        if resp.status_code != 200:
            get_log(f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP: {str(resp.status_code)}".upper())
            print(f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP: {str(resp.status_code)}")
            return None

        if resp.text == '[]':
            get_log(f"Requisição {tipo_arquivo} não contém dados".upper())
            print(f"Requisição {tipo_arquivo} não contém dados")
            return None

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

def strftime_date(date_str):
    try:
        if date_str:
            year = date_str.year
            month = date_str.month
            day = date_str.day
            pt_br_date = f"{day:02d}/{month:02d}/{year}"
            return pt_br_date
    except AttributeError as err:
        get_log(f"Erro {err} ao converter a data para pt_br em interacao".upper())
        print(f"Erro {err} ao converter a data para pt_br em interacao".upper())

# Chama a função principal
get_interacao()
