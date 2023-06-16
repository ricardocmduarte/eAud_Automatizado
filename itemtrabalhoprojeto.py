import db
import requests
import geral
from log import get_log
import json
from join_function import join_data


tipo_arquivo = 'get_item_trabalho_projeto'


def get_item_trabalho_projeto(ids):
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
                lista_dados.append(get_item_projeto_requisicao(id))

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

            id = tarefa['id']
            situacao = tarefa['situacao']
            estado = tarefa['estado']
            atividade = tarefa['atividade']
            titulo = tarefa['titulo']
            idtarefaassociada = tarefa['idTarefaAssociada'] if tarefa['idTarefaAssociada'] else ''
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

            unidadeexec = tarefa['campos']['unidadeExecutora']['valor']
            unidadeexecutoras = []
            if unidadeexec:
                for i, unidade in enumerate(unidadeexec):
                    unidadeexecutoras.append(unidade['nomeExibicao'])

                unidadeexecutoras = join_data(unidadeexecutoras)

            detalhamento = tarefa['campos']['Detalhamento']['valor']

            anexosgerais = tarefa['campos']['anexosGerais']['valor']
            anexos = []
            if anexosgerais:
                for i, file in enumerate(anexosgerais):
                    anexos.append(file['nomeExibicao'])

                anexos = join_data(anexos)

            processosassociados = tarefa['campos']['processosAssociados']['valor']
            produtouaig = tarefa['campos']['produtoUaig']['valor']

            supervisor = tarefa['campos']['unidEnvolvidas']['valor']
            supervisores = []
            if supervisor:
                for i, super in enumerate(supervisor):
                    supervisores.append(super['nomeExibicao'])

                supervisores = join_data(supervisores)

            link = tarefa['campos']['tarefasPrecedentes']['valor']
            links = []
            if link:
                for i, lin in enumerate(link):
                    links.append(lin['descricao'] + '|' + lin['url'])

                links = join_data(links)

            homemhora = tarefa['campos']['hhTarefa']['valor']

            unidadeenvolvida = tarefa['campos']['unidEnvolvidas']['valor']
            unidadesenvolvidas = []
            if unidadeenvolvida:
                for i, unidade in enumerate(unidadeenvolvida):
                    unidadesenvolvidas.append(unidade['nomeExibicao'])

                unidadesenvolvidas = join_data(unidadesenvolvidas)

            destusuariounidade = tarefa['campos']['destinatarioUsuarioUnidade']['valor']
            destinatariousuariounidade = []
            if destusuariounidade:
                destinatariousuariounidade = unidade['nomeExibicao']

            tarefasprec = tarefa['campos']['tarefasPrecedentes']['valor']
            tarefasprecedentes = []
            if tarefasprec:
                for i, tarefapre in enumerate(tarefasprec):
                    tarefasprecedentes.append(tarefapre['nomeExibicao'])

                tarefasprecedentes = join_data(tarefasprecedentes)

            executor = tarefa['campos']['executores']['valor']
            executores = []
            if executor:
                for i, obs in enumerate(executor):
                    executores.append(obs['nomeExibicao'])

                executores = join_data(executores)

            descricaotag = tarefa['campos']['tags']['valor']
            tags = []
            if descricaotag:
                for i, tagdesc in enumerate(descricaotag):
                    tags.append(tagdesc['descricao'])

                tags = join_data(tags)

            estadosituacao = tarefa['estadoSituacao']
            arquivocomportamento = tarefa['arquivoComportamentoEspecifico']

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
                'unidadesexecutoras': unidadeexecutoras,
                'detalhamento': detalhamento,
                'anexosgerais': anexos,
                'processoassociado': processosassociados,
                'produtouaig': produtouaig,
                'supervisores': supervisores,
                'links': links,
                'homemhora': homemhora,
                'unidadesenvolvidas': unidadesenvolvidas,
                'destinatariousuariounidade': destinatariousuariounidade,
                'tarefasprecedentes': tarefasprecedentes,
                'executores': executores,
                'tags': tags,
                'estadosituacao': estadosituacao,
                'arquivocomportamentoespecifico': arquivocomportamento,
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
                 tarefa['unidadesexecutoras'],
                 tarefa['detalhamento'],
                 tarefa['anexosgerais'],
                 tarefa['processoassociado'],
                 tarefa['produtouaig'],
                 tarefa['supervisores'],
                 tarefa['links'],
                 tarefa['homemhora'],
                 tarefa['unidadesenvolvidas'],
                 tarefa['destinatariousuariounidade'],
                 tarefa['tarefasprecedentes'],
                 tarefa['executores'],
                 tarefa['estadosituacao'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO item_trabalho_projeto (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,unidadesexecutoras,detalhamento,
                                                anexosgerais,processoassociado,produtouaig,supervisores,links,homemhora,unidadesenvolvidas,
                                                destinatariousuariounidade,tarefasprecedentes,executores,arquivocomportamentoespecifico,estadosituacao,
                                                tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_item_projeto_requisicao(id):
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
