import db
import requests
import geral
from log import get_log
import json
from join_function import join_data

tipo_arquivo = 'get_achados'


def get_achados(ids):
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
                lista_dados.append(get_achados_requisicao(id))

                print(f"Iteração {str(i)} {tipo_arquivo}")

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

                unidadeenvolvida = tarefa['campos']['unidEnvolvidas']['valor']
                unidadesenvolvidas = []
                if unidadeenvolvida:
                    for i, uni in enumerate(unidadeenvolvida):
                        unidadesenvolvidas.append(
                            uni['nomeExibicao'] + ' | ' + uni['localidade']['nomeExibicao'])

                    unidadesenvolvidas = join_data(unidadesenvolvidas)

                else:
                    unidadesenvolvidas = ''

                itemachado = tarefa['campos']['itensAchadoAuditoria']['valor']
                itensachadosauditoria = []
                if itemachado:
                    for i, item in enumerate(itemachado):
                        itensachadosauditoria.append(item['descricaoSumaria'])

                    itensachadosauditoria = join_data(itensachadosauditoria)
                else:
                    itensachadosauditoria = ''

                anexgerais = tarefa['campos']['anexosGerais']['valor']
                anexosgerais = []
                if anexgerais:
                    for i, file in enumerate(anexgerais):
                        anexosgerais.append(file['nome'])

                    anexosgerais = join_data(anexosgerais)
                else:
                    anexosgerais = ''

                relcom = tarefa['campos']['RelatorioCom']['valor']
                relatoriocom = relcom['nome'] if relcom else ''

                prectarefas = tarefa['campos']['tarefasPrecedentes']['valor']
                tarefaprecedentes = prectarefas if prectarefas else ''

                observador = tarefa['campos']['observadores']['valor']
                observadores = []
                if observador:
                    for i, obs in enumerate(observador):
                        observadores.append(obs['nomeExibicao'])

                    observadores = join_data(observadores)
                else:
                    observadores = ''

                hiplegal = tarefa['campos']['hipoteseLegal']['valor']
                hipoteselegal = []
                if hiplegal:
                    for i, hip in enumerate(hiplegal):
                        hipoteselegal.append(hip['nomeExibicao'])

                    hipoteselegal = join_data(hipoteselegal)
                else:
                    hipoteselegal = ''

                coordequipe = tarefa['campos']['CoordenadorEquipe']['valor']
                coordenadorequipe = []
                if coordequipe:
                    for i, coord in enumerate(coordequipe):
                        coordenadorequipe.append(coord['nomeExibicao'])

                    coordenadorequipe = join_data(coordenadorequipe)
                else:
                    coordenadorequipe = ''

                equipgeral = tarefa['campos']['EquipeGeral']['valor']
                equipegeral = []
                if equipgeral:
                    for i, equipe in enumerate(equipgeral):
                        equipegeral.append(equipe['nomeExibicao'])

                    equipegeral = join_data(equipegeral)
                else:
                    equipegeral = ''

                supervisor = tarefa['campos']['supervisores']['valor']
                supervisores = []
                if supervisor:
                    for i, super in enumerate(supervisor):
                        supervisores.append(super['nomeExibicao'])

                    supervisores = join_data(supervisores)
                else:
                    supervisores = ''

                anexrelatorio = tarefa['campos']['anexosRelatorio']['valor']
                anexosrelatorios = []
                if anexrelatorio:
                    for i, file in enumerate(anexrelatorio):
                        anexosrelatorios.append(file['nome'])

                    anexosrelatorios = join_data(anexosrelatorios)
                else:
                    anexosrelatorios = ''

                mesconclusaorealizado = tarefa['mesConclusaoRealizado']
                mesanoultimamodificacao = tarefa['mesAnoUltimaModificacao']

                estadosituacao = tarefa['estadoSituacao']

                filecomport = tarefa['arquivoComportamentoEspecifico']
                arquivocomportamento = filecomport if filecomport else ''

                descricaotag = tarefa['campos']['tags']['valor']
                tags = []
                if descricaotag:
                    for i, tagdesc in enumerate(descricaotag):
                        tags.append(tagdesc['descricao'])

                    tags = join_data(tags)
                else:
                    tags = ''

                pendencias = tarefa['pendencias']
                listapendencia = []
                if pendencias:
                    for i, pendencia in enumerate(pendencias):
                        listapendencia.append(pendencia['nomeUsuarioUnidade'])

                    listapendencia = join_data(listapendencia)
                else:
                    listapendencia = ''

                abasatividade = tarefa['abasAtividade']
                listaabaatividades = []
                if abasatividade:
                    for i, abas in enumerate(abasatividade):
                        listaabaatividades.append(abas['descricao'])

                    listaabaatividades = join_data(listaabaatividades)
                else:
                    listaabaatividades = ''

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
                    'unidadesenvolvidas': unidadesenvolvidas,
                    'itensachadosauditoria': itensachadosauditoria,
                    'anexosgerais': anexosgerais,
                    'relatoriocom': relatoriocom,
                    'tarefaprecedentes': tarefaprecedentes,
                    'observadores': observadores,
                    'hipoteselegal': hipoteselegal,
                    'coordenadorequipe': coordenadorequipe,
                    'equipegeral': equipegeral,
                    'supervisores': supervisores,
                    'anexosrelatorio': anexosrelatorios,
                    'mesconclusaorealizado': mesconclusaorealizado,
                    'mesanoultimamodificacao': mesanoultimamodificacao,
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
                 tarefa['unidadesenvolvidas'],
                 tarefa['itensachadosauditoria'],
                 tarefa['anexosgerais'],
                 tarefa['relatoriocom'],
                 tarefa['tarefaprecedentes'],
                 tarefa['observadores'],
                 tarefa['hipoteselegal'],
                 tarefa['coordenadorequipe'],
                 tarefa['equipegeral'],
                 tarefa['supervisores'],
                 tarefa['anexosrelatorio'],
                 tarefa['mesconclusaorealizado'],
                 tarefa['mesanoultimamodificacao'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO achados_auditoria (id, situacao, estado, atividade, titulo,idtarefaassociada,
                                                titulotarefaassociada,dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtRealizadaFim,
                                                prioridade,assunto,idatividade,descricaoatividade,idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,unidadesenvolvidas,itensachadosauditoria,anexosgerais,
                                                relatoriocom,tarefaprecedentes,observadores,hipoteselegal,coordenadorequipe,equipegeral, supervisores,
                                                anexosrelatorio,mesconclusaorealizado,mesanoultimamodificacao,arquivocomportamentoespecifico,estadosituacao,
                                                tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_achados_requisicao(id):
    try:
        url = geral.url + \
            f"tarefa/{id}/dto/json"
        resp = requests.get(url, headers=geral.header)

        if resp.status_code != 200:
            get_log(
                f"Erro ao conectar com a url get_tarefas, código do erro HTTP: {str(resp.status_code)}".upper())
            return print(
                f"Erro ao conectar com a url get_tarefas, código do erro HTTP: {str(resp.status_code)}")

        if resp.text == '[]':
            get_log("Requisição não contém dados".upper())
            return print("Requisição não contém dados")

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
