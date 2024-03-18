import db
import requests
import geral
from log import get_log
import json
from join_function import join_data
from datetime import datetime

tipo_arquivo = 'get_relatorio_preliminar'


def get_relatorio_preliminar(ids):
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
                lista_dados.append(get_relatorio_preliminar_requisicao(id))

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

                prelrelatorio = tarefa['campos']['relatorioPreliminar']['valor']
                relatoriopreliminar = []
                if prelrelatorio:
                    relatoriopreliminar = prelrelatorio['nome']

                hipotese = tarefa['campos']['hipoteseLegal']['valor']
                hipoteselegal = []
                if hipotese:
                    for i, hip in enumerate(hipotese):
                        hipoteselegal.append(hip['nomeExibicao'])

                    hipoteselegal = join_data(hipoteselegal)

                relatoriofinal = tarefa['campos']['relatorioFinal']['valor']

                coordequipe = tarefa['campos']['CoordenadorEquipe']['valor']
                coordenadorequipe = []
                if coordequipe:
                    for i, coord in enumerate(coordequipe):
                        coordenadorequipe.append(coord['nomeExibicao'])

                    coordenadorequipe = join_data(coordenadorequipe)

                supervisor = tarefa['campos']['supervisores']['valor']
                supervisores = []
                if supervisor:
                    for i, super in enumerate(supervisor):
                        supervisores.append(super['nomeExibicao'])

                    supervisores = join_data(supervisores)

                parecer = tarefa['campos']['parecer']['valor']
                pareceres = []
                if parecer:
                    for i, file in enumerate(parecer):
                        pareceres.append(file['nome'])

                    pareceres = join_data(pareceres)

                wordrel = tarefa['campos']['relatorioWord']['valor']
                relatorioword = []
                if wordrel:
                    relatorioword = wordrel['nome']

                unidenvolvidas = tarefa['campos']['unidEnvolvidas']['valor']
                unidadesenvolvidas = []
                if unidenvolvidas:
                    for i, envolvidos in enumerate(unidenvolvidas):
                        unidadesenvolvidas.append(envolvidos['nomeExibicao'])

                    unidadesenvolvidas = join_data(unidadesenvolvidas)

                relcom = tarefa['campos']['RelatorioCom']['valor']
                relatoriocom = []
                if relcom:
                    for i, file in enumerate(relcom):
                        relatoriocom.append(file['nome'])

                    relatoriocom = join_data(relatoriocom)

                obser = tarefa['campos']['observadores']['valor']
                observadores = []
                if obser:
                    for i, obs in enumerate(obser):
                        observadores.append(obs['nomeExibicao'])

                    observadores = join_data(observadores)

                certificado = tarefa['campos']['certificado']['valor']
                certificados = []
                if certificado:
                    for i, file in enumerate(certificado):
                        certificados.append(file['nome'])

                    certificados = join_data(certificados)

                tag = tarefa['campos']['tags']['valor']
                tags = []
                if tag:
                    for i, tagtag in enumerate(tag):
                        tags.append(tagtag['descricao'])

                    tags = join_data(tags)

                anexrelpre = tarefa['campos']['AnexRelpre']['valor']
                anexorelatoriopreliminar = []
                if anexrelpre:
                    for i, file in enumerate(anexrelpre):
                        anexorelatoriopreliminar.append(file['nome'])

                    anexorelatoriopreliminar = join_data(
                        anexorelatoriopreliminar)

                equipe = tarefa['campos']['EquipeGeral']['valor']
                equipegeral = []
                if equipe:
                    for i, team in enumerate(equipe):
                        equipegeral.append(team['nomeExibicao'])

                    equipegeral = join_data(equipegeral)

                arquivocomportamento = tarefa['arquivoComportamentoEspecifico']
                estadosituacao = tarefa['estadoSituacao']

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
                    'relatoriopreliminar': relatoriopreliminar,
                    'hipoteselegal': hipoteselegal,
                    'relatoriofinal': relatoriofinal,
                    'coordenadorequipe': coordenadorequipe,
                    'supervisores': supervisores,
                    'parecer': pareceres,
                    'anexorelatorio': anexorelatoriopreliminar,
                    'relatorioword': relatorioword,
                    'unidadesenvolvidas': unidadesenvolvidas,
                    'relatoriocom': relatoriocom,
                    'observadores': observadores,
                    'certificados': certificados,
                    'equipegeral': equipegeral,
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
                 tarefa['relatoriopreliminar'],
                 tarefa['hipoteselegal'],
                 tarefa['relatoriofinal'],
                 tarefa['coordenadorequipe'],
                 tarefa['supervisores'],
                 tarefa['parecer'],
                 tarefa['anexorelatorio'],
                 tarefa['relatorioword'],
                 tarefa['unidadesenvolvidas'],
                 tarefa['relatoriocom'],
                 tarefa['observadores'],
                 tarefa['certificados'],
                 tarefa['equipegeral'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO relatorio_preliminar_teste (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,relatoriofinal,relatoriopreliminar,hipoteselegal,coordenadorequipe,supervisores,
                                                parecer,anexorelatorio,relatorioword,unidadesenvolvidas,relatoriocom,observadores,certificados,
                                                equipegeral,arquivocomportamentoespecifico, estadosituacao,
                                                tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_relatorio_preliminar_requisicao(id):
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
