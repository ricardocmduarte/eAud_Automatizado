import psycopg2
import geral_env as geral_db

# Conectar ao banco de dados de origem
def db_saver_beneficios_id():
    conn1 = psycopg2.connect(
        f"host = {geral_db.server1}   dbname ={geral_db.database1}   user = {geral_db.login1}  password = {geral_db.password1}"
    )
    # Conectar ao banco de dados de destino
    conn2 = psycopg2.connect(f"host = {geral_db.server2}   dbname ={geral_db.database2}   user = {geral_db.login2}  password = {geral_db.password2}"
    )

    # Consulta SQL para extrair os dados de origem
    query = "SELECT id, atividade FROM beneficios_id_auxiliar"

    # Criar uma conexão para inserir os dados no destino
    cur = conn2.cursor()

    # Executar a consulta e inserir os dados no destino
    with conn1.cursor() as cursor:
        cursor.execute(query)
        for row in cursor:
            cur.execute("""
                        INSERT INTO beneficios_id (id, atividade) 
                VALUES (%s, %s) 
                ON CONFLICT (id) DO UPDATE 
                SET 
                    atividade = EXCLUDED.atividade                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            """, row)
                        

    # Commitar a transação     
    conn2.commit()
    conn2.close()
    conn1.close()
db_saver_beneficios_id()
