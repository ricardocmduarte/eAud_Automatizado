import psycopg2
import geral_env as geral_db
import csv

def exportar_dados_para_csv(result):

    if result:
        # Nome do Arquivo csv
        arquivo = f"C://Users//M1503249//Documents//eAud_Arquivos//termo_compromisso_consultoria_auxiliar.csv"

        try:
            # Abrir o arquivo csv em modo de escrita
            with open(arquivo, 'w', newline='') as arquivo:

                #Criar um escritor csv
                escritor_csv = csv.writer(arquivo)

                #Escrever  os cabeçalhos das colunas 
                escritor_csv.writerow(['id', 'atividade'])

                #Escrever os dados
                for row in result:
                    escritor_csv.writerow(row)
            print(f"Dados exportados para {arquivo}")
        except Exception as e:
            print("Erro ao exportar dados para CSV:", e)


def termo_compromisso_consultoria_verificador_dados():
    # Conectar ao banco de dados de origem
    conn = psycopg2.connect(
        f" host = {geral_db.server3} dbname = {geral_db.database3} user = {geral_db.login3} password = {geral_db.password3}"
    )
    cursor = conn.cursor()

    # Verificar IDs na tabela tarefas_id vinculados à atividade 'CGE - Termo de Compromisso (Consultoria)' que não estão na tabela termo_compromisso_consultoria 
    cursor.execute(""" 
        SELECT a.id, a.atividade
        FROM tarefas_id a
        LEFT JOIN termo_compromisso_consultoria b
        ON a.id = b.id AND a.atividade = b.atividade
        WHERE a.atividade = 'CGE - Termo de Compromisso (Consultoria)' AND b.id IS NULL
    """)
    
    result = cursor.fetchall()
    
    if result:
        print("\nIDs na tabela tarefas_id vinculados com a atividade 'CGE - Termo de Compromisso (Consultoria)' que não estão na tabela termo_compromisso_consultoria: ")
        
        for row in result:
            print(row)
        exportar_dados_para_csv(result)
    else:
         print("Não existe IDs na tabela tarefas_id vinculados com a atividade 'CGE - Termo de Compromisso (Consultoria)' que não existam na tabela termo_compromisso_consultoria!")
    
    # Fechar conexão com o banco de dados
    conn.close()
    
termo_compromisso_consultoria_verificador_dados()
