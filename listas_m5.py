import importacoes_m5
from db import get_idtarefas, db_connection

def dicionario():
    # Nome do campo: lista que deve ser criada
    dict = {'CGE - Monitoramento': 'lista_monitoramento',
            #'CGE - Planejamento (Consultoria)': 'lista_planejamento_consultoria',
            #'CGE - Projeto Geral': 'lista_projeto_geral',
            #'CGE - Relatório Final': 'lista_relatorio_final',
            #'CGE - Relatório Preliminar': 'lista_relatorio_preliminar',
            #'CGE - Resultados (Consultoria)': 'lista_resultados_consultoria',
            #'CGE - Termo de Compromisso (Consultoria)': 'lista_termo_compromisso_consultoria',
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

        if tipo == 'CGE - Monitoramento': 
            lista_monitoramento = []
        #elif tipo == 'CGE - Planejamento (Consultoria)': 
        #    lista_planejamento_consultoria = []
        #elif tipo == 'CGE - Projeto Geral': 
        #    lista_projeto_geral = []
        #elif tipo == 'CGE - Relatório Final': 
        #    lista_relatorio_final = []
        #elif tipo == 'CGE - Relatório Preliminar':
        #    lista_relatorio_preliminar = []
        #elif tipo == 'CGE - Resultados (Consultoria)':
        #    lista_resultados_consultoria = []
        #elif tipo == 'CGE - Termo de Compromisso (Consultoria)':
        #    lista_termo_compromisso_consultoria = []
        else:
            pass
            #return("Erro ao criar as listas")
    
    for i, tarefa in enumerate(data):
        #lista de monitoramento
        if tarefa['atividade'] == lista_titulo_atividade[0]:
            lista_monitoramento.append(tarefa['id'])
        ##lista de planejamento consultoria
        #elif tarefa['atividade'] == lista_titulo_atividade[1]:
        #    lista_planejamento_consultoria.append(tarefa['id'])
        ##lista de projeto geral
        #elif tarefa['atividade'] == lista_titulo_atividade[2]:
        #    lista_projeto_geral.append(tarefa['id'])
        ##lista_relatorio_final
        #elif tarefa['atividade'] == lista_titulo_atividade[3]:
        #    lista_relatorio_final.append(tarefa['id']) 
        ##lista de Relatório Preliminar
        #elif tarefa['atividade'] == lista_titulo_atividade[4]:
        #    lista_relatorio_preliminar.append(tarefa['id'])
        ##lista de Resultados Consultória
        #elif tarefa['atividade'] == lista_titulo_atividade[5]:
        #    lista_resultados_consultoria.append(tarefa['id'])
        ##lista de Termo Compromisso Consultória
        #elif tarefa['atividade'] == lista_titulo_atividade[6]:
        #    lista_termo_compromisso_consultoria.append(tarefa['id'])
        else:
            pass
            #return("Erro ao salvar os dados")

    #def Monitoramento
    importacoes_m5.monitoramento.get_monitoramento(lista_monitoramento)        
    ##def Planejamento Consultoria
    #importacoes_m5.planejamentoconsultoria.get_planejamento_consultoria(lista_planejamento_consultoria)
    ##def Projeto Geral
    #importacoes_m5.projetogeral.get_projeto_geral(lista_projeto_geral)
    ##def Relatorio Final
    #importacoes_m5.relatoriofinal.get_relatorio_final(lista_relatorio_final)
    ##def Relatório Preliminar
    #importacoes_m5.relatoriopreliminar.get_relatorio_preliminar(lista_relatorio_preliminar)
    ##def Resultados Consultória
    #importacoes_m5.resultadosconsultoria.get_resultados_consultoria(lista_resultados_consultoria)
    ## def Termo Compromisso Consultória
    #importacoes_m5.termocompromissoconsultoria.get_termo_compromisso_consultoria(lista_termo_compromisso_consultoria)

listar()





    