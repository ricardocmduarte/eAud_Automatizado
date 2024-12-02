import psycopg2
import geral_env as geral_db

def db_saver_analisepreliminar():

    # Conectar ao banco de dados da origem
    conn1 = psycopg2.connect(
        f" host = {geral_db.server1} dbname = {geral_db.database1} user = {geral_db.login1} password = {geral_db.password1}"
    )
    
    print("Conexão com o banco de dados de origem estabelecida.")
    
    # Conectar ao banco de dados do destino
    conn2 = psycopg2.connect(
        f" host = {geral_db.server2} dbname = {geral_db.database2} user = {geral_db.login2} password = {geral_db.password2}"
    )
    
    print("Conexão com o banco de dados de destino estabelecida.")
    
    # Consulta SQL para extrair os dados da origem
    query = " SELECT id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, unidadesenvolvidas, universosauditaveis, anexosgerais, objetosauditoria, matrizcontrole, tarefasprecedentes, observadores, hipoteselegal, coordenadorequipe, equipegeral, supervisores, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade FROM analise_preliminar_auxiliar"
    # Criar uma conexão para inserir os dados no destino
    cur = conn2.cursor()

    # Executar a consulta e inserir os dados no destino
    with conn1.cursor() as cursor:
        print("Executando consulta para extrair dados da tabela de origem.")
        cursor.execute(query)
        for row in cursor:
            print(f"Inserindo/Atualizando dados: {row}")
            cur.execute ("""
                         INSERT INTO analise_preliminar (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, unidadesenvolvidas, universosauditaveis, anexosgerais, objetosauditoria, matrizcontrole, tarefasprecedentes, observadores, hipoteselegal, coordenadorequipe, equipegeral, supervisores, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
                ON CONFLICT (id) DO UPDATE
                SET
                    situacao = EXCLUDED.situacao,
                    estado = EXCLUDED.estado,
                    atividade = EXCLUDED.atividade,
                    titulo = EXCLUDED.titulo,
                    idtarefaassociada = EXCLUDED.idtarefaassociada,
                    titulotarefaassociada = EXCLUDED.titulotarefaassociada,
                    dtprevisaoinicio = EXCLUDED.dtprevisaoinicio,
                    dtprevisaofim = EXCLUDED.dtprevisaofim,
                    dtrealizadainicio = EXCLUDED.dtrealizadainicio,
                    dtrealizadafim = EXCLUDED.dtrealizadafim,
                    prioridade = EXCLUDED.prioridade,
                    assunto = EXCLUDED.assunto,
                    idatividade = EXCLUDED.idatividade,
                    descricaoatividade = EXCLUDED.descricaoatividade,
                    idsituacao = EXCLUDED.idsituacao,
                    dataultimamodificacao = EXCLUDED.dataultimamodificacao,
                    autorultimamodificacao = EXCLUDED.autorultimamodificacao,
                    unidadesenvolvidas = EXCLUDED.unidadesenvolvidas,
                    universosauditaveis = EXCLUDED.universosauditaveis,
                    anexosgerais = EXCLUDED.anexosgerais,
                    objetosauditoria = EXCLUDED.objetosauditoria,
                    matrizcontrole = EXCLUDED.matrizcontrole,
                    tarefasprecedentes = EXCLUDED.tarefasprecedentes,
                    observadores = EXCLUDED.observadores,
                    hipoteselegal = EXCLUDED.hipoteselegal,
                    coordenadorequipe = EXCLUDED.coordenadorequipe,
                    equipegeral = EXCLUDED.equipegeral,
                    supervisores = EXCLUDED.supervisores,
                    arquivocomportamentoespecifico = EXCLUDED.arquivocomportamentoespecifico,
                    estadosituacao = EXCLUDED.estadosituacao,
                    tags = EXCLUDED.tags,
                    pendencias = EXCLUDED.pendencias,
                    abasatividade = EXCLUDED.abasatividade
                         
            """, row)

    # Comitar e fechar a transação
    conn2.commit()
    conn2.close()
    conn1.close()
    print(f"Inserção/Atualização de dados no banco de dados {geral_db.database2} na tabela analise_preliminar finalizada com sucesso!")
    print("------------------------------------------------------------------------------------------------------------------------------------")

db_saver_analisepreliminar()
