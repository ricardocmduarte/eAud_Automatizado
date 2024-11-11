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
if __name__ == '__main__':
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