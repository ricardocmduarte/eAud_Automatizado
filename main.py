
import tarefas_id
import beneficios_id
import tarefas
import beneficios
import interacao
import listas
#import listas_m
#import listas_m1
#import listas_m2
#import listas_m3
#import listas_m4
#import listas_m5
#import excel_csv
import excel_csv_m1
import finalizar_programa
#import excel_csv_m


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
    #excel_csv.converter()
    excel_csv_m1.converter_m1()
    finalizar_programa.finalizar_programa()
    #excel_csv_m.converter_m()
    


   
   


        



 











