import psycopg2
import geral_env as geral_db

def db_saver_itemprocessoanalisetce():
    # Conectar ao banco de dados de origem
    conn1 = psycopg2.connect(
        f" host = {geral_db.server1} dbname = {geral_db.database1} user = {geral_db.login1} password = {geral_db.password1}"
    )
    # Conectar ao banco de dados de destino
    conn2 = psycopg2.connect(
        f" host = {geral_db.server2} dbname = {geral_db.database2} user = {geral_db.login2} password = {geral_db.password2}"
    )
    # Consulta SQL para extrair os dados de origem
    query = " SELECT  id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, unidadeexecutora, fatosobapuracao, anexosgerais, processosassociados, tceorigem, produtouaig, numprocessotribunal, localidadesinteracao, numresolucaoportaria, dataencaminhado, fatoapuracao, links, datainstauracao, unidadesenvolvidas, valoratualizado, procedenciatce, destinatariousuariounidade, executores, valorprejuizoestimado, gerentesubprojeto, tipopessoa, cpf, cnpjs, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade FROM item_analise_tce_auxiliar"
    # Criar uma conexão para inserir os dados no destino
    cur = conn2.cursor()
    # Executar a consulta e inserir os dados no destino
    with conn1.cursor() as cursor:
        cursor.execute(query)
        for row in cursor:
            cur.execute(""" 
                        INSERT INTO item_analise_tce (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, unidadeexecutora, fatosobapuracao, anexosgerais, processosassociados, tceorigem, produtouaig, numprocessotribunal, localidadesinteracao, numresolucaoportaria, dataencaminhado, fatoapuracao, links, datainstauracao, unidadesenvolvidas, valoratualizado, procedenciatce, destinatariousuariounidade, executores, valorprejuizoestimado, gerentesubprojeto, tipopessoa, cpf, cnpjs, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
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
                    unidadeexecutora = EXCLUDED.unidadeexecutora,
                    fatosobapuracao = EXCLUDED.fatosobapuracao,
                    anexosgerais = EXCLUDED.anexosgerais,
                    processosassociados = EXCLUDED.processosassociados,
                    tceorigem = EXCLUDED.tceorigem,
                    produtouaig = EXCLUDED.produtouaig,
                    numprocessotribunal = EXCLUDED.numprocessotribunal,
                    localidadesinteracao = EXCLUDED.localidadesinteracao,
                    numresolucaoportaria = EXCLUDED.numresolucaoportaria,
                    dataencaminhado = EXCLUDED.dataencaminhado,
                    fatoapuracao = EXCLUDED.fatoapuracao,
                    links = EXCLUDED.links,
                    datainstauracao = EXCLUDED.datainstauracao,
                    unidadesenvolvidas = EXCLUDED.unidadesenvolvidas,
                    procedenciatce = EXCLUDED.procedenciatce,
                    destinatariousuariounidade = EXCLUDED.destinatariousuariounidade,
                    executores = EXCLUDED.executores,
                    valorprejuizoestimado = EXCLUDED.valorprejuizoestimado,
                    tags = EXCLUDED.tags,
                    gerentesubprojeto = EXCLUDED.gerentesubprojeto,
                    tipopessoa = EXCLUDED.tipopessoa,
                    cpf = EXCLUDED.cpf,
                    cnpjs = EXCLUDED.cnpjs,
                    valoratualizado = EXCLUDED.valoratualizado,
                    arquivocomportamentoespecifico = EXCLUDED.arquivocomportamentoespecifico,
                    estadosituacao = EXCLUDED.estadosituacao,
                    pendencias = EXCLUDED.pendencias,
                    abasatividade = EXCLUDED.abasatividade
            """,row)
    # Commitar a transação
    conn2.commit()
    conn2.close()
    conn1.close()
db_saver_itemprocessoanalisetce()