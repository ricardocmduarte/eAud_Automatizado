import listas
import tarefas
import beneficios
import beneficios_id

if __name__ == '__main__':
    # get_tarefas e get_beneficios_id devem ser executados primeiros para adquirirem os ids
    tarefas.get_tarefas()
    beneficios_id.get_beneficios_id()

    # funções para buscar os dados por completo
    beneficios.get_beneficios()
    listas.listar()
