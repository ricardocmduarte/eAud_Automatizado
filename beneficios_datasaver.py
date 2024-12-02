import psycopg2
import geral_env as geral_db

# Conectar ao banco de dados de origem
def db_saver_beneficios():
    conn1 = psycopg2.connect(
         f"host = {geral_db.server1}   dbname ={geral_db.database1}   user = {geral_db.login1}  password = {geral_db.password1}"
    )
    
    print("Conexão com o banco de dados de origem estabelecida.")
    
    # Conectar ao banco de dados de destino
    conn2 = psycopg2.connect(f"host = {geral_db.server2}   dbname ={geral_db.database2}   user = {geral_db.login2}  password = {geral_db.password2}"
    )
    
    print("Conexão com o banco de dados de destino estabelecida.") 
     
    # Consulta SQL para extrair os dados de origem
    query = "SELECT id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, beneficioavulso, descricaobeneficio, valorbruto, descricaocusto, dimensaorepercussao, valorcusto, unidadesenvolvidas, unidadegestora, anexosbeneficio, providenciabeneficio, dimenssaobeneficio, parcelasbeneficio, titulofundamento, textofundamentobeneficio, valorliquido, classebeneficio, tipobeneficio, tarefasprecedentes, unidadeproponente, anofatogeradorbeneficio, situacaoanateriorbeneficio, anoimplementacaobeneficio, repercussaobeneficio, classebf, nivelbeneficio, classebnf, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade FROM beneficios_auxiliar"

    # Criar uma conexão para inserir os dados no destino
    cur = conn2.cursor()

    # Executar a consulta e inserir os dados no destino
    with conn1.cursor() as cursor:
        print("Executando consulta para extrair dados da tabela de origem.")
        cursor.execute(query)
        for row in cursor:
            print(f"Inserindo/Atualizando dados: {row}")
            cur.execute("""
                        INSERT INTO beneficios (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada, dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, idsituacao, dataultimamodificacao, autorultimamodificacao, beneficioavulso, descricaobeneficio, valorbruto, descricaocusto, dimensaorepercussao, valorcusto, unidadesenvolvidas, unidadegestora, anexosbeneficio, providenciabeneficio, dimenssaobeneficio, parcelasbeneficio, titulofundamento, textofundamentobeneficio, valorliquido, classebeneficio, tipobeneficio, tarefasprecedentes, unidadeproponente, anofatogeradorbeneficio, situacaoanateriorbeneficio, anoimplementacaobeneficio, repercussaobeneficio, classebf, nivelbeneficio, classebnf, arquivocomportamentoespecifico, estadosituacao, tags, pendencias, abasatividade) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
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
                    beneficioavulso = EXCLUDED.beneficioavulso, 
                    descricaobeneficio = EXCLUDED.descricaobeneficio, 
                    valorbruto = EXCLUDED.valorbruto, 
                    descricaocusto = EXCLUDED.descricaocusto, 
                    dimensaorepercussao = EXCLUDED.dimensaorepercussao, 
                    valorcusto = EXCLUDED.valorcusto, 
                    unidadesenvolvidas = EXCLUDED.unidadesenvolvidas, 
                    unidadegestora = EXCLUDED.unidadegestora, 
                    anexosbeneficio = EXCLUDED.anexosbeneficio, 
                    providenciabeneficio = EXCLUDED.providenciabeneficio, 
                    dimenssaobeneficio = EXCLUDED.dimenssaobeneficio, 
                    parcelasbeneficio = EXCLUDED.parcelasbeneficio, 
                    titulofundamento = EXCLUDED.titulofundamento, 
                    textofundamentobeneficio = EXCLUDED.textofundamentobeneficio, 
                    valorliquido = EXCLUDED.valorliquido, 
                    classebeneficio = EXCLUDED.classebeneficio, 
                    tipobeneficio = EXCLUDED.tipobeneficio, 
                    tarefasprecedentes = EXCLUDED.tarefasprecedentes, 
                    unidadeproponente = EXCLUDED.unidadeproponente, 
                    anofatogeradorbeneficio = EXCLUDED.anofatogeradorbeneficio, 
                    situacaoanateriorbeneficio = EXCLUDED.situacaoanateriorbeneficio, 
                    anoimplementacaobeneficio = EXCLUDED.anoimplementacaobeneficio, 
                    repercussaobeneficio = EXCLUDED.repercussaobeneficio, 
                    classebf = EXCLUDED.classebf, 
                    nivelbeneficio = EXCLUDED.nivelbeneficio, 
                    classebnf = EXCLUDED.classebnf, 
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
    print(f"Inserção/Atualização de dados no banco de dados {geral_db.database2} na tabela beneficios finalizada com sucesso!")
    print("--------------------------------------------------------------------------------------------------------------------------")
    
db_saver_beneficios()
