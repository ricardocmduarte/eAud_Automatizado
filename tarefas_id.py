import requests
import json
import geral as geral
from log import get_log
import db

tipo_arquivo = 'get_tarefas_id'


def get_tarefas_id():
    response = geral.check_url_health('tarefa')
    get_log(f"Iniciado {tipo_arquivo}")

    if response != 200:
        get_log(
            f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP:  {str(response)}".upper())
        return print(f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP:  {str(response)}")

    try:
        offset = 0
        limite_offset = 50000 #100 #200 #20000 #30000 #50000 #80000 #100000
        lista_final = []

        while offset < limite_offset:
            resultado_array = get_tarefas_id_requisicao(offset)
            if resultado_array:
                for i, lista_appended in enumerate(resultado_array):
                    lista_final.append({
                        'id': lista_appended['id'],
                        'atividade': lista_appended['atividade']
                    })
                print(f"{offset} atual {tipo_arquivo}")

                offset += 5
            else:
                offset += limite_offset

        get_log(
            f"Esta requisicao {tipo_arquivo} contém {len(lista_final)} itens")

        salvar_dados(lista_final)

        return print("Ok")

    except NameError as err:
        get_log(f"Erro {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro {tipo_arquivo}")


def salvar_dados(resultado_array):
    try:
        banco = db.db_connection()
        cur = banco.cursor()

        db.delete_datas(banco)
        get_log("Dados do banco foram apagados")
        print("Dados do banco foram apagados")

        resultado_array = db.current_datetime_query(resultado_array)

        for tarefa in resultado_array:
            lista = [
                (tarefa['id'],
                 tarefa['atividade'])
            ]

            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (
                f"""INSERT INTO tarefas_id_teste (id, atividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")

        banco.commit()
        print("Fechando conexão com o banco")

        banco.close()
        get_log(
            '--------------------------------------------------------------------------------')
        return print("Conexão encerrada")

    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_tarefas_id_requisicao(offset):
    try:
        url = geral.url + \
            f"tarefa?tamanhoPagina=5&offset={offset}&apenasAtrasadas=false&apenasFinalizadas=false&apenasModificadasNosUltimos30Dias=false&apenasExcluidas=false \
                &apenasAbertas=false&periodoInicialDataInicio=2024-03-09&periodoFinalDataInicio=2024-03-16&colunasSelecionadas=id&colunasSelecionadas=atividade"
        resp = requests.get(url, headers=geral.header)

        if resp.status_code != 200:
            get_log(
                f"Erro ao conectar com a url get_tarefas, código do erro HTTP: {str(resp.status_code)}".upper())
            return print(f"Erro ao conectar com a url get_tarefas, código do erro HTTP: {str(resp.status_code)}")

        if resp.text == '[]':
            get_log("Requisição não contém dados".upper())
            return print("Requisição não contém dados")

        response_text = json.loads(resp.text)

        return response_text['data']

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
get_tarefas_id()