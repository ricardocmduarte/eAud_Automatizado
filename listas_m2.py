import importacoes_m2
from db import get_idtarefas, db_connection

def dicionario():
    # Nome do campo: lista que deve ser criada
    dict = {'Autoavaliação IA-CM': 'lista_ia_cm',
            'CGE - Comunicação de Auditoria': 'lista_comunicacao_auditoria',
            'CGE - Escopo da Auditoria': 'lista_escopo_auditoria',
            'CGE - Execução (Consultoria)': 'lista_execucao_consultoria',
            }

    lista_titulo_atividade = list(dict.keys())
    dict_value = list(dict.values())

    return(lista_titulo_atividade, dict_value)

def listar():
    banco = db_connection()
    data = get_idtarefas('tarefas_id_teste', banco)
    lista_dicionario = dicionario()
    lista_titulo_atividade = lista_dicionario[0]

    for i, tipo in enumerate(lista_titulo_atividade):

        if tipo == 'Autoavaliação IA-CM': 
            lista_ia_cm = []
        elif tipo == 'CGE - Comunicação de Auditoria': 
            lista_comunicacao_auditoria = []
        elif tipo == 'CGE - Escopo da Auditoria': 
            lista_escopo_auditoria = []
        elif tipo == 'CGE - Execução (Consultoria)': 
            lista_execucao_consultoria = []
        else:
            pass
            #return("Erro ao criar as listas")
    
    for i, tarefa in enumerate(data):
        #Lista de Autoavaliação IA-CM
        if tarefa['atividade'] == lista_titulo_atividade[0]:
            lista_ia_cm.append(tarefa['id'])
        #Lista de Comunicação de Auditoria
        elif tarefa['atividade'] == lista_titulo_atividade[1]:
            lista_comunicacao_auditoria.append(tarefa['id'])
        #Lista de Escopo da Auditoria
        elif tarefa['atividade'] == lista_titulo_atividade[0]:
            lista_escopo_auditoria.append(tarefa['id'])
        #Lista de Execução Consultoria
        elif tarefa['atividade'] == lista_titulo_atividade[3]:
            lista_execucao_consultoria.append(tarefa['id'])
        else:
            pass
            #return("Erro ao salvar os dados")
    # def autoavaliacao ia-cm
    importacoes_m2.autoavaliacaoiacm.get_autoavaliacao_iacm(lista_ia_cm)
    # def comunicacao auditoria
    importacoes_m2.comunicacaoauditoria.get_comunicacao_auditoria(lista_comunicacao_auditoria)
    # def escopo auditoria
    importacoes_m2.escopoauditoria.get_escopo_auditoria(lista_escopo_auditoria)
    # def execucao consultoria
    importacoes_m2.execucaoconsultoria.get_execucao_consultoria(lista_execucao_consultoria)
listar()