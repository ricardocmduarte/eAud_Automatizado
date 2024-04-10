import importacoes_m3
from db import get_idtarefas, db_connection

def dicionario():
    # Nome do campo: lista que deve ser criada
    dict = {'CGEMG - Item de Processo (Análise de TCE)': 'lista_item_processo',
            'CGE - Item de Processo (Análise de TCE)': 'lista_item_processo1',
            'CGE - Item de Trabalho (Atividade)': 'lista_item_trabalho_atividade',
            'CGE - Item de Trabalho (Projeto)': 'lista_item_trabalho_projeto',
            'KPA IACM': 'lista_kpa_iacm',
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

        if tipo == 'CGEMG - Item de Processo (Análise de TCE)':
            lista_item_processo = []
        elif tipo == 'CGE - Item de Processo (Análise de TCE)':
            lista_item_processo1 = []
        elif tipo == 'CGE - Item de Trabalho (Atividade)':
            lista_item_trabalho_atividade = []
        elif tipo == 'CGE - Item de Trabalho (Projeto)':
           lista_item_trabalho_projeto = []
        elif tipo == 'KPA IACM':
            lista_kpa_iacm = []
        else:
            pass
            #return("Erro ao criar as listas")
        
    for i, tarefa in enumerate(data):
        # Lista item processo analise tce
        if tarefa['atividade'] == lista_titulo_atividade[0]:
            lista_item_processo.append(tarefa['id'])
        elif tarefa['atividade'] == lista_titulo_atividade[1]:
            lista_item_processo1.append(tarefa['id'])
        # Lista item trabalho atividade
        elif tarefa['atividade'] == lista_titulo_atividade[2]:
            lista_item_trabalho_atividade.append(tarefa['id'])
        # Lista item trabalho projeto
        elif tarefa['atividade'] == lista_titulo_atividade[3]:
            lista_item_trabalho_projeto.append(tarefa['id'])
        # Lista kpa iacm
        elif tarefa['atividade'] == lista_titulo_atividade[4]:
            lista_kpa_iacm.append(tarefa['id'])
        else:
            pass
            #return("Erro ao salvar os dados")

    # def item processo analise tce
    importacoes_m3.itemprocessoanalisetce.get_item_processo_analise_tce(lista_item_processo)
    importacoes_m3.itemprocessoanalisetce.get_item_processo_analise_tce(lista_item_processo1)
    # def item tarbalho atividade
    importacoes_m3.itemtrabalhoatividade.get_item_trabalho_atividade(lista_item_trabalho_atividade)
    # def item trabalho projeto
    importacoes_m3.itemtrabalhoprojeto.get_item_trabalho_projeto(lista_item_trabalho_projeto)
    # def kpa iacm
    importacoes_m3.kpaiacm.get_kpa_iacm(lista_kpa_iacm) 

listar()
