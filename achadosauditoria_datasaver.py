import psycopg2
import geral_env as geral_db


def db_saver_achadosauditoria():
    # Conectar ao banco de dados da origem
    conn1 = psycopg2.connect(
        f"host = {geral_db.server1} dbname = {geral_db.database1} user = {geral_db.login1} password = {geral_db.password1} "
    )

    # Conectar ao banco de dados do destino 
    conn2 = psycopg2.connect(
        f"host = {geral_db.server2} dbname = {geral_db.database2} user = {geral_db.login2} password = {geral_db.password2}"
    )

    # Consulta SQL para extrair os dados da origem
    query = "SELECT id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtRealizadaFim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, unidadesenvolvidas, itensachadosauditoria, anexosgerais, relatoriocom, tarefaprecedentes, observadores, hipoteselegal, coordenadorequipe, equipegeral, supervisores, anexosrelatorio, mesconclusaorealizado, mesanoultimamodificacao, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade FROM achados_auditoria_auxiliar"

    # Criar uma conexão para inserir os dados no destino
    cur = conn2.cursor()

    # Executar a consulta e inserir os dados no destino
    with conn1.cursor() as cursor:
        cursor.execute(query)
        for row in cursor:
            cur.execute(""" 
                        INSERT INTO achados_auditoria (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtRealizadaFim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, unidadesenvolvidas, itensachadosauditoria, anexosgerais, relatoriocom, tarefaprecedentes, observadores, hipoteselegal, coordenadorequipe, equipegeral, supervisores, anexosrelatorio, mesconclusaorealizado, mesanoultimamodificacao, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ) 
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
                    dtRealizadaFim = EXCLUDED.dtRealizadaFim, 
                    prioridade = EXCLUDED.prioridade, 
                    assunto = EXCLUDED.assunto,
                    idatividade = EXCLUDED.idatividade, 
                    descricaoatividade = EXCLUDED.descricaoatividade, 
                    idsituacao = EXCLUDED.idsituacao, 
                    dataultimamodificacao = EXCLUDED.dataultimamodificacao, 
                    autorultimamodificacao = EXCLUDED.autorultimamodificacao, 
                    unidadesenvolvidas = EXCLUDED.unidadesenvolvidas, 
                    itensachadosauditoria = EXCLUDED.itensachadosauditoria,
                    anexosgerais = EXCLUDED.anexosgerais, 
                    relatoriocom = EXCLUDED.relatoriocom, 
                    tarefaprecedentes = EXCLUDED.tarefaprecedentes, 
                    observadores = EXCLUDED.observadores, 
                    hipoteselegal = EXCLUDED.hipoteselegal, 
                    coordenadorequipe = EXCLUDED.coordenadorequipe, 
                    equipegeral = EXCLUDED.equipegeral, 
                    supervisores = EXCLUDED.supervisores, 
                    anexosrelatorio = EXCLUDED.anexosrelatorio,
                    mesconclusaorealizado = EXCLUDED.mesconclusaorealizado, 
                    mesanoultimamodificacao = EXCLUDED.mesanoultimamodificacao, 
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

db_saver_achadosauditoria()

