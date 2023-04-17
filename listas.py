import importacoes
from db import get_idtarefas, db_connection


def dicionario():
    # nome do campo: lista que deve ser criada
    dict = {'Autoavaliação IA-CM': 'lista_ia_cm',
            'CGE - Achados': 'lista_achados',
            'CGE - Análise Preliminar': 'lista_analise_preliminar',
            'CGE - Análises da Auditoria': 'lista_analise_auditoria',
            'CGE - Apuração Preliminar': 'lista_apuracao_preliminar',
            'CGE - Atividade Continuada': 'lista_atividade_continuada',
            'CGE - Auditoria': 'lista_auditoria',
            'CGE - Comunicação de Auditoria': 'lista_comunicacao_auditoria',
            'CGE - Escopo da Auditoria': 'lista_escopo_auditoria',
            'CGE - Execução (Consultoria)': 'lista_execucao_consultoria',
            'CGE - Item de Trabalho (Atividade)': 'lista_item_trabalho_atividade',
            'CGE - Item de Trabalho (Projeto)': 'lista_item_trabalho_projeto',
            'CGE - Matriz de Planejamento': 'lista_matriz_planejamento',
            'CGE - Minuta de Posicionamento': 'lista_minuta_posicionamento',
            'CGE - Monitoramento': 'lista_monitoramento',
            'CGE - Planejamento (Consultoria)': 'lista_planejamento_consultoria',
            'CGE - Projeto Geral': 'lista_projeto_geral',
            'CGE - Relatório Final': 'lista_relatorio_final',
            'CGE - Relatório Preliminar': 'lista_relatorio_preliminar',
            'CGE - Resultados (Consultoria)': 'lista_resultados_consultoria',
            'CGE - Termo de Compromisso (Consultoria)': 'lista_termo_compromisso_consultoria',
            'CGEMG - Item de Processo (Análise de TCE)': 'lista_item_processo',
            'KPA IACM': 'lista_kpa_iacm'}

    lista_titulo_atividade = list(dict.keys())
    dict_value = list(dict.values())

    return (lista_titulo_atividade, dict_value)


