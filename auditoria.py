import db
import requests
import geral_env as geral
from log import get_log
import json
from join_function import join_data
from datetime import datetime

tipo_arquivo = 'get_auditoria'

def get_auditoria(ids):
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
                lista_dados.append(get_auditoria_requisicao(id))
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
                dataultimamodificacao = datetime.strptime(tarefa['dataUltimaModificacao'],'%d/%m/%Y %H:%M:%S') if tarefa['dataUltimaModificacao'] else None               
                autorultimamodificacao = tarefa['autorUltimaModificacao']
                
                # SOLUÇÃO: Usar get() para evitar KeyError quando campos não existirem
                # Extração de campos específicos da auditoria
                objetosauditoria = tarefa['campos'].get('objetosAuditoriaAuditoria', {}).get('valor')
                processosassociados = tarefa['campos'].get('processosAssociados', {}).get('valor')
                dadosgerenciais = tarefa['campos'].get('dadosGerenciaisAuditoria', {}).get('valor')
                gerentesauditoria = tarefa['campos'].get('gerentesAuditoria', {}).get('valor')
                gerenteauditoria = []
                if gerentesauditoria:
                    for ger in gerentesauditoria:
                        gerenteauditoria.append(ger['nomeExibicao'])
                    gerenteauditoria = join_data(gerenteauditoria)

                rrelpreli = tarefa['campos'].get('relPreliminarAud', {}).get('valor')
                relatoriopreliminar = []
                if rrelpreli:
                    relatoriopreliminar = rrelpreli['nome']

                proponenteauditoria = tarefa['campos'].get('proponenteAuditoria', {}).get('valor')
                duracaomeses = tarefa['campos'].get('duracaoMesesAuditoria', {}).get('valor')
                recursofinanceiro = tarefa['campos'].get('recursoFinanceiroAuditoria', {}).get('valor')
                conhecimentostecnicos = tarefa['campos'].get('conhecimentosTecnicosRequeridosAuditoria', {}).get('valor')
                conhecimentostec = []
                if conhecimentostecnicos:
                    for conhecimento in conhecimentostecnicos:
                        conhecimentostec.append(conhecimento['nomeExibicao'])
                    conhecimentostec = join_data(conhecimentostec)

                localidadeauditoria = tarefa['campos'].get('localidadesAuditoria', {}).get('valor')
                locaisauditoria = []
                if localidadeauditoria:
                    for local in localidadeauditoria:
                        locaisauditoria.append(local['nomeExibicao'])
                    locaisauditoria = join_data(locaisauditoria)

                # SOLUÇÃO APLICADA: Usar get() para evitar KeyError no campo responsavelAuditoria
                responsavelauditoria = tarefa['campos'].get('responsavelAuditoria', {}).get('valor')
                
                anexrel = tarefa['campos'].get('AnexRelpre', {}).get('valor')
                anexorelpreliminar = []
                if anexrel:
                    for file in anexrel:
                        anexorelpreliminar.append(file['nome'])
                    anexorelpreliminar = join_data(anexorelpreliminar)

                objestrategico = tarefa['campos'].get('resultadosEsperadosAuditoria', {}).get('valor')
                objetivoestrategico = []
                resultadosindicador = []
                resultadosdescricao = []
                if objestrategico:
                    for obj in objestrategico:
                        objetivoestrategico.append(
                            obj['objetivoEstrategico']['nome'])
                        if obj['indicador'] is None:
                            pass
                        else:
                            resultadosindicador.append(
                                obj['indicador']['nome'])
                            resultadosdescricao.append(
                                obj['indicador']['descricao'])
                    objetivoestrategico = join_data(objetivoestrategico)
                    resultadosindicador = join_data(resultadosindicador)
                    resultadosdescricao = join_data(resultadosdescricao)

                origemdemanda = tarefa['campos'].get('origemDemandaAuditoria', {}).get('valor')
                origem = origemdemanda['nomeExibicao'] if origemdemanda else None
                
                pessoajuridica = tarefa['campos'].get('pessoaJuridicaExaminadaAuditoria', {}).get('valor')
                supervisores = tarefa['campos'].get('supervisoresAuditoria', {}).get('valor')
                supervisor = []
                if supervisores:
                    for super in supervisores:
                        supervisor.append(super['nomeExibicao'])
                    supervisor = join_data(supervisor)

                tipoconsultoria = tarefa['campos'].get('tipoConsultoria', {}).get('valor')
                tipo = []
                if tipoconsultoria:
                    for tip in tipoconsultoria:
                        tipo.append(tip['valor'])
                    tipo = join_data(tipo)

                numdenuncia = tarefa['campos'].get('numDenuncia', {}).get('valor')
                coordenadorequipe = tarefa['campos'].get('coordenadorEquipeAuditoria', {}).get('valor')
                coordenador = []
                if coordenadorequipe:
                    for coordequipe in coordenadorequipe:
                        coordenador.append(coordequipe['nomeExibicao'])
                    coordenador = join_data(coordenador)

                unidadesauditadas = tarefa['campos'].get('unidadesAuditadasAuditoria', {}).get('valor')
                nomeunidadesauditadas = []
                if unidadesauditadas:
                    for unidades in unidadesauditadas:
                        nomeunidadesauditadas.append(unidades['nome'])
                    nomeunidadesauditadas = join_data(nomeunidadesauditadas)

                homemhoras = tarefa['campos'].get('homemHorasAuditoria', {}).get('valor')
                equipeauditoria = tarefa['campos'].get('equipeAuditoria', {}).get('valor')
                equipe = []
                if equipeauditoria:
                    for geralequipe in equipeauditoria:
                        equipe.append(geralequipe['nomeExibicao'])
                    equipe = join_data(equipe)

                aanexrel = tarefa['campos'].get('anexRel', {}).get('valor')
                anexorel = []
                if aanexrel:
                    for file in aanexrel:
                        anexorel.append(file['nome'])
                    anexorel = join_data(anexorel)

                areasrequeridas = tarefa['campos'].get('areasRequeridasAuditoria', {}).get('valor')
                arearequerida = []
                if areasrequeridas:
                    for area in areasrequeridas:
                        arearequerida.append(area['nomeExibicao'])
                    arearequerida = join_data(arearequerida)

                objetivoauditoria = tarefa['campos'].get('objetivoAuditoria', {}).get('valor')
                tarefasprecedentes = tarefa['campos'].get('tarefasPrecedentes', {}).get('valor')
                envolvidosauditoria = tarefa['campos'].get('envolvidosAuditoria', {}).get('valor')
                envolauditoria = []
                if envolvidosauditoria:
                    for envolvido in envolvidosauditoria:
                        envolauditoria.append(envolvido['nomeExibicao'])
                    envolauditoria = join_data(envolauditoria)

                processotrabalhoauditoria = tarefa['campos'].get('processoTrabalhoAuditoria', {}).get('valor')
                anexosauditoria = tarefa['campos'].get('anexosAuditoria', {}).get('valor')
                anexoauditoria = []
                if anexosauditoria:
                    for anex in anexosauditoria:
                        anexoauditoria.append(anex['nome'])
                    anexoauditoria = join_data(anexoauditoria)

                acaolinha = tarefa['campos'].get('linhaAcaoAuditoria', {}).get('valor')
                linhaacao = acaolinha['valor'] if acaolinha else ''

                relfinal = tarefa['campos'].get('relFinalAud', {}).get('valor')
                relatorifinal = relfinal['nome'] if relfinal else []

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
                    'objetosauditoria': objetosauditoria,
                    'processosassociados': processosassociados,
                    'dadosgerenciais': dadosgerenciais,
                    'gerentesauditoria': gerenteauditoria,
                    'relatoriopreliminar': relatoriopreliminar,
                    'proponenteauditoria': proponenteauditoria,
                    'duracaomeses': duracaomeses,
                    'recursofinanceiro': recursofinanceiro,
                    'conhecimentostecnicos': conhecimentostec,
                    'localidadesauditoria': locaisauditoria,
                    'responsavelauditoria': responsavelauditoria,
                    'anexorelatoriopreliminar': anexorelpreliminar,
                    'objetivosestrategicos': objetivoestrategico,
                    'resultadosindicador': resultadosindicador,
                    'resultadosdescricao': resultadosdescricao,
                    'origemdemanda': origem,
                    'pessoajuridica': pessoajuridica,
                    'tipoconsultoria': tipo,
                    'numdenuncia': numdenuncia,
                    'unidadesauditadas': nomeunidadesauditadas,
                    'homemhoras': homemhoras,
                    'equipeauditoria': equipe,
                    'anexorel': anexorel,
                    'areasrequeridas': arearequerida,
                    'objetivoauditoria': objetivoauditoria,
                    'tarefasprecedentes': tarefasprecedentes,
                    'envolvidosauditoria': envolauditoria,
                    'processotrabalhoauditoria': processotrabalhoauditoria,
                    'anexosauditoria': linhaacao,
                    'linhaacaoauditoria': anexoauditoria,
                    'relatoriofinal': relatorifinal,
                    'coordenadorequipe': coordenador,
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
                 tarefa['objetosauditoria'],
                 tarefa['processosassociados'],
                 tarefa['dadosgerenciais'],
                 tarefa['gerentesauditoria'],
                 tarefa['relatoriopreliminar'],
                 tarefa['proponenteauditoria'],
                 tarefa['duracaomeses'],
                 tarefa['recursofinanceiro'],
                 tarefa['conhecimentostecnicos'],
                 tarefa['localidadesauditoria'],
                 tarefa['responsavelauditoria'],
                 tarefa['anexorelatoriopreliminar'],
                 tarefa['objetivosestrategicos'],
                 tarefa['resultadosindicador'],
                 tarefa['resultadosdescricao'],
                 tarefa['origemdemanda'],
                 tarefa['pessoajuridica'],
                 tarefa['tipoconsultoria'],
                 tarefa['numdenuncia'],
                 tarefa['unidadesauditadas'],
                 tarefa['homemhoras'],
                 tarefa['equipeauditoria'],
                 tarefa['anexorel'],
                 tarefa['areasrequeridas'],
                 tarefa['objetivoauditoria'],
                 tarefa['tarefasprecedentes'],
                 tarefa['envolvidosauditoria'],
                 tarefa['processotrabalhoauditoria'],
                 tarefa['linhaacaoauditoria'],
                 tarefa['anexosauditoria'],
                 tarefa['relatoriofinal'],
                 tarefa['coordenadorequipe'],
                 tarefa['supervisores'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO auditorias_auxiliar (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,objetosauditoria,processosassociados,dadosgerenciais,
                                                gerentesauditoria,relatoriopreliminar,proponenteauditoria,duracaomeses,recursofinanceiro,conhecimentostecnicos,localidadesauditoria,
                                                responsavelauditoria,anexorelatoriopreliminar, objetivosestrategicos,resultadosindicador,resultadosdescricao,
                                                origemdemanda,pessoajuridica,tipoconsultoria,numdenuncia,unidadesauditadas,homemhoras,
                                                equipeauditoria,anexorel,areasrequeridas,objetivoauditoria,tarefasprecedentes,envolvidosauditoria,processotrabalhoauditoria,
                                                anexosauditoria,linhaacaoauditoria,relatoriofinal,coordenadorequipe,supervisores,
                                                estadosituacao, arquivocomportamentoespecifico,tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)

def get_auditoria_requisicao(id):
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