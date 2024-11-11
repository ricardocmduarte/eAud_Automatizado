import importacoes_teste
from db_teste import get_idtarefas_teste, db_connection_teste



def dicionario_teste():
    # nome do campo: lista que deve ser criada
    dict = {'CGE - Achados_Teste': 'lista_achados_teste',
            'CGE - Análises da Auditoria_Teste': 'lista_analise_auditoria_teste',
            'CGE - Análise Preliminar_Teste': 'lista_analise_preliminar_teste',
            'CGE - Apuração Preliminar_Teste': 'lista_apuracao_preliminar_teste',
            'CGE - Atividade Continuada_Teste': 'lista_atividade_continuada_teste',
            'CGE - Auditoria_Teste': 'lista_auditoria_teste',
            'Autoavaliação IA-CM_Teste': 'lista_ia_cm_teste',
            'CGE - Comunicação de Auditoria_Teste': 'lista_comunicacao_auditoria_teste',
            'CGE - Escopo da Auditoria_Teste': 'lista_escopo_auditoria_teste',
            'CGE - Execução (Consultoria_Teste)': 'lista_execucao_consultoria_teste',
            'CGEMG - Item de Processo (Análise de TCE_Teste)': 'lista_item_processo_teste',
            'CGE - Item de Trabalho (Atividade_Teste)': 'lista_item_trabalho_atividade_teste',
            'CGE - Item de Trabalho (Projeto_Teste)': 'lista_item_trabalho_projeto_teste',
            'KPA IACM_Teste': 'lista_kpa_iacm_teste',
            'CGE - Matriz de Planejamento_Teste': 'lista_matriz_planejamento_teste',
            'CGE - Minuta de Posicionamento_Teste': 'lista_minuta_posicionamento_teste',
            'CGE - Monitoramento_Teste': 'lista_monitoramento_teste',
            'CGE - Planejamento (Consultoria_Teste)': 'lista_planejamento_consultoria_teste',
            'CGE - Projeto Geral_Teste': 'lista_projeto_geral_teste',
            'CGE - Relatório Final_Teste': 'lista_relatorio_final_teste',
            'CGE - Relatório Preliminar_Teste': 'lista_relatorio_preliminar_teste',
            'CGE - Resultados (Consultoria_Teste)': 'lista_resultados_consultoria_teste',
            'CGE - Termo de Compromisso (Consultoria_Teste)': 'lista_termo_compromisso_consultoria_teste',
            }

    lista_titulo_atividade_teste = list(dict.keys())
    dict_value_teste = list(dict.values())

    return (lista_titulo_atividade_teste, dict_value_teste)


