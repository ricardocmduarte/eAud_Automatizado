import psycopg2
import geral_env as geral_db

# Conectar ao banco de dados de origem
def db_saver_interacao():
    conn1 = psycopg2.connect(
         f"host = {geral_db.server1}   dbname ={geral_db.database1}   user = {geral_db.login1}  password = {geral_db.password1}"
         )
    # Conectar ao banco de dados de destino
    conn2 = psycopg2.connect(f"host = {geral_db.server2}   dbname ={geral_db.database2}   user = {geral_db.login2}  password = {geral_db.password2}"
    )

    # Consulta SQL para extrair os dados de origem
    query = "SELECT tipointeracao, autor, unidadeautor, idtarefa, datamodificacao FROM interacoes_auxiliar"

    # Criar uma conexão para inserir os dados no destino
    cur = conn2.cursor()

    # Executar a consulta e inserir os dados no destino
    with conn1.cursor() as cursor:
        cursor.execute(query)
        for row in cursor:
            # Desempacotar a tupla row
            #id, tipointeracao, autor, unidadeautor, idtarefa, datamodificacao = row
            cur.execute("""
                        INSERT INTO interacoes (tipointeracao, autor, unidadeautor, idtarefa, datamodificacao) 
                VALUES (%s, %s, %s, %s, %s);
            """, row) #(tipointeracao, autor, unidadeautor, idtarefa, datamodificacao))
                      #ON CONFLICT (idtarefa, tipointeracao) DO UPDATE
                      #SET 
                      #    autor = EXCLUDED.autor, 
                      #    unidadeautor = EXCLUDED.unidadeautor,  
                      #    datamodificacao = EXCLUDED.datamodificacao            
    # Commitar a transação     
    conn2.commit()
    conn2.close()
    conn1.close()
db_saver_interacao()
