import database.db as db
from misc.log import get_log


def salvar_dados(resultado_array):
    try:
        banco = db.db_connection()
        cur = banco.cursor()

        for tarefa in resultado_array:
            lista = {(
                tarefa['id'],
                tarefa['atividade']
            )}

            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (
                f"""INSERT INTO tarefas (id, atividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log("Tarefas salvo com sucesso")

        banco.commit()
        print("Fechando conexão com o banco")

        banco.close()
        get_log(
            '--------------------------------------------------------------------------------')
        return print("Conexão encerrada")

    except NameError as err:
        get_log("Erro ao salvar os dados get_tarefas".upper())
        get_log(err)
        return print("Erro ao salvar os dados get_tarefas", err)
