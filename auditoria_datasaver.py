import psycopg2
import geral_env as geral_db

# Conectar ao banco de dados de origem
def db_saver_auditoria():
    conn1 = psycopg2.connect(
        f"host = {geral_db.server1}   dbname ={geral_db.database1}   user = {geral_db.login1}  password = {geral_db.password1}"
    )
    
    print("Conexão com o banco de dados de origem estabelecida.")
    
    # Conectar ao banco de dados de destino
    conn2 = psycopg2.connect(
        f"host = {geral_db.server2}   dbname ={geral_db.database2}   user = {geral_db.login2}  password = {geral_db.password2}"
    )
    
    print("Conexão com o banco de dados de destino estabelecida.")

    # Consulta SQL para extrair os dados de origem
    query = "SELECT id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, objetosauditoria, processosassociados, dadosgerenciais, gerentesauditoria, relatoriopreliminar, proponenteauditoria, duracaomeses, recursofinanceiro, conhecimentostecnicos, localidadesauditoria, responsavelauditoria, anexorelatoriopreliminar, objetivosestrategicos, resultadosindicador, resultadosdescricao, origemdemanda, pessoajuridica, tipoconsultoria, numdenuncia, unidadesauditadas, homemhoras, equipeauditoria, anexorel, areasrequeridas, objetivoauditoria, tarefasprecedentes, envolvidosauditoria, processotrabalhoauditoria, anexosauditoria, linhaacaoauditoria, relatoriofinal, coordenadorequipe, supervisores, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade FROM auditorias_auxiliar"

    # Criar uma conexão para inserir os dados no destino
    cur = conn2.cursor()

    # Executar a consulta e inserir os dados no destino
    with conn1.cursor() as cursor:
        print("Executando consulta para extrair dados da tabela de origem.")
        cursor.execute(query)
        for row in cursor:
            print(f"Inserindo/Atualizando dados: {row}")
            cur.execute("""
                        INSERT INTO auditorias (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, objetosauditoria, processosassociados, dadosgerenciais, gerentesauditoria, relatoriopreliminar, proponenteauditoria, duracaomeses, recursofinanceiro, conhecimentostecnicos, localidadesauditoria, responsavelauditoria, anexorelatoriopreliminar, objetivosestrategicos, resultadosindicador, resultadosdescricao, origemdemanda, pessoajuridica, tipoconsultoria, numdenuncia, unidadesauditadas, homemhoras, equipeauditoria, anexorel, areasrequeridas, objetivoauditoria, tarefasprecedentes, envolvidosauditoria, processotrabalhoauditoria, anexosauditoria, linhaacaoauditoria, relatoriofinal, coordenadorequipe, supervisores, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
                ON CONFLICT (id) DO UPDATE 
                SET 
                    situacao = EXCLUDED.situacao, 
                    estado = EXCLUDED.estado, 
                    atividade = EXCLUDED.atividade, 
                    titulo = EXCLUDED.titulo, 
                    idtarefaassociada = EXCLUDED.idtarefaassociada, 
                    titulotarefaassociada = EXCLUDED.titulotarefaassociada, 
                    dtprevisaoinicio = EXCLUDED.dtprevisaoinicio,  
                    dtprevisaofim  = EXCLUDED.dtprevisaofim, 
                    dtrealizadainicio = EXCLUDED.dtrealizadainicio, 
                    dtrealizadafim = EXCLUDED.dtrealizadafim, 
                    prioridade = EXCLUDED.prioridade, 
                    assunto = EXCLUDED.assunto, 
                    idatividade = EXCLUDED.idatividade, 
                    descricaoatividade = EXCLUDED.descricaoatividade, 
                    idsituacao = EXCLUDED.idsituacao, 
                    dataultimamodificacao = EXCLUDED.dataultimamodificacao, 
                    autorultimamodificacao = EXCLUDED.autorultimamodificacao, 
                    objetosauditoria = EXCLUDED.objetosauditoria, 
                    processosassociados = EXCLUDED.processosassociados, 
                    dadosgerenciais = EXCLUDED.dadosgerenciais, 
                    gerentesauditoria = EXCLUDED.gerentesauditoria, 
                    relatoriopreliminar = EXCLUDED.relatoriopreliminar, 
                    proponenteauditoria = EXCLUDED.proponenteauditoria, 
                    duracaomeses = EXCLUDED.duracaomeses, 
                    recursofinanceiro = EXCLUDED.recursofinanceiro, 
                    conhecimentostecnicos = EXCLUDED.conhecimentostecnicos, 
                    localidadesauditoria = EXCLUDED.localidadesauditoria, 
                    responsavelauditoria = EXCLUDED.responsavelauditoria, 
                    anexorelatoriopreliminar = EXCLUDED.anexorelatoriopreliminar, 
                    objetivosestrategicos = EXCLUDED.objetivosestrategicos, 
                    resultadosindicador = EXCLUDED.resultadosindicador, 
                    resultadosdescricao = EXCLUDED.resultadosdescricao, 
                    origemdemanda = EXCLUDED.origemdemanda, 
                    pessoajuridica = EXCLUDED.pessoajuridica, 
                    tipoconsultoria = EXCLUDED.tipoconsultoria, 
                    numdenuncia = EXCLUDED.numdenuncia, 
                    unidadesauditadas = EXCLUDED.unidadesauditadas, 
                    homemhoras = EXCLUDED.homemhoras, 
                    equipeauditoria = EXCLUDED.equipeauditoria, 
                    anexorel = EXCLUDED.anexorel, 
                    areasrequeridas = EXCLUDED.areasrequeridas, 
                    objetivoauditoria = EXCLUDED.objetivoauditoria, 
                    tarefasprecedentes = EXCLUDED.tarefasprecedentes, 
                    envolvidosauditoria = EXCLUDED.envolvidosauditoria, 
                    processotrabalhoauditoria = EXCLUDED.processotrabalhoauditoria, 
                    anexosauditoria = EXCLUDED.anexosauditoria, 
                    linhaacaoauditoria = EXCLUDED.linhaacaoauditoria, 
                    relatoriofinal = EXCLUDED.relatoriofinal, 
                    coordenadorequipe = EXCLUDED.coordenadorequipe, 
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
    print(f"Inserção/Atualização de dados no banco de dados {geral_db.database2} na tabela auditora finalizada com sucesso!")
    print("--------------------------------------------------------------------------------------------------------------------------")
    
db_saver_auditoria()
