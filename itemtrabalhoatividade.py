import db
import requests
import geral
from log import get_log
import json
from join_function import join_data


tipo_arquivo = 'get_item_trabalho_atividade'


def get_item_trabalho_atividade(ids_item_atividade):

    lista_dados = []
    lista_final = []
    try:
        if ids_item_atividade:
            for i, id in enumerate(ids_item_atividade):
                lista_dados.append(get_item_atividade_requisicao(id))
                if lista_dados == None:
                    break
                print(
                    f"Iteração {tipo_arquivo} {str(i)} registrada com sucesso")

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
            idtarefaassociada = tarefa['idTarefaAssociada']
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
            processt = tarefa['campos']['processT']['valor']['valor']

            origemdemanda = tarefa['campos']['origemDemanda']['valor']['valor']

            link = tarefa['campos']['tarefasPrecedentes']['valor']
            links = []
            if link:
                for i, lin in enumerate(link):
                    links.append(lin['nomeExibicao'])

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
                for i, unidade in enumerate(destusuariounidade):
                    destinatariousuariounidade.append(unidade['nomeExibicao'])

                destinatariousuariounidade = join_data(
                    destinatariousuariounidade)

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
                'processt': processt,
                'origemdemanda': origemdemanda,
                'links': links,
                'homemhora': homemhora,
                'unidadesenvolvidas': unidadesenvolvidas,
                'destinatariousuariounidade': destinatariousuariounidade,
                'tarefasprecedentes': tarefasprecedentes,
                'executor': executores,
                'tags': tags,
                'estadosituacao': estadosituacao,
                'pendencias': listapendencia,
                'abasatividade': listaabaatividades,
            })

        get_log(f"Lista {tipo_arquivo} tratada com sucesso")
        return lista_final
    except NameError as err:
        get_log(f"Erro ao tratar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao tratar os dados {tipo_arquivo}", err)


def salvar_dados(lista_iacm):
    try:
        banco = db.db_connection
        cur = banco.cursor()

        lista_iacm = db.current_datetime_query(lista_iacm)

        for tarefa in lista_iacm:
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
                 tarefa['unidadeexecutoras'],
                 tarefa['detalhamento'],
                 tarefa['anexos'],
                 tarefa['processosassociados'],
                 tarefa['processt'],
                 tarefa['origemdemanda'],
                 tarefa['links'],
                 tarefa['homemhora'],
                 tarefa['unidadesenvolvidas'],
                 tarefa['destinatariousuariounidade'],
                 tarefa['tarefasprecedentes'],
                 tarefa['executores'],
                 tarefa['tags'],
                 tarefa['listapendencia'],
                 tarefa['listaabaatividades'],
                 tarefa['dataatualizacao'],
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO achados_auditoria (id, situacao, estado, atividade, titulo, titulotarefaassociada,
                                                titulotarefaassociada,dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,unidadeexecutoras,detalhamento,anexos,
                                                processosassociados,processt,origemdemanda,links,homemhora,unidadesenvolvidas,destinatariousuariounidade,
                                                tarefasprecedentes,executores,,estadosituacao,
                                                tags,listapendencia,listaabaatividades,dataatualizacao) VALUES {array_records}""")

            cur.execute(insert_query, lista)
            get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_item_atividade_requisicao(id):
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
