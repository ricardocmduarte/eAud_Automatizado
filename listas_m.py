import importacoes_m
from db import get_idtarefas, db_connection


def dicionario():
    # nome do campo: lista que deve ser criada
    dict = {'CGE - Monitoramento': 'lista_monitoramento',
            'CGE - Auditoria': 'lista_auditoria',
            'CGE - Atividade Continuada': 'lista_atividade_continuada',
            'CGE - Projeto Geral': 'lista_projeto_geral',
            }

    lista_titulo_atividade = list(dict.keys())
    dict_value = list(dict.values())

    return (lista_titulo_atividade, dict_value)


def listar():
    banco = db_connection()
    data = get_idtarefas('tarefas_id_teste', banco)
    lista_dicionario = dicionario()
    lista_titulo_atividade = lista_dicionario[0]

    for i, tipo in enumerate(lista_titulo_atividade):
        if tipo == 'CGE - Monitoramento':
            lista_monitoramento = []
        elif tipo == 'CGE - Auditoria':
            lista_auditoria = []
        elif tipo == 'CGE - Atividade Continuada':
            lista_atividade_continuada = []      
        elif tipo == 'CGE - Projeto Geral':
            lista_projeto_geral = []
        else:
            pass
            #return ("Erro ao criar as listas")

    for i, tarefa in enumerate(data):
        # lista de monitoramento
        if tarefa['atividade'] == lista_titulo_atividade[0]:
            lista_monitoramento.append(tarefa['id'])
        # lista de auditoria
        elif tarefa['atividade'] == lista_titulo_atividade[1]: 
            lista_auditoria.append(tarefa['id'])
        # lista de atividade continuada
        elif tarefa['atividade'] == lista_titulo_atividade[2]:
            lista_atividade_continuada.append(tarefa['id'])
        # lista de projeto geral
        elif tarefa['atividade'] == lista_titulo_atividade[3]: 
            lista_projeto_geral.append(tarefa['id'])

        else:
            pass
            #return ("Erro ao salvar os dados")

    # def monitoramento #
    importacoes_m.monitoramento.get_monitoramento(lista_monitoramento)    
    # def auditoria
    importacoes_m.auditoria.get_auditoria(lista_auditoria)
    # def atividade continuada
    importacoes_m.atividadecontinuada.get_atividade_continuada(lista_atividade_continuada)
    # def projeto geral #
    importacoes_m.projetogeral.get_projeto_geral(lista_projeto_geral)
listar()