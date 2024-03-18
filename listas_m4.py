import importacoes_m4
from db import get_idtarefas, db_connection

def dicionario():
    # Nome do campo: lista que deve ser criada
    dict = {'CGE - Matriz de Planejamento': 'lista_matriz_planejamento',
            'CGE - Minuta de Posicionamento': 'lista_minuta_posicionamento',
            'CGE - Planejamento (Consultoria)': 'lista_planejamento_consultoria',
            'CGE - Relatório Final': 'lista_relatorio_final',
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

        if tipo == 'CGE - Matriz de Planejamento':
            lista_matriz_planejamento = []
        elif tipo == 'CGE - Minuta de Posicionamento':
            lista_minuta_posicionamento = []
        elif tipo == 'CGE - Planejamento (Consultoria)':
            lista_planejamento_consultoria = []
        elif tipo == 'CGE - Relatório Final':
            lista_relatorio_final = []
        else:
            pass
            #return("Erro ao criar as listas")
    
    for i, tarefa in enumerate(data):
        # Lista de matriz planejamento
        if tarefa['atividade'] == lista_titulo_atividade[0]:
            lista_matriz_planejamento.append(tarefa['id'])
        # Lista de minuta posicionamento
        elif tarefa['atividade'] == lista_titulo_atividade[1]:
            lista_minuta_posicionamento.append(tarefa['id'])
        # Lista de planejamento consultoria
        elif tarefa['atividade'] == lista_titulo_atividade[2]:
            lista_planejamento_consultoria.append(tarefa['id'])
        # Lista de relatorio final
        elif tarefa['atividade'] == lista_titulo_atividade[3]:
            lista_relatorio_final.append(tarefa['id'])
        else:
            pass
            #return("Erro ao salvar os dados")
        
    # def matriz planejamento
    importacoes_m4.matrizplanejamento.get_matriz_planejamento(lista_matriz_planejamento)
    # def minuta posicionamento
    importacoes_m4.minutaposicionamento.get_minuta_posicionamento(lista_minuta_posicionamento)
    # def planejamento consultoria
    importacoes_m4.planejamentoconsultoria.get_planejamento_consultoria(lista_planejamento_consultoria)
    # def relatorio final
    importacoes_m4.relatoriofinal.get_relatorio_final(lista_relatorio_final)
listar()
    