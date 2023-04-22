import listas
import tarefas
import beneficios
import beneficios_id

if __name__ == '__main__':
    # get_tarefas e get_beneficios_id devem ser executados primeiros para adquirirem os ids
    beneficios_id.get_beneficios_id()
    tarefas.get_tarefas()

    # funções para buscar os dados por completo
    beneficios.get_beneficios()
    listas.listar()
