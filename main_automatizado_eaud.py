import tarefas_id
import beneficios_id
import tarefas
import beneficios
import interacao
import listas
import excel_csv_m1
import tarefas_id_datasaver
import beneficios_id_datasaver
import tarefas_datasaver
import beneficios_datasaver
import interacao_datasaver
import atividadecontinuada_datasaver
import auditoria_datasaver
import monitoramento_datasaver
import projetogeral_datasaver
import achadosauditoria_datasaver
import analiseauditoria_datasaver
import analisepreliminar_datasaver
import apuracaopreliminar_datasaver
import autoavaliacaoiacm_datasaver
import comunicacaoauditoria_datasaver
import escopoauditoria_datasaver
import execucaoconsultoria_datasaver
import itemprocessoanalisetce_datasaver
import itemtrabalhoatividade_datasaver
import itemtrabalhoprojeto_datasaver
import kpaiacm_datasaver
import matrizplanejamento_datatasaver
import minutaposicionamento_datasaver
import planejamentoconsultoria_datasaver
import relatoriofinal_datasaver
import relatoriopreliminar_datasaver
import resultadosconsultoria_datasaver
import termocompromissoconsultoria_datasaver
import tarefas_verificador_dados_datasaver
import beneficios_verificador_dados_datasaver
import interacao_verificador_dados_datasaver
import atividadecontinuada_verificador_dados_datasaver
import auditoria_verificador_dados_datasaver
import monitoramento_verificador_dados_datasaver
import projetogeral_verificador_dados_datasaver
import achadosauditoria_verificador_dados_datasaver
import analiseauditoria_verificador_dados_datasaver
import analisepreliminar_verificador_dados_datasaver
import apuracaopreliminar_verificador_dados_datasaver
import autoavaliacaoiacm_verificador_dados_datasaver
import comunicacaoauditoria_verificador_dados_datasaver
import escopoauditoria_verificador_dados_datasaver
import execucaoconsultoria_verificador_dados_datasaver
import itemprocessoanalisetce_verificador_dados_datasaver
import itemtrabalhoatividade_verificador_dados_datasaver
import itemtrabalhoprojeto_verificador_dados_datasaver
import kpaiacm_verificador_dados_datasaver
import matrizplanejamento_verificador_dados_datasaver
import minutaposicionamento_verificador_dados_datasaver
import planejamentoconsultoria_verificador_dados_datasaver
import relatoriofinal_verificador_dados_datasaver
import relatoriopreliminar_verificador_dados_datasaver
import resultadosconsultoria_verificador_dados_datasaver
import termocompromissoconsultoria_verificador_dados_datasaver
import contador_registros_tabelas_eAud
import finalizar_programa

if __name__ == '__main__':
    
    # get_tarefas_id e get_beneficios_id devem ser executados primeiros para adquirirem os ids.
    tarefas_id.get_tarefas_id()
    beneficios_id.get_beneficios_id()   
    # funções para buscar os dados por completo.
    tarefas.get_tarefas()
    beneficios.get_beneficios()
    interacao.get_interacao()
    #listas_m.listar()
    #listas_m1.listar()
    #listas_m2.listar()
    #listas_m3.listar()
    #listas_m4.listar()
    #listas_m5.listar()
    listas.listar()
    excel_csv_m1.converter_m1()
    # get_tarefas e get_beneficios_id devem ser executados primeiros para adquirirem os ids
    tarefas_id_datasaver.db_saver_tarefas_id()
    beneficios_id_datasaver.db_saver_beneficios_id()
    # funções para buscar os dados por completo
    tarefas_datasaver.db_saver_tarefas()
    beneficios_datasaver.db_saver_beneficios()
    interacao_datasaver.db_saver_interacao()
    atividadecontinuada_datasaver.db_saver_atividadecontinuada()
    auditoria_datasaver.db_saver_auditoria()
    monitoramento_datasaver.db_saver_monitoramento()
    projetogeral_datasaver.db_saver_projetogeral()
    achadosauditoria_datasaver.db_saver_achadosauditoria()
    analiseauditoria_datasaver.db_saver_analiseauditoria()
    analisepreliminar_datasaver.db_saver_analisepreliminar()
    apuracaopreliminar_datasaver.db_saver_apuracaopreliminar()
    autoavaliacaoiacm_datasaver.db_saver_autoavaliacaoiacm()
    comunicacaoauditoria_datasaver.db_saver_comunicacaoauditoria()
    escopoauditoria_datasaver.db_saver_escopoauditoria()
    execucaoconsultoria_datasaver.db_saver_execucaoconsultoria()
    itemprocessoanalisetce_datasaver.db_saver_itemprocessoanalisetce()
    itemtrabalhoatividade_datasaver.db_saver_itemtrabalhoatividade()
    itemtrabalhoprojeto_datasaver.db_saver_itemtrabalhoprojeto()
    kpaiacm_datasaver.db_saver_kpaiacm()
    matrizplanejamento_datatasaver.db_saver_matrizplanejamento()
    minutaposicionamento_datasaver.db_saver_minutaposicionamento()
    planejamentoconsultoria_datasaver.db_saver_planejamentoconsultoria()
    relatoriofinal_datasaver.db_saver_relatoriofinal()
    relatoriopreliminar_datasaver.db_saver_relatoriopreliminar()
    resultadosconsultoria_datasaver.db_saver_resultadosconsultoria()
    termocompromissoconsultoria_datasaver.db_saver_termocompromissoconsultoria()
    # funções para executar os verificadores de dados com base nas tabelas tarefas_id e beneficios_id 
    tarefas_verificador_dados_datasaver.tarefas_verificador_dados()
    beneficios_verificador_dados_datasaver.beneficios_verificador_dados()
    interacao_verificador_dados_datasaver.interacao_verificador_dados()
    atividadecontinuada_verificador_dados_datasaver.atividade_continuada_verificador_dados()
    auditoria_verificador_dados_datasaver.auditoria_verificador_dados()
    monitoramento_verificador_dados_datasaver.monitoramento_verificador_dados()
    projetogeral_verificador_dados_datasaver.projeto_geral_verificador_dados()
    achadosauditoria_verificador_dados_datasaver.achados_auditoria_vericador_dados()
    analiseauditoria_verificador_dados_datasaver.analise_auditoria_verificador_dados()
    analisepreliminar_verificador_dados_datasaver.analise_preliminar_verificador_dados()
    apuracaopreliminar_verificador_dados_datasaver.apuracao_preliminar_verificador_dados()
    autoavaliacaoiacm_verificador_dados_datasaver.autoavaliacao_iacm_verificador_dados()
    comunicacaoauditoria_verificador_dados_datasaver.comunicacao_auditoria_verificador_dados()
    escopoauditoria_verificador_dados_datasaver.escopo_auditoria_verificdor_dados()
    execucaoconsultoria_verificador_dados_datasaver.execucao_consultoria_verificador_dados()
    itemprocessoanalisetce_verificador_dados_datasaver.itemprocesso_analise_tce_verificador_dados()
    itemtrabalhoatividade_verificador_dados_datasaver.item_trabalho_atividade_verificador_dados()
    itemtrabalhoprojeto_verificador_dados_datasaver.item_trabalho_projeto_verificador_dados()
    kpaiacm_verificador_dados_datasaver.kpa_iacm_verificador_dados()
    matrizplanejamento_verificador_dados_datasaver.matriz_planejamento_verificador_dados()
    minutaposicionamento_verificador_dados_datasaver.minuta_posicionamento_verificador_dados()
    planejamentoconsultoria_verificador_dados_datasaver.planejamento_consultoria_verificador_dados()
    relatoriofinal_verificador_dados_datasaver.relatorio_final_verificador_dados()
    relatoriopreliminar_verificador_dados_datasaver.relatorio_preliminar_verificador_dados()
    resultadosconsultoria_verificador_dados_datasaver.resultados_consultoria_verificador_dados()
    termocompromissoconsultoria_verificador_dados_datasaver.termo_compromisso_consultoria_verificador_dados()
    contador_registros_tabelas_eAud.principal()    
    finalizar_programa.finalizar_programa() 