def listar_teste():
    banco = db_connection_teste()
    data = get_idtarefas_teste('tarefas_id_teste', banco)
    lista_dicionario_teste = dicionario_teste()
    lista_titulo_atividade = lista_dicionario_teste[0]

    for i, tipo in enumerate(lista_titulo_atividade):

        if tipo == 'CGE - Achados_Teste':
            lista_achados_teste = []
        elif tipo == 'CGE - Análise Preliminar_Teste':
            lista_analise_preliminar_teste = []
        elif tipo == 'CGE - Análises da Auditoria_Teste':
            lista_analise_auditoria_teste = []
        elif tipo == 'CGE - Apuração Preliminar_Teste':
            lista_apuracao_preliminar_teste = []
        elif tipo == 'CGE - Atividade Continuada_Teste':
            lista_atividade_continuada_teste = []
        elif tipo == 'CGE - Auditoria_Teste':
            lista_auditoria_teste = []
        elif tipo == 'Autoavaliação IA-CM_Teste':
            lista_ia_cm_teste = []
        elif tipo == 'CGE - Comunicação de Auditoria_Teste':
            lista_comunicacao_auditoria_teste = []
        elif tipo == 'CGE - Escopo da Auditoria_Teste':
            lista_escopo_auditoria_teste = []
        elif tipo == 'CGE - Execução (Consultoria_Teste)':
            lista_execucao_consultoria_teste = []
        elif tipo == 'CGE - Item de Trabalho (Atividade_Teste)':
            lista_item_trabalho_atividade_teste = []
        elif tipo == 'CGEMG - Item de Processo (Análise de TCE_Teste)':
            lista_item_processo_analise_tce_teste = []
        elif tipo == 'CGE - Item de Trabalho (Projeto_Teste)':
            lista_item_trabalho_projeto_teste = []
        elif tipo == 'KPA IACM_Teste':
            lista_kpa_iacm_teste = []
        elif tipo == 'CGE - Matriz de Planejamento_Teste':
            lista_matriz_planejamento_teste = []
        elif tipo == 'CGE - Minuta de Posicionamento_Teste':
            lista_minuta_posicionamento_teste = []
        elif tipo == 'CGE - Monitoramento_Teste':
            lista_monitoramento_teste = []
        elif tipo == 'CGE - Planejamento (Consultoria_Teste)':
            lista_planejamento_consultoria_teste = []
        elif tipo == 'CGE - Projeto Geral_Teste':
            lista_projeto_geral_teste = []
        elif tipo == 'CGE - Relatório Final_Teste':
            lista_relatorio_final_teste = []
        elif tipo == 'CGE - Relatório Preliminar_Teste':
            lista_relatorio_preliminar_teste = []
        elif tipo == 'CGE - Resultados (Consultoria_Teste)':
            lista_resultados_consultoria_teste = []
        elif tipo == 'CGE - Termo de Compromisso (Consultoria_Teste)':
            lista_termo_compromisso_consultoria_teste = []
        else:
            return ("Erro ao criar as listas")

    for i, tarefa in enumerate(data):
        # lista de achados
        if tarefa['atividade'] == lista_titulo_atividade[0]:
            lista_achados_teste.append(tarefa['id'])
        # lista de analise auditoria
        elif tarefa['atividade'] == lista_titulo_atividade[1]:
            lista_analise_auditoria_teste.append(tarefa['id'])
        # lista de analise preliminar
        elif tarefa['atividade'] == lista_titulo_atividade[2]:
            lista_analise_preliminar_teste.append(tarefa['id'])
        # lista de apuração preliminar
        elif tarefa['atividade'] == lista_titulo_atividade[3]:
            lista_apuracao_preliminar_teste.append(tarefa['id'])
        # lista de atividade continuada
        elif tarefa['atividade'] == lista_titulo_atividade[4]:
            lista_atividade_continuada_teste.append(tarefa['id'])
        # lista de auditoria
        elif tarefa['atividade'] == lista_titulo_atividade[5]:
            lista_auditoria_teste.append(tarefa['id'])
        # lista de avaliação iacm
        elif tarefa['atividade'] == lista_titulo_atividade[6]:
            lista_ia_cm_teste.append(tarefa['id'])
        # lista de comunicação auditoria
        elif tarefa['atividade'] == lista_titulo_atividade[7]:
            lista_comunicacao_auditoria_teste.append(tarefa['id'])
        # lista de escopo auditoria
        elif tarefa['atividade'] == lista_titulo_atividade[8]:
            lista_escopo_auditoria_teste.append(tarefa['id'])
        # lista de execução consultoria
        elif tarefa['atividade'] == lista_titulo_atividade[9]:
            lista_execucao_consultoria_teste.append(tarefa['id'])
        # lista de item processo analise tce
        elif tarefa['atividade'] == lista_titulo_atividade[10]:
            lista_item_processo_analise_tce_teste.append(tarefa['id'])
        # lista de item trabalho atividade
        elif tarefa['atividade'] == lista_titulo_atividade[11]:
            lista_item_trabalho_atividade_teste.append(tarefa['id'])
        # lista de item trabalho projeto
        elif tarefa['atividade'] == lista_titulo_atividade[12]:
            lista_item_trabalho_projeto_teste.append(tarefa['id'])
         # lista de kpa iacm
        elif tarefa['atividade'] == lista_titulo_atividade[13]:
            lista_kpa_iacm_teste.append(tarefa['id'])
        # lista de matriz planejamento
        elif tarefa['atividade'] == lista_titulo_atividade[14]:
            lista_matriz_planejamento_teste.append(tarefa['id'])
        # lista de minuta posicionamento
        elif tarefa['atividade'] == lista_titulo_atividade[15]:
            lista_minuta_posicionamento_teste.append(tarefa['id'])
        # lista de monitoramento
        elif tarefa['atividade'] == lista_titulo_atividade[16]:
            lista_monitoramento_teste.append(tarefa['id'])
        # lista de planejamento consultoria
        elif tarefa['atividade'] == lista_titulo_atividade[17]:
            lista_planejamento_consultoria_teste.append(tarefa['id'])
        # lista de projeto geral
        elif tarefa['atividade'] == lista_titulo_atividade[18]:
            lista_projeto_geral_teste.append(tarefa['id'])
        # lista de relatorio final
        elif tarefa['atividade'] == lista_titulo_atividade[19]:
            lista_relatorio_final_teste.append(tarefa['id'])
        # lista de relatorio preliminar
        elif tarefa['atividade'] == lista_titulo_atividade[20]:
            lista_relatorio_preliminar_teste.append(tarefa['id'])
        # lista de resultados consultoria
        elif tarefa['atividade'] == lista_titulo_atividade[21]:
            lista_resultados_consultoria_teste.append(tarefa['id'])
        # lista de termo compromisso consultoria
        elif tarefa['atividade'] == lista_titulo_atividade[22]:
            lista_termo_compromisso_consultoria_teste.append(tarefa['id'])

        else:
            return ("Erro ao salvar os dados")

    # def achados auditoria
    importacoes_teste.achadosauditoria_teste.get_achados_teste(lista_achados_teste)
    # def analise auditoria
    importacoes_teste.analiseauditoria_teste.get_analise_auditoria_teste(lista_analise_auditoria_teste)
    # def analise preliminar
    importacoes_teste.analisepreliminar_teste.get_analise_preliminar_teste(
        lista_analise_preliminar_teste)
    # def apuração preliminar
    importacoes_teste.apuracaopreliminar_teste.get_apuracao_preliminar_teste(
        lista_apuracao_preliminar_teste)
    # def atividade continuada
    importacoes_teste.atividadecontinuada_teste.get_atividade_continuada_teste(
        lista_atividade_continuada_teste)
    # def auditoria
    importacoes_teste.auditoria_teste.get_auditoria_teste(lista_auditoria_teste)
    # def autoavaliação iacm
    importacoes_teste.autoavaliacaoiacm_teste.get_autoavaliacao_iacm_teste(lista_ia_cm_teste)
    # def comunicacao auditoria
    importacoes_teste.comunicacaoauditoria_teste.get_comunicacao_auditoria_teste(
        lista_comunicacao_auditoria_teste)
    # def escopo auditoria
    importacoes_teste.escopoauditoria_teste.get_escopo_auditoria_teste(lista_escopo_auditoria_teste)
    # def execucao consultoria
    importacoes_teste.execucaoconsultoria_teste.get_execucao_consultoria_teste(
        lista_execucao_consultoria_teste)
    # def item processo analise tce
    importacoes_teste.itemprocessoanalisetce_teste.get_item_processo_analise_tce_teste(
        lista_item_processo_analise_tce_teste)
    # def item trabalho atividade
    importacoes_teste.itemtrabalhoatividade_teste.get_item_trabalho_atividade_teste(
        lista_item_trabalho_atividade_teste)
    # def item trabalho projeto #
    importacoes_teste.itemtrabalhoprojeto_teste.get_item_trabalho_projeto_teste(
        lista_item_trabalho_projeto_teste)
    # def kpa iacm
    importacoes_teste.kpaiacm_teste.get_kpa_iacm_teste(lista_kpa_iacm_teste)
    # def matriz planejamento
    importacoes_teste.matrizplanejamento_teste.get_matriz_planejamento_teste(
        lista_matriz_planejamento_teste)
    # def minuta posicionamento #
    importacoes_teste.minutaposicionamento_teste.get_minuta_posicionamento_teste(
        lista_minuta_posicionamento_teste)
    # def monitoramento #
    importacoes_teste.monitoramento_teste.get_monitoramento_teste(lista_monitoramento_teste)
    # def planejamento consultoria #
    importacoes_teste.planejamentoconsultoria_teste.get_planejamento_consultoria_teste(
        lista_planejamento_consultoria_teste)
    # def projeto geral #
    importacoes_teste.projetogeral_teste.get_projeto_geral_teste(lista_projeto_geral_teste)
    # def relatorio final
    importacoes_teste.relatoriofinal_teste.get_relatorio_final_teste(lista_relatorio_final_teste)
    # def relatorio preliminar
    importacoes_teste.relatoriopreliminar_teste.get_relatorio_preliminar_teste(
        lista_relatorio_preliminar_teste)
    # def resultado consultoria
    importacoes_teste.resultadosconsultoria_teste.get_resultados_consultoria_teste(
        lista_resultados_consultoria_teste)
    # def termo compromisso consultoria
    importacoes_teste.termocompromissoconsultoria_teste.get_termo_compromisso_consultoria_teste(
        lista_termo_compromisso_consultoria_teste)
listar_teste()