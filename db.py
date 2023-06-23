import psycopg2
import geral as geral
from datetime import datetime
from log import get_log


def db_connection():
    try:
        # String de conexão em produção
        conn_string = psycopg2.connect(
            f"host = {geral.server}   dbname ={geral.database}   user = {geral.login}  password = {geral.password}")
        conn = conn_string
        return conn
    except NameError as err:
        get_log("ERRO DB_CONNECTION")
        get_log(err)
        print("Erro db connection", err)


def delete_query(tabela, banco):
    try:
        cur = banco.cursor()
        cur.execute(f"""SELECT id FROM {tabela}""")
        rows = cur.fetchall()
        count_items = len(rows)

        if (count_items != 0):
            delete_query = (f"""DELETE FROM {tabela}""")
            banco.cursor().execute(delete_query)
            banco.commit()
            print(f"Dados da tabela {tabela} foram apagados com sucesso!")
            # banco.close()
        else:
            print(f"A tabela {tabela} está vazia")
    except NameError as err:
        get_log("ERRO DELETE QUERY")
        get_log(err)
        print("Erro delete query", err)


# Adiciona o item dataatualizacao na lista assim salvando no banco com a data e hora que o script foi executado
def current_datetime_query(lista):
    lista_retorno = []
    now = datetime.now()
    hora_atualizacao = now.strftime("%d/%m/%Y %H:%M:%S")
    for nova_lista in lista:
        nova_lista.update({'dataatualizacao': hora_atualizacao})
        lista_retorno.append(nova_lista)

    return lista_retorno


def get_idtarefas(tabela, banco):
    try:
        lista_retorno = []
        cur = banco.cursor()
        cur.execute(f"""SELECT * FROM {tabela}""")
        for ids in cur.fetchall():
            lista_retorno.append({'id': ids[0],
                                  'atividade': ids[1]})

        return lista_retorno
    except NameError as err:
        get_log("ERRO GET ID TAREFAS")
        get_log(err)
        print("Erro get idtarefas", err)


def get_idtarefas_status(banco):
    try:
        lista_retorno = []
        cur = banco.cursor()
        cur.execute(f"""SELECT id, situacao FROM tarefas
                    WHERE situacao = 'Concluída'""")
        for ids in cur.fetchall():
            lista_retorno.append({'id': ids[0],
                                  'situacao': ids[1]})

        return lista_retorno
    except NameError as err:
        get_log("ERRO GET ID TAREFAS")
        get_log(err)
        print("Erro get idtarefas", err)


def get_idbeneficios(tabela, banco):
    try:
        lista_retorno = []
        cur = banco.cursor()
        cur.execute(f"""SELECT * FROM {tabela}""")
        for ids in cur.fetchall():
            lista_retorno.append({'id': ids[0],
                                  'atividade': ids[1]})

        return lista_retorno
    except NameError as err:
        get_log("ERRO GET ID BENEFICIOS")
        get_log(err)
        print("Erro get idbeneficios", err)


def delete_datas(banco):
    lista_tabelas = ['achados_auditoria',  'analise_auditoria', 'analise_preliminar',  'apuracao_preliminar',
                     'atividade_continuada', 'auditorias', 'auto_avaliacao_iacm', 'comunicacao_auditoria',
                     'escopo_auditoria', 'execucao_consultoria', 'item_analise_tce', 'item_trabalho_atividade',
                     'item_trabalho_projeto', 'kpa_iacm', 'matriz_planejamento', 'minuta_posicionamento',
                     'monitoramento',  'planejamento_consultoria', 'projeto_geral', 'relatorio_final',
                     'relatorio_preliminar', 'resultados_consultoria', 'termo_compromisso_consultoria',
                     'tarefas', 'tarefas_id', 'beneficios', 'beneficios_id']

    try:
        for table in lista_tabelas:
            delete_query = (f"""DELETE FROM {table}""")
            banco.cursor().execute(delete_query)
            print(f"Dados da tabela {table} foram apagados com sucesso!")
            banco.commit()
        print("Todos os dados foram apagados")
    except NameError as err:
        get_log("Erro ao deletar os dados")
        get_log(err)
        print("Erro ao deletar dados")
