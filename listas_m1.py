import importacoes_m1
from db import get_idtarefas, db_connection

def dicionario():
    # Nome do campo : Listas que deve ser criada
    dict = {#'CGE - Achados': 'lista_achados',
            #'CGE - Análises da Auditoria': 'lista_analises_auditoria',
            'CGE - Análise Preliminar': 'lista_analises_preliminar',
            #'CGE - Apuração Preliminar': 'lista_apuracao_preliminar',
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
        
        #if tipo == 'CGE - Achados':
        #   lista_achados = []
        #elif tipo == 'CGE - Análises da Auditoria':
        #    lista_analises_auditoria = []
        if tipo == 'CGE - Análise Preliminar': 
            lista_analises_preliminar = []
        #elif tipo == 'CGE - Apuração Preliminar': 
        #    lista_apuracao_preliminar = []
        else:
            pass
            #return("Erro ao criar as listas")
    
    for i, tarefa in enumerate(data):
        ##Lista de Achados da Auditoria
        #if tarefa['atividade'] == lista_titulo_atividade[0]:
        #    lista_achados.append(tarefa['id'])
        ##Lista de Análises da Auditoria
        #elif tarefa['atividade'] == lista_titulo_atividade[1]:
        #    lista_analises_auditoria.append(tarefa['id'])
        #Lista de Análises Preliminar
        if tarefa['atividade'] == lista_titulo_atividade[0]:
            lista_analises_preliminar.append(tarefa['id'])
        ##Lista de Apuração Preliminar
        #elif tarefa['atividade'] == lista_titulo_atividade[3]:
        #    lista_apuracao_preliminar.append(tarefa['id'])
        else:
            pass
            #return ("Erro ao salvar os dados")
    
    ## def Achados Auditoria
    #importacoes_m1.achadosauditoria.get_achados(lista_achados)
    ## def Análises da Auditoria
    #importacoes_m1.analiseauditoria.get_analise_auditoria(lista_analises_auditoria)
    # def Análises Preliminar
    importacoes_m1.analisepreliminar.get_analise_preliminar(lista_analises_preliminar)
    ## def Apuração Preliminar
    #importacoes_m1.apuracaopreliminar.get_apuracao_preliminar(lista_apuracao_preliminar)
listar()