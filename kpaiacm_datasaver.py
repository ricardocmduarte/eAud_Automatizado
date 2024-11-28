import psycopg2
import geral_env as geral_db

def db_saver_kpaiacm():
    # Conectar ao banco de dados de origem
    conn1 = psycopg2.connect(
        f" host = {geral_db.server1} dbname = {geral_db.database1} user = {geral_db.login1} password = {geral_db.password1}"
    )
    # Conectar ao banco de dados de destino
    conn2 = psycopg2.connect(
        f" host = {geral_db.server2} dbname = {geral_db.database2} user = {geral_db.login2} password = {geral_db.password2}"
    )
    # Consulta SQL para extrair os dados de origem
    query = " SELECT id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade,descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, conclusaokpa, anexosgerais, objetivokpa, equipevalidacaoexternaiacm, atividaeskpa, equipeavaliacaoiacm, titulokpamodelo, datarealizadamodelokpa, datafimmodelokpa, assundomodelokpa, unidadesvalidadoras, produtokpa, resultadoskpa, praticakpa, links, uaigs, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade FROM kpa_iacm_auxiliar"
    # Criar uma conexão para inserir os dados no destino
    cur = conn2.cursor()
    # Executar a consulta e inserir os dados no destino
    with conn1.cursor() as cursor:
        cursor.execute(query)
        for row in cursor:
            cur.execute(""" 
                        INSERT INTO kpa_iacm (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, conclusaokpa, anexosgerais, objetivokpa, equipevalidacaoexternaiacm, atividaeskpa, equipeavaliacaoiacm, titulokpamodelo, datarealizadamodelokpa, datafimmodelokpa, assundomodelokpa, unidadesvalidadoras, produtokpa, resultadoskpa, praticakpa, links, uaigs, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
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
                    conclusaokpa = EXCLUDED.conclusaokpa,
                    anexosgerais = EXCLUDED.anexosgerais,
                    objetivokpa = EXCLUDED.objetivokpa,
                    equipevalidacaoexternaiacm = EXCLUDED.equipevalidacaoexternaiacm,
                    atividaeskpa = EXCLUDED.atividaeskpa,
                    equipeavaliacaoiacm = EXCLUDED.equipeavaliacaoiacm,
                    titulokpamodelo = EXCLUDED.titulokpamodelo,
                    datarealizadamodelokpa = EXCLUDED.datarealizadamodelokpa,
                    datafimmodelokpa = EXCLUDED.datafimmodelokpa,
                    assundomodelokpa = EXCLUDED.assundomodelokpa,
                    unidadesvalidadoras = EXCLUDED.unidadesvalidadoras,
                    produtokpa = EXCLUDED.produtokpa,
                    resultadoskpa = EXCLUDED.resultadoskpa,
                    praticakpa = EXCLUDED.praticakpa,
                    links = EXCLUDED.links,
                    uaigs = EXCLUDED.uaigs,
                    arquivocomportamentoespecifico = EXCLUDED.arquivocomportamentoespecifico,
                    estadosituacao = EXCLUDED.estadosituacao,
                    tags = EXCLUDED.tags,
                    pendencias = EXCLUDED.pendencias,
                    abasatividade = EXCLUDED.abasatividade,         
                    
            """, row)
    # Commitar a transação
    conn2.commit()
    conn2.close()
    conn1.close()
db_saver_kpaiacm()