import db
import requests
import geral_env as geral
from log import get_log
import json
from join_function import join_data
from datetime import datetime

tipo_arquivo = 'get_comunicacao_auditoria'

def get_comunicacao_auditoria(ids):
    response = geral.check_url_health('tarefa')
    get_log(f"Iniciado {tipo_arquivo}")

    if response != 200:
        get_log(
            f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP:  {str(response)}".upper())
        return print(f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP:  {str(response)}")

    try:
        lista_dados = []
        lista_final = []
        if ids:
            for i, id in enumerate(ids):
                lista_dados.append(get_comunicacao_requisicao(id))
                print(
                    f"Iteração {tipo_arquivo} {str(i)} registrada com sucesso")

        get_log(
            f"Esta requisicao {tipo_arquivo} contém {len(lista_dados)} itens")

        # lista final passa por um tratamento de dados
        if lista_dados:
            lista_final = tratamento_dados(lista_dados)

        # comando para salvar os dados tratados
        if lista_final:
            salvar_dados(lista_final)
        get_log(f"Lista de {tipo_arquivo} ok")
        return print(f"Lista de {tipo_arquivo} ok")
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)

def tratamento_dados(data):
    try:
        lista_final = []
        for i, tarefa in enumerate(data):
            if tarefa:
                # Extração de campos básicos da tarefa
                id = tarefa['id']
                situacao = tarefa['situacao']
                estado = tarefa['estado']
                atividade = tarefa['atividade']
                titulo = tarefa['titulo']
                idtarefaassociada = tarefa['idTarefaAssociada'] if tarefa['idTarefaAssociada'] else 0
                titulotarefaassociada = tarefa['tituloTarefaAssociada']
                dtprevisaoinicio = datetime.strptime(tarefa['dtPrevisaoInicio'], '%d/%m/%Y') if tarefa['dtPrevisaoInicio'] else None
                dtprevisaofim = datetime.strptime(tarefa['dtPrevisaoFim'], '%d/%m/%Y') if tarefa['dtPrevisaoFim'] else None
                dtrealizadainicio = datetime.strptime(tarefa['dtRealizadaInicio'], '%d/%m/%Y') if tarefa['dtRealizadaInicio'] else None
                dtrealizadafim = datetime.strptime(tarefa['dtRealizadaFim'], '%d/%m/%Y') if tarefa['dtRealizadaFim'] else None                                                
                prioridade = tarefa['prioridade']
                assunto = tarefa['assunto']
                idatividade = tarefa['idAtividade']
                descricaoatividade = tarefa['descricaoAtividade']
                idsituacao = tarefa['idSituacao']
                dataultimamodificacao = datetime.strptime(tarefa['dataUltimaModificacao'], '%d/%m/%Y %H:%M:%S') if tarefa['dataUltimaModificacao'] else None                                
                autorultimamodificacao = tarefa['autorUltimaModificacao']

                # SOLUÇÃO: Usar get() para evitar KeyError quando campos não existirem
                # Extração de campos específicos da comunicação de auditoria
                indminutadestinatario = tarefa['campos'].get('indMinutaDestinatario', {}).get('valor')
                detalhamento = tarefa['campos'].get('Detalhamento', {}).get('valor')

                anexosgerais = tarefa['campos'].get('anexosGerais', {}).get('valor')
                anexgerais = []
                if anexosgerais:
                    for anex in anexosgerais:
                        anexgerais.append(anex['nome'])
                    anexgerais = join_data(anexgerais)

                coordenadorequipe = tarefa['campos'].get('CoordenadorEquipe', {}).get('valor')
                coordenador = []
                if coordenadorequipe:
                    for coordequipe in coordenadorequipe:
                        coordenador.append(coordequipe['nomeExibicao'])
                    coordenador = join_data(coordenador)

                destinatarios = tarefa['campos'].get('destinatarios', {}).get('valor')
                destinatario = []
                if destinatarios:
                    for dest in destinatarios:
                        destinatario.append(dest['nomeExibicao'])
                    destinatario = join_data(destinatario)

                copycom = tarefa['campos'].get('copiaComunicacao', {}).get('valor')
                copiacomunicacao = []
                if copycom:
                    for file in copycom:
                        copiacomunicacao.append(file['nomeExibicao'])
                    copiacomunicacao = join_data(copiacomunicacao)

                supervisores = tarefa['campos'].get('EquipeGeral', {}).get('valor')
                supervisor = []
                if supervisores:
                    for super in supervisores:
                        supervisor.append(super['nomeExibicao'])
                    supervisor = join_data(supervisor)

                unidadesenvolvidas = tarefa['campos'].get('unidEnvolvidas', {}).get('valor')
                unidadesenvol = []
                if unidadesenvolvidas:
                    for unidade in unidadesenvolvidas:
                        unidadesenvol.append(unidade['nomeExibicao'])
                    unidadesenvol = join_data(unidadesenvol)

                # SOLUÇÃO: Usar get() e verificar se o valor existe antes de converter data
                prazo_valor = tarefa['campos'].get('Prazo', {}).get('valor')
                prazo = datetime.strptime(prazo_valor, '%d/%m/%Y %H:%M:%S') if prazo_valor else None
                
                tarefasprecedentes = tarefa['campos'].get('tarefasPrecedentes', {}).get('valor')
                
                dataenviocomunicacao_valor = tarefa['campos'].get('dataEnvioComunicacao', {}).get('valor')
                dataenviocomunicacao = datetime.strptime(dataenviocomunicacao_valor, '%d/%m/%Y') if dataenviocomunicacao_valor else None
                
                dataciencia_valor = tarefa['campos'].get('dataCiencia', {}).get('valor')
                dataciencia = datetime.strptime(dataciencia_valor, '%d/%m/%Y') if dataciencia_valor else None

                equipegeral = tarefa['campos'].get('EquipeGeral', {}).get('valor')
                equipe = []
                if equipegeral:
                    for geralequipe in equipegeral:
                        equipe.append(geralequipe['nomeExibicao'])
                    equipe = join_data(equipe)

                indminutaremente = tarefa['campos'].get('indMinutaRemetente', {}).get('valor')
                estadosituacao = tarefa['estadoSituacao']
                arquivocomportamento = tarefa['arquivoComportamentoEspecifico']

                descricaotag = tarefa['campos'].get('tags', {}).get('valor')
                tags = []
                if descricaotag:
                    for tagdesc in descricaotag:
                        tags.append(tagdesc['descricao'])
                    tags = join_data(tags)

                pendencias = tarefa['pendencias']
                listapendencia = []
                if pendencias:
                    for pendencia in pendencias:
                        listapendencia.append(pendencia['nomeUsuarioUnidade'])
                    listapendencia = join_data(listapendencia)

                abasatividade = tarefa['abasAtividade']
                listaabaatividades = []
                if abasatividade:
                    for abas in abasatividade:
                        listaabaatividades.append(abas['descricao'])
                    listaabaatividades = join_data(listaabaatividades)

                lista_final.append({
                    'id': id,
                    'situacao': situacao,
                    'estado': estado,
                    'atividade': atividade,
                    'titulo': titulo,
                    'idtarefaassociada': idtarefaassociada,
                    'titulotarefaassociada': titulotarefaassociada,
                    'dtprevisaoinicio': dtprevisaoinicio,
                    'dtprevisaofim': dtprevisaofim,
                    'dtrealizadainicio': dtrealizadainicio,
                    'dtrealizadafim': dtrealizadafim,
                    'prioridade': prioridade,
                    'assunto': assunto,
                    'idatividade': idatividade,
                    'descricaoatividade': descricaoatividade,
                    'idsituacao': idsituacao,
                    'dataultimamodificacao': dataultimamodificacao,
                    'autorultimamodificacao': autorultimamodificacao,
                    'indminutadestinatario': indminutadestinatario,
                    'detalhamento': detalhamento,
                    'anexosgerais': anexgerais,
                    'destinatarios': destinatario,
                    'copiacomunicacao': copiacomunicacao,
                    'prazo': prazo,
                    'dataenviocomunicacao': dataenviocomunicacao,
                    'dataciencia': dataciencia,
                    'indminutaremetente': indminutaremente,
                    'tarefasprecedentes': tarefasprecedentes,
                    'unidadesenvolvidas': unidadesenvol,
                    'coordenadorequipe': coordenador,
                    'equipegeral': equipe,
                    'supervisores': supervisor,
                    'arquivocomportamentoespecifico': arquivocomportamento,
                    'estadosituacao': estadosituacao,
                    'tags': tags,
                    'pendencias': listapendencia,
                    'abasatividade': listaabaatividades,
                })

        get_log(f"Lista {tipo_arquivo} tratada com sucesso")
        return lista_final
    except NameError as err:
        get_log(f"Erro ao tratar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao tratar os dados {tipo_arquivo}", err)

def salvar_dados(resultado_array):
    try:
        banco = db.db_connection()
        cur = banco.cursor()

        resultado_array = db.current_datetime_query(resultado_array)

        for tarefa in resultado_array:
            lista = [
                (tarefa['id'],
                 tarefa['situacao'],
                 tarefa['estado'],
                 tarefa['atividade'],
                 tarefa['titulo'],
                 tarefa['idtarefaassociada'],
                 tarefa['titulotarefaassociada'],
                 tarefa['dtprevisaoinicio'],
                 tarefa['dtprevisaofim'],
                 tarefa['dtrealizadainicio'],
                 tarefa['dtrealizadafim'],
                 tarefa['prioridade'],
                 tarefa['assunto'],
                 tarefa['idatividade'],
                 tarefa['descricaoatividade'],
                 tarefa['idsituacao'],
                 tarefa['dataultimamodificacao'],
                 tarefa['autorultimamodificacao'],
                 tarefa['indminutadestinatario'],
                 tarefa['detalhamento'],
                 tarefa['anexosgerais'],
                 tarefa['destinatarios'],
                 tarefa['copiacomunicacao'],
                 tarefa['prazo'],
                 tarefa['dataenviocomunicacao'],
                 tarefa['dataciencia'],
                 tarefa['indminutaremetente'],
                 tarefa['tarefasprecedentes'],
                 tarefa['unidadesenvolvidas'],
                 tarefa['coordenadorequipe'],
                 tarefa['equipegeral'],
                 tarefa['supervisores'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO comunicacao_auditoria_auxiliar (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,indminutadestinatario,detalhamento,anexosgerais,
                                                destinatarios,copiacomunicacao,prazo,dataenviocomunicacao,dataciencia,indminutaremetente,
                                                tarefasprecedentes,unidadesenvolvidas,coordenadorequipe,equipegeral,supervisores,
                                                estadosituacao, arquivocomportamentoespecifico,tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)

def get_comunicacao_requisicao(id):
    try:
        url = geral.url + \
            f"tarefa/{id}/dto/json"
        resp = requests.get(url, headers=geral.header)

        if resp.status_code != 200:
            get_log(
                f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP: {str(resp.status_code)}".upper())
            print(
                f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP: {str(resp.status_code)}")
            return None

        if resp.text == '[]':
            get_log(f"Requisição {tipo_arquivo} não contém dados".upper())
            return print(f"Requisição {tipo_arquivo} não contém dados")

        response_text = json.loads(resp.text)

        return response_text

    except requests.exceptions.HTTPError as errh:
        get_log(errh)
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        get_log(errc)
        print(errc)
    except requests.exceptions.Timeout as errt:
        get_log(errt)
        print(errt)
    except requests.exceptions.RequestException as err:
        get_log(err)
        print(err)