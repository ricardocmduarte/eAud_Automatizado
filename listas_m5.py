import importacoes_m5
from db import get_idtarefas, db_connection

def dicionario():
    # Nome do campo: lista que deve ser criada
    dict = {'CGE - Relatório Preliminar': 'lista_relatorio_preliminar', 
            'CGE - Resultados (Consultoria)': 'lista_resultados_consultoria',
            'CGE - Termo de Compromisso (Consultoria)': 'lista_termo_compromisso_consultoria',
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

        if tipo == 'CGE - Relatório Preliminar':
            lista_relatorio_preliminar = []
        elif tipo == 'CGE - Resultados (Consultoria)':
            lista_resultados_consultoria = []
        if tipo == 'CGE - Termo de Compromisso (Consultoria)':
            lista_termo_compromisso_consultoria = []
        else:
            pass
            #return("Erro ao criar as listas")
    
    for i, tarefa in enumerate(data):
        #lista de Relatório Preliminar
        if tarefa['atividade'] == lista_titulo_atividade[0]:
            lista_relatorio_preliminar.append(tarefa['id'])
        #lista de Resultados Consultória
        elif tarefa['atividade'] == lista_titulo_atividade[1]:
            lista_resultados_consultoria.append(tarefa['id'])
        #lista de Termo Compromisso Consultória
        elif tarefa['atividade'] == lista_titulo_atividade[2]:
            lista_termo_compromisso_consultoria.append(tarefa['id'])
        else:
            pass
            #return("Erro ao salvar os dados")
    
    #def Relatório Preliminar
    importacoes_m5.relatoriopreliminar.get_relatorio_preliminar(lista_relatorio_preliminar)
    #def Resultados Consultória
    importacoes_m5.resultadosconsultoria.get_resultados_consultoria(lista_resultados_consultoria)
    # def Termo Compromisso Consultória
    importacoes_m5.termocompromissoconsultoria.get_termo_compromisso_consultoria(lista_termo_compromisso_consultoria)
listar()





    