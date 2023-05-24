import db
import requests
import geral
from log import get_log
import json
from join_function import join_data


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

                id = tarefa['id']
                situacao = tarefa['situacao']
                estado = tarefa['estado']
                atividade = tarefa['atividade']
                titulo = tarefa['titulo']
                idtarefaassociada = tarefa['campos']['tarefaAssociada'][
                    'valor']['id'] if tarefa['campos']['tarefaAssociada']['valor'] else ''
                titulotarefaassociada = tarefa['tituloTarefaAssociada']
                dtprevisaoinicio = tarefa['dtPrevisaoInicio']
                dtprevisaofim = tarefa['dtPrevisaoFim']
                dtrealizadainicio = tarefa['dtRealizadaInicio']
                dtrealizadafim = tarefa['dtRealizadaFim']
                prioridade = tarefa['prioridade']
                assunto = tarefa['assunto']
                idatividade = tarefa['idAtividade']
                descricaoatividade = tarefa['descricaoAtividade']
                idsituacao = tarefa['idSituacao']
                dataultimamodificacao = tarefa['dataUltimaModificacao']
                autorultimamodificacao = tarefa['autorUltimaModificacao']

                objetosauditoria = tarefa['campos']['objetosAuditoriaAuditoria']['valor']
                processosassociados = tarefa['campos']['processosAssociados']['valor']
                dadosgerenciais = tarefa['campos']['dadosGerenciaisAuditoria']['valor']

                gerentesauditoria = tarefa['campos']['gerentesAuditoria']['valor']
                gerenteauditoria = []
                if gerentesauditoria:
                    for i, ger in enumerate(gerentesauditoria):
                        gerenteauditoria.append(ger['nomeExibicao'])

                    gerenteauditoria = join_data(gerenteauditoria)

                rrelpreli = tarefa['campos']['relPreliminarAud']['valor']
                relatoriopreliminar = []
                if rrelpreli:
                    relatoriopreliminar = rrelpreli['nome']

                proponenteauditoria = tarefa['campos']['proponenteAuditoria']['valor']
                duracaomeses = tarefa['campos']['duracaoMesesAuditoria']['valor']
                recursofinanceiro = tarefa['campos']['recursoFinanceiroAuditoria']['valor']

                conhecimentostecnicos = tarefa['campos']['conhecimentosTecnicosRequeridosAuditoria']['valor']
                conhecimentostec = []
                if conhecimentostecnicos:
                    for i, conhecimento in enumerate(conhecimentostecnicos):
                        conhecimentostec.append(conhecimento['nomeExibicao'])

                    conhecimentostec = join_data(conhecimentostec)

                localidadeauditoria = tarefa['campos']['localidadesAuditoria']['valor']
                locaisauditoria = []
                if localidadeauditoria:
                    for i, local in enumerate(localidadeauditoria):
                        locaisauditoria.append(local['nomeExibicao'])

                    locaisauditoria = join_data(locaisauditoria)

                responsavelauditoria = tarefa['campos']['responsavelAuditoria']['valor']
                anexrel = tarefa['campos']['AnexRelpre']['valor']
                anexorelpreliminar = []
                if anexrel:
                    for i, file in enumerate(anexrel):
                        anexorelpreliminar.append(file['nome'])

                    anexorelpreliminar = join_data(anexorelpreliminar)

                objestrategico = tarefa['campos']['resultadosEsperadosAuditoria']['valor']
                objetivoestrategico = []
                resultadosindicador = []
                resultadosdescricao = []
                if objestrategico:
                    for i, obj in enumerate(objestrategico):
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

                origemdemanda = tarefa['campos']['origemDemandaAuditoria']['valor']
                origem = origemdemanda['nomeExibicao']

                pessoajuridica = tarefa['campos']['pessoaJuridicaExaminadaAuditoria']['valor']

                supervisores = tarefa['campos']['supervisoresAuditoria']['valor']
                supervisor = []
                if supervisores:
                    for i, super in enumerate(supervisores):
                        supervisor.append(super['nomeExibicao'])

                    supervisor = join_data(supervisor)

                tipoconsultoria = tarefa['campos']['tipoConsultoria']['valor']
                tipo = []
                if tipoconsultoria:
                    for i, tip in enumerate(tipoconsultoria):
                        tipo.append(tip['valor'])

                    tipo = join_data(tipo)

                numdenuncia = tarefa['campos']['numDenuncia']['valor']

                coordenadorequipe = tarefa['campos']['coordenadorEquipeAuditoria']['valor']
                coordenador = []
                if coordenadorequipe:
                    for i, coordequipe in enumerate(coordenadorequipe):
                        coordenador.append(coordequipe['nomeExibicao'])

                    coordenador = join_data(coordenador)

                unidadesauditadas = tarefa['campos']['unidadesAuditadasAuditoria']['valor']
                nomeunidadesauditadas = []
                if unidadesauditadas:
                    for i, unidades in enumerate(unidadesauditadas):
                        nomeunidadesauditadas.append(unidades['nome'])

                    nomeunidadesauditadas = join_data(nomeunidadesauditadas)

                homemhoras = tarefa['campos']['homemHorasAuditoria']['valor']

                equipeauditoria = tarefa['campos']['equipeAuditoria']['valor']
                equipe = []
                if equipeauditoria:
                    for i, geralequipe in enumerate(equipeauditoria):
                        equipe.append(geralequipe['nomeExibicao'])

                    equipe = join_data(equipe)

                aanexrel = tarefa['campos']['anexRel']['valor']
                anexorel = []
                if aanexrel:
                    for i, file in enumerate(aanexrel):
                        anexorel.append(file['nome'])

                    anexorel = join_data(anexorel)

                areasrequeridas = tarefa['campos']['areasRequeridasAuditoria']['valor']
                arearequerida = []
                if areasrequeridas:
                    for i, area in enumerate(areasrequeridas):
                        arearequerida.append(area['nomeExibicao'])

                    arearequerida = join_data(arearequerida)

                objetivoauditoria = tarefa['campos']['objetivoAuditoria']['valor']

                tarefasprecedentes = tarefa['campos']['tarefasPrecedentes']['valor']

                envolvidosauditoria = tarefa['campos']['envolvidosAuditoria']['valor']
                envolauditoria = []
                if envolvidosauditoria:
                    for i, envolvido in enumerate(envolvidosauditoria):
                        envolauditoria.append(envolvido['nomeExibicao'])

                    envolauditoria = join_data(envolauditoria)

                processotrabalhoauditoria = tarefa['campos']['processoTrabalhoAuditoria']['valor']

                anexosauditoria = tarefa['campos']['anexosAuditoria']['valor']
                anexoauditoria = []
                if anexosauditoria:
                    for i, anex in enumerate(anexosauditoria):
                        anexoauditoria.append(anex['nome'])

                    anexoauditoria = join_data(anexoauditoria)

                acaolinha = tarefa['campos']['linhaAcaoAuditoria']['valor']
                linhaacao = []
                if acaolinha:
                    linhaacao = acaolinha['valor']
                else:
                    linhaacao = ''

                relfinal = tarefa['campos']['relFinalAud']['valor']
                relatorifinal = []
                if relfinal:
                    relatorifinal = relfinal['nome']

                estadosituacao = tarefa['estadoSituacao']
                arquivocomportamento = tarefa['arquivoComportamentoEspecifico']

                descricaotag = tarefa['campos']['tags']['valor']
                tags = []
                if descricaotag:
                    for i, tagdesc in enumerate(descricaotag):
                        tags.append(tagdesc['descricao'])

                    tags = join_data(tags)

                pendencias = tarefa['pendencias']
                listapendencia = []
                if pendencias:
                    for i, pendencia in enumerate(pendencias):
                        listapendencia.append(pendencia['nomeUsuarioUnidade'])

                    listapendencia = join_data(listapendencia)

                abasatividade = tarefa['abasAtividade']
                listaabaatividades = []
                if abasatividade:
                    for i, abas in enumerate(abasatividade):
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
            insert_query = (f"""INSERT INTO auditorias (id, situacao, estado, atividade, titulo, titulotarefaassociada,
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
