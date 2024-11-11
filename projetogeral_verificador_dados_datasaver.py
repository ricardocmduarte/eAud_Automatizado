import psycopg2
import geral_db_verificador_dados_datasaver as geral_db
import csv

def exportar_dados_para_csv(result):

    if result:

        # Nome do Arquivo csv
        arquivo = f"C://Users//M1503249//Documents//eAud_Arquivos//projeto_geral_teste.csv"

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


def projeto_geral_verificador_dados():
    # Conexão com o banco de dados
    conn = psycopg2.connect(
         f"host = {geral_db.server}   dbname ={geral_db.database}   user = {geral_db.login}  password = {geral_db.password}"
    )
    cur = conn.cursor()

    # Verificar IDs na tabela tarefas_id vinculados à atividade 'CGE - Projeto Geral' que não estão na tabela projeto_geral
    cur.execute(""" 
        SELECT a.id, a.atividade
        FROM tarefas_id a
        LEFT JOIN projeto_geral b
        ON a.id = b.id AND a.atividade = b.atividade
        WHERE a.atividade = 'CGE - Projeto Geral' AND b.id IS NULL
    """)

    result = cur.fetchall()

    if result:
        print("\nIDs na tabela tarefas_id vinculados com a atividade 'CGE - Projeto Geral' que não existem na tabela projeto_geral: ")
        
        for row in result:
            print(row)
        exportar_dados_para_csv(result)
    else:
        print("Não existem IDs na tabela tarefas_id vinculados com a atividade 'CGE - Projeto Geral' que não existam na tabela projeto_geral!")


    # Fechar conexão com o banco de dados
    conn.close()
projeto_geral_verificador_dados()