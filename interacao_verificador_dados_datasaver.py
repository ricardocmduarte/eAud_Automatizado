import psycopg2
import geral_env as geral_db
import csv

def exportar_dados_para_csv(result):

    if result:
         
        # Nome do Arquivo csv
        arquivo = f"C://Users//M1503249//Documents//eAud_Arquivos//interacoes_auxiliar.csv"

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

def interacao_verificador_dados():
    # Conexão com o banco de dados
    conn = psycopg2.connect(
        f" host = {geral_db.server3} dbname = {geral_db.database3} user = {geral_db.login3} password = {geral_db.password3}"
    )
    cur = conn.cursor()

    # Verificar IDs na tabela tarefas_id que não estão na tabela interacoes
    cur.execute("""
        SELECT a.id, a.atividade
        FROM tarefas_id a
        LEFT JOIN interacoes b
        ON a.id = b.idtarefa
        WHERE b.idtarefa IS NULL
    """)
    result = cur.fetchall()

    if result:

        print("\nIDs na tabela tarefas_id que não existem na tabela interacoes")

        for row in result:
            print(row)
        exportar_dados_para_csv(result)
    else:
        print("Não existem IDs na tabela tarefas_id que não existam na tabela interacoes!")

    # Fechar conexão com o banco de dados
    conn.close()
interacao_verificador_dados()
