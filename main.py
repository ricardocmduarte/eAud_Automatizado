import listas
import tarefas_id
import tarefas
import beneficios
import beneficios_id
import interacao
import excel_csv

if __name__ == '__main__':
    # get_tarefas e get_beneficios_id devem ser executados primeiros para adquirirem os ids
    tarefas_id.get_tarefas_id()
    beneficios_id.get_beneficios_id()

    # funções para buscar os dados por completo
    tarefas.get_tarefas()
    beneficios.get_beneficios()
    listas.listar()
    interacao.get_interacao()

    excel_csv.converter()
