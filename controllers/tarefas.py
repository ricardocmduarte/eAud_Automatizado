import requests
import json
import conf.geral as geral
from misc.log import get_log


def get_tarefas():
    response = geral.check_url_health()
    get_log("Iniciado get_tarefas")

    if response != 200:
        get_log(
            f"Erro ao conectar com a url, código do erro HTTP:  {str(response)}".upper())
        return print(f"Erro ao conectar com a url, código do erro HTTP:  {str(response)}")

    try:
        offset = 0
        lista_final = []
        resultado_array = get_tarefas_requisicao(offset)
        if resultado_array == None or resultado_array == [] or resultado_array == '':
            get_log('Lista de tarefas vazia')
            return print('Lista de tarefas vazia')

        for i, lista_appended in enumerate(resultado_array):
            lista_final.append({
                'id': lista_appended['id'],
                'atividade': lista_appended['atividade']
            })

        return lista_final

    except NameError as err:
        get_log("Erro get_tarefas".upper())
        get_log(err)
        return print("Erro get_tarefas")


def get_tarefas_requisicao(offset):
    try:
        url = geral.url + \
            f"tarefa?tamanhoPagina=100&offset={offset}&apenasAtrasadas=false&apenasFinalizadas=false&apenasModificadasNosUltimos30Dias=false&apenasExcluidas=false \
                &apenasAbertas=false&periodoInicialDataInicio=2021-01-01&colunasSelecionadas=id&colunasSelecionadas=atividade"
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
