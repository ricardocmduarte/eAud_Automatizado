import psycopg2
import geral_db_verificador_dados_datasaver as geral_db
import csv

def exportar_dados_para_csv(result, result1):

    if result:

        # Nome do Arquivo csv
        arquivo = f"C://Users//M1503249//Documents//eAud_Arquivos//item_analise_tce_teste.csv"

        try:
            # Abrir o arquivo csv em modo de escrita
            with open(arquivo, 'w', newline='') as arquivo:

                # Criar um escritor csv
                escritor_csv = csv.writer(arquivo)

                # Escrever  os cabeçalhos das colunas
                escritor_csv.writerow(['id', 'atividade'])

                # Escrever os dados
                for row in result:
                    escritor_csv.writerow(row)
            print(f"Dados exportados para {arquivo}")
        except Exception as e:
            print("Erro ao exportar dados para CSV: ", e)
    
    if result1:

        # Nome do Arquivo csv
        arquivo1 = f"C://Users//M1503249//Documents//eAud_Arquivos//item_analise_tce_test.csv"
    
        try:
            # Abrir o arquivo csv em modo de escrita
            with open(arquivo1, 'w', newline='') as arquivo1:
                # Criar um escritor csv
                escritor_csv1 = csv.writer(arquivo1)
                # Escrever  os cabeçalhos das colunas
                escritor_csv1.writerow(['id', 'atividade'])
                # Escrever os dados
                for row1 in result1:
                    escritor_csv1.writerow(row1)
            print(f"Dados exportados para {arquivo1}")
        except Exception as e1:
            print("Erro ao exportar dados para CSV: ", e1)

def itemprocesso_analise_tce_verificador_dados():
    # Conexão com o banco de dados
    conn = psycopg2.connect(
        f" host = {geral_db.server} dbname = {geral_db.database} user = {geral_db.login} password = {geral_db.password}"
    )
    cur = conn.cursor()

    # Verificar IDs na tabela tarefas_id vinculados à atividade 'CGEMG - Item de Processo (Análise de TCE)' que não estão na tabela item_analise_tce
    cur.execute(""" 
        SELECT a.id, a.atividade
        FROM tarefas_id a 
        LEFT JOIN item_analise_tce b
        ON a.id = b.id AND a.atividade = b.atividade
        WHERE a.atividade =  'CGEMG - Item de Processo (Análise de TCE)' AND b.id IS NULL
    """)

    result = cur.fetchall()

    if result: 
        print("\nIDs na tabela tarefas_id vinculados com a atividade 'CGEMG - Item de Processo (Análise de TCE)' que não existem na tabela item_analise_tce: ")
        
        for row in result:
            print(row)
        exportar_dados_para_csv(result)
    else:
        print("Não existem IDs na tabela tarefas_id vinculados com a atividade 'CGEMG - Item de Processo (Análise de TCE)' que não existam na tabela item_analise_tce!")

    # Verificar IDs na tabela tarefas_id vinculados à atividade 'CGE - Item de Processo (Análise de TCE)' que não estão na tabela item_analise_tce
    cur.execute(""" 
    SELECT a.id, a.atividade
    FROM tarefas_id a 
    LEFT JOIN item_analise_tce b
    ON a.id = b.id AND a.atividade = b.atividade
    WHERE a.atividade =  'CGE - Item de Processo (Análise de TCE)' AND b.id IS NULL
    """)
    result1 = cur.fetchall()

    if result1: 
        print("\nIDs na tabela tarefas_id vinculados com a atividade 'CGE - Item de Processo (Análise de TCE)' que não existem na tabela item_analise_tce: ")

        for row1 in result1:
            print(row1)
        exportar_dados_para_csv(result1)
    else:
        print("Não existem IDs na tabela tarefas_id vinculados com a atividade 'CGE - Item de Processo (Análise de TCE)' que não existam na tabela item_analise_tce!")
    
    # Fechar conexão com o banco de dados
    conn.close()

itemprocesso_analise_tce_verificador_dados()