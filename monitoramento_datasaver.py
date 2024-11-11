import psycopg2
import geral_db_datasaver as geral_db

# Conectar ao banco de dados de origem
def db_saver_monitoramento():
    conn1 = psycopg2.connect(
         f"host = {geral_db.server1}   dbname ={geral_db.database1}   user = {geral_db.login1}  password = {geral_db.password1}"
         )
    # Conectar ao banco de dados de destino
    conn2 = psycopg2.connect(f"host = {geral_db.server2}   dbname ={geral_db.database2}   user = {geral_db.login2}  password = {geral_db.password2}"
    )

    # Consulta SQL para extrair os dados de origem
    query = "SELECT id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, detalhesmonitoramento, providencia, unidadesauditoria,  unidadesenvolvidas, categoriasmonitoramento, tarefasprecedentes, valorprejuizoestimado, observadores, unidadegestora, fundamentos, ultimoposicionamento, textoultimoposicionamento, textoultimamanifestacao, anexorelatorio, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade FROM monitoramento_teste"

    # Criar uma conexão para inserir os dados no destino
    cur = conn2.cursor()

    # Executar a consulta e inserir os dados no destino
    with conn1.cursor() as cursor:
        cursor.execute(query)
        for row in cursor:
            cur.execute("""
                        INSERT INTO monitoramento (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, detalhesmonitoramento, providencia, unidadesauditoria,  unidadesenvolvidas, categoriasmonitoramento, tarefasprecedentes, valorprejuizoestimado, observadores, unidadegestora, fundamentos, ultimoposicionamento, textoultimoposicionamento, textoultimamanifestacao, anexorelatorio, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
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
                    detalhesmonitoramento = EXCLUDED.detalhesmonitoramento, 
                    providencia = EXCLUDED.providencia, 
                    unidadesauditoria = EXCLUDED.unidadesauditoria,
                    unidadesenvolvidas = EXCLUDED.unidadesenvolvidas, 
                    categoriasmonitoramento = EXCLUDED.categoriasmonitoramento, 
                    tarefasprecedentes = EXCLUDED.tarefasprecedentes, 
                    valorprejuizoestimado = EXCLUDED.valorprejuizoestimado, 
                    observadores = EXCLUDED.observadores,
                    unidadegestora = EXCLUDED.unidadegestora, 
                    fundamentos = EXCLUDED.fundamentos, 
                    ultimoposicionamento = EXCLUDED.ultimoposicionamento, 
                    textoultimoposicionamento = EXCLUDED.textoultimoposicionamento, 
                    textoultimamanifestacao = EXCLUDED.textoultimamanifestacao,
                    anexorelatorio = EXCLUDED.anexorelatorio, 
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
db_saver_monitoramento()
