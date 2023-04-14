import psycopg2
import conf.geral as geral
from datetime import datetime
from misc.log import get_log


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
        cur.execute(f"""SELECT id FROM {tabela}""")
        for ids in cur.fetchall():
            lista_retorno.append(ids[0])

        return lista_retorno
    except NameError as err:
        get_log("ERRO GET ID TAREFAS")
        get_log(err)
        print("Erro get idtarefas", err)


def delete_datas(banco):
    lista_tabelas = ['achados_auditoria_pendencias', 'achados_auditoria', 'analise_auditoria_pendencias', 'analise_auditoria',
                     'analise_preliminar_pendencias', 'analise_preliminar', 'auditorias_pendencias', 'auditorias_localidade',
                     'auditorias_unidades_envolvidas', 'auditorias_unidades_auditadas', 'auditorias_arquivos', 'auditorias', 'beneficios_pendencias',
                     'beneficios', 'escopo_auditoria_pendencias', 'escopo_auditoria', 'indicadores', 'localidades', 'matriz_planejamento_pendencias',
                     'matriz_planejamento', 'monitoramento_manifestacao', 'monitoramento_pendencias', 'monitoramento_posicionamento',
                     'monitoramento_unidades', 'monitoramento', 'plano_operacional_pactuacao', 'plano_operacional_pendencias', 'plano_operacional',
                     'plano_trabalho_localidades', 'plano_trabalho_pendencias', 'plano_trabalho_unidades_envolvidas', 'plano_trabalho',
                     'relatorio_auditoria_pendencias', 'relatorio_auditoria', 'tarefas_pendencias', 'tarefas_arquivos', 'tarefas',
                     'unidade_gestores', 'unidade_tipos', 'unidade', 'usuario']

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
