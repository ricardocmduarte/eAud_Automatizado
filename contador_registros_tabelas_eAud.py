import psycopg2
import geral_env as geral_db
import csv
import os
from datetime import datetime, timedelta

def get_contador_linhas_tabelas(connection):
    # Consulta para obter todas as tabelas do esquema público do banco de dados
    query_tables = """ 
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'public' AND table_type = 'BASE TABLE';
    """

    table_counts = []

    with connection.cursor() as cursor:
        cursor.execute(query_tables)
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]
            # Consulta para contar o número de registros em cada tabela
            query_count = f"SELECT COUNT(*) FROM {table_name};"
            cursor.execute(query_count)
            count = cursor.fetchone()[0]
            table_counts.append((table_name, count))
    
    return table_counts

def escrever_contador_para_csv(table_counts, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome_Tabela", "Numero_Registros"])
        writer.writerows(table_counts)

def principal():
    # Conectar ao banco de dados PostgreSQL
    connection = psycopg2.connect(f"dbname={geral_db.database3} user={geral_db.login3} password={geral_db.password3} host={geral_db.server3}")
    data_atual = datetime.now()
    #data_incremantada = data_atual + timedelta(days=1)
    dia = data_atual.strftime("%d") #data_incremantada.strftime("%d")
    mes = data_atual.strftime("%m") #data_incremantada.strftime("%m")
    ano = data_atual.strftime("%Y") #data_incremantada.strftime("%Y")
    print (f'{dia}/{mes}/{ano}')
    try:
        table_counts = get_contador_linhas_tabelas(connection)
        
        escrever_contador_para_csv(table_counts, f'C:\\Users\\M1503249\\Documents\\E-aud\\table_counts_{dia}-{mes}-{ano}.csv')
        print(f"Arquivo table_counts_{dia}-{mes}-{ano}.csv criado com sucesso na data {dia}/{mes}/{ano}.")
        
        escrever_contador_para_csv(table_counts, f'C:\\Users\\M1503249\\OneDrive - CAMG\\Documentos\\E-aud\\table_counts_{dia}-{mes}-{ano}.csv')
        print(f"Arquivo table_counts_{dia}-{mes}-{ano}.csv criado com sucesso na data {dia}/{mes}/{ano}.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        connection.close()

principal()

