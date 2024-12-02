import psycopg2
import geral_env as geral_db

def db_saver_escopoauditoria():
    # Conectar ao banco de dados de origem
    conn1 = psycopg2.connect(
        f" host = {geral_db.server1} dbname = {geral_db.database1} user = {geral_db.login1} password = {geral_db.password1}"
    )
    
    print("Conexao com o banco de dados de origem estabelecida.")
    
    # Conectar ao banco de dados de destino
    conn2 = psycopg2.connect(
        f" host = {geral_db.server2} dbname = {geral_db.database2} user = {geral_db.login2} password = {geral_db.password2}"
    )
    
    print("Conexao com o banco de dados de destino estabelecida.")
    
    # Consulta SQL para extrair os dados de origem
    query = "SELECT id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, escopodescricao, escopovalortotal, escopovalorauditado, macroprocessoescopo, observadores, hiposetelegal, tarefasprecedentes, unidadesenvolvidas, coordenadorequipe, equipegeral, supervisores, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade FROM escopo_auditoria_auxiliar"
    # Criar uma conexão para inserir os dados no destino
    cur = conn2.cursor()
    # Executar a consulta e inserir os dados no destino
    with conn1.cursor() as cursor:
        print("Executando consulta para extrair dados da tabela de origem.")
        cursor.execute(query)
        for row in cursor:
            print(f"Inserindo/Atualizando dados: {row}")
            cur.execute(""" INSERT INTO escopo_auditoria (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, escopodescricao, escopovalortotal, escopovalorauditado, macroprocessoescopo, observadores, hiposetelegal, tarefasprecedentes, unidadesenvolvidas, coordenadorequipe, equipegeral, supervisores, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade) 
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
                    escopodescricao = EXCLUDED.escopodescricao,
                    escopovalortotal = EXCLUDED.escopovalortotal,
                    escopovalorauditado = EXCLUDED.escopovalorauditado,
                    macroprocessoescopo = EXCLUDED.macroprocessoescopo,
                    observadores = EXCLUDED.observadores,
                    hiposetelegal = EXCLUDED.hiposetelegal,
                    tarefasprecedentes = EXCLUDED.tarefasprecedentes,
                    unidadesenvolvidas = EXCLUDED.unidadesenvolvidas,
                    coordenadorequipe = EXCLUDED.coordenadorequipe,
                    equipegeral = EXCLUDED.equipegeral,
                    supervisores = EXCLUDED.supervisores,
                    arquivocomportamentoespecifico = EXCLUDED.arquivocomportamentoespecifico,
                    estadosituacao = EXCLUDED.estadosituacao,
                    tags = EXCLUDED.tags,
                    pendencias = EXCLUDED.pendencias,
                    abasatividade = EXCLUDED.abasatividade
            """, row)
    # Commitar a transação
    conn2.commit()
    conn2.close()
    conn1.close()
    print(f"Inserção/Atualização de dados no banco de dados {geral_db.database2} na tabelas escopo_auditoria finalizada com sucesso!")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    
db_saver_escopoauditoria()