def listar():
    banco = db_connection()
    data = get_idtarefas('tarefas', banco)
    lista_dicionario = dicionario()
    lista_titulo_atividade = lista_dicionario[0]

    for i, tipo in enumerate(lista_titulo_atividade):

        if tipo == 'CGE - Achados':
            lista_achados = []
        elif tipo == 'CGE - Análise Preliminar':
            lista_analise_preliminar = []
        elif tipo == 'CGE - Análises da Auditoria':
            lista_analise_auditoria = []
        elif tipo == 'CGE - Apuração Preliminar':
            lista_apuracao_preliminar = []
        elif tipo == 'CGE - Atividade Continuada':
            lista_atividade_continuada = []
        elif tipo == 'CGE - Auditoria':
            lista_auditoria = []
        elif tipo == 'Autoavaliação IA-CM':
            lista_ia_cm = []
        elif tipo == 'CGE - Comunicação de Auditoria':
            lista_comunicacao_auditoria = []
        elif tipo == 'CGE - Escopo da Auditoria':
            lista_escopo_auditoria = []
        elif tipo == 'CGE - Execução (Consultoria)':
            lista_execucao_consultoria = []
        elif tipo == 'CGE - Item de Trabalho (Atividade)':
            lista_item_trabalho_atividade = []
        elif tipo == 'CGE - Item de Trabalho (Projeto)':
            lista_item_trabalho_projeto = []
        elif tipo == 'CGE - Matriz de Planejamento':
            lista_matriz_planejamento = []
        elif tipo == 'CGE - Minuta de Posicionamento':
            lista_minuta_posicionamento = []
        elif tipo == 'CGE - Monitoramento':
            lista_monitoramento = []
        elif tipo == 'CGE - Planejamento (Consultoria)':
            lista_planejamento_consultoria = []
        elif tipo == 'CGE - Projeto Geral':
            lista_projeto_geral = []
        elif tipo == 'CGE - Relatório Final':
            lista_relatorio_final = []
        elif tipo == 'CGE - Relatório Preliminar':
            lista_relatorio_preliminar = []
        elif tipo == 'CGE - Resultados (Consultoria)':
            lista_resultados_consultoria = []
        elif tipo == 'CGE - Termo de Compromisso (Consultoria)':
            lista_termo_compromisso_consultoria = []
        elif tipo == 'CGEMG - Item de Processo (Análise de TCE)':
            lista_item_processo_analise_tce = []
        elif tipo == 'KPA IACM':
            lista_kpa_iacm = []
        else:
            return ("Erro ao criar as listas")

    for i, tarefa in enumerate(data):
        # lista de achados
        if tarefa['atividade'] == lista_titulo_atividade[1]:
            lista_achados.append(tarefa['id'])
        # lista de analise preliminar
        elif tarefa['atividade'] == lista_titulo_atividade[2]:
            lista_analise_preliminar.append(tarefa['id'])
        # lista de analise auditoria
        elif tarefa['atividade'] == lista_titulo_atividade[3]:
            lista_analise_auditoria.append(tarefa['id'])
        # lista de apuração preliminar
        elif tarefa['atividade'] == lista_titulo_atividade[4]:
            lista_apuracao_preliminar.append(tarefa['id'])
        # lista de atividade continuada
        elif tarefa['atividade'] == lista_titulo_atividade[5]:
            lista_atividade_continuada.append(tarefa['id'])
        # lista de auditoria
        elif tarefa['atividade'] == lista_titulo_atividade[6]:
            lista_auditoria.append(tarefa['id'])
        # lista de avaliação iacm
        elif tarefa['atividade'] == lista_titulo_atividade[0]:
            lista_ia_cm.append(tarefa['id'])
        # lista de comunicação auditoria
        elif tarefa['atividade'] == lista_titulo_atividade[7]:
            lista_comunicacao_auditoria.append(tarefa['id'])
        # lista de escopo auditoria
        elif tarefa['atividade'] == lista_titulo_atividade[8]:
            lista_escopo_auditoria.append(tarefa['id'])
        # lista de execução consultoria
        elif tarefa['atividade'] == lista_titulo_atividade[9]:
            lista_execucao_consultoria.append(tarefa['id'])
        # lista de item trabalho atividade
        elif tarefa['atividade'] == lista_titulo_atividade[10]:
            lista_item_trabalho_atividade.append(tarefa['id'])
        # lista de item trabalho projeto
        elif tarefa['atividade'] == lista_titulo_atividade[11]:
            lista_item_trabalho_projeto.append(tarefa['id'])
        # lista de matriz planejamento
        elif tarefa['atividade'] == lista_titulo_atividade[12]:
            lista_matriz_planejamento.append(tarefa['id'])
        # lista de minuta posicionamento
        elif tarefa['atividade'] == lista_titulo_atividade[13]:
            lista_minuta_posicionamento.append(tarefa['id'])
        # lista de monitoramento
        elif tarefa['atividade'] == lista_titulo_atividade[14]:
            lista_monitoramento.append(tarefa['id'])
        # lista de planejamento consultoria
        elif tarefa['atividade'] == lista_titulo_atividade[15]:
            lista_planejamento_consultoria.append(tarefa['id'])
        # lista de projeto geral
        elif tarefa['atividade'] == lista_titulo_atividade[16]:
            lista_projeto_geral.append(tarefa['id'])
        # lista de relatorio final
        elif tarefa['atividade'] == lista_titulo_atividade[17]:
            lista_relatorio_final.append(tarefa['id'])
        # lista de relatorio preliminar
        elif tarefa['atividade'] == lista_titulo_atividade[18]:
            lista_relatorio_preliminar.append(tarefa['id'])
        # lista de resultados consultoria
        elif tarefa['atividade'] == lista_titulo_atividade[19]:
            lista_resultados_consultoria.append(tarefa['id'])
        # lista de termo compromisso consultoria
        elif tarefa['atividade'] == lista_titulo_atividade[20]:
            lista_termo_compromisso_consultoria.append(tarefa['id'])
        # lista de item processo
        elif tarefa['atividade'] == lista_titulo_atividade[21]:
            lista_item_processo_analise_tce.append(tarefa['id'])
        # lista de kpa iacm
        elif tarefa['atividade'] == lista_titulo_atividade[22]:
            lista_kpa_iacm.append(tarefa['id'])
        else:
            return ("Erro ao salvar os dados")

    importacoes.achadosauditoria.get_achados(lista_achados)
    importacoes.analisepreliminar.get_analise_preliminar(
        lista_analise_preliminar)
    importacoes.analiseauditoria.get_analise_auditoria(lista_analise_auditoria)
    importacoes.apuracaopreliminar.get_apuracao_preliminar(
        lista_apuracao_preliminar)
    importacoes.atividadecontinuada.get_atividade_continuada(
        lista_atividade_continuada)
    importacoes.auditoria.get_auditoria(lista_auditoria)
    importacoes.autoavaliacaoiacm.get_autoavaliacao_iacm(lista_ia_cm)
    importacoes.comunicacaoauditoria.get_comunicacao_auditoria(
        lista_comunicacao_auditoria)
    importacoes.escopoauditoria.get_escopo_auditoria(lista_escopo_auditoria)
    importacoes.execucaoconsultoria.get_execucao_consultoria(
        lista_execucao_consultoria)
    importacoes.itemprocessoanalisetce.get_item_processo_analise_tce(
        lista_item_processo_analise_tce)
    importacoes.itemtrabalhoatividade.get_item_trabalho_atividade(
        lista_item_trabalho_atividade)
    importacoes.itemtrabalhoprojeto.get_item_trabalho_projeto(
        lista_item_trabalho_projeto)
    importacoes.matrizplanejamento.get_matriz_planejamento(
        lista_matriz_planejamento)
    importacoes.minutaposicionamento.get_minuta_posicionamento(
        lista_minuta_posicionamento)
    importacoes.monitoramento.get_monitoramento(lista_monitoramento)
    importacoes.planejamentoconsultoria.get_planejamento_consultoria(
        lista_planejamento_consultoria)
    importacoes.projetogeral.get_projeto_geral(lista_projeto_geral)
    importacoes.relatoriofinal.get_relatorio_final(lista_relatorio_final)
    importacoes.relatoriopreliminar.get_relatorio_preliminar(
        lista_relatorio_preliminar)
    importacoes.resultadosconsultoria.get_resultados(
        lista_resultados_consultoria)
    importacoes.termocompromissoconsultoria.get_termo_compromisso(
        lista_termo_compromisso_consultoria)
    importacoes.kpaiacm.get_lista_kpa_iacm(lista_kpa_iacm)


listar()
