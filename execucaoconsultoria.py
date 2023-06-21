import db
import requests
import geral
from log import get_log
import json
from join_function import join_data


tipo_arquivo = 'get_execucao_consultoria'


def get_execucao_consultoria(ids):
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
                lista_dados.append(get_execucao_requisicao(id))

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

                unidadesenvolvidas = tarefa['campos']['unidEnvolvidas']['valor']
                unidadesenvol = []
                if unidadesenvolvidas:
                    for i, unidade in enumerate(unidadesenvolvidas):
                        unidadesenvol.append(unidade['nomeExibicao'])
                    unidadesenvol = join_data(unidadesenvol)

                anexosgerais = tarefa['campos']['anexosGerais']['valor']
                anexos = []
                if anexosgerais:
                    for i, file in enumerate(anexosgerais):
                        anexos.append(file['nomeExibicao'])

                    anexos = join_data(anexos)

                tarefasprecedentes = tarefa['campos']['tarefasPrecedentes']['valor']
                tarefasprec = []
                if tarefasprecedentes:
                    for i, tarefapre in enumerate(tarefasprecedentes):
                        tarefasprec.append(tarefapre['nomeExibicao'])

                    tarefasprec = join_data(tarefasprec)

                observador = tarefa['campos']['observadores']['valor']
                observadores = []
                if observador:
                    for i, obs in enumerate(observador):
                        observadores.append(obs['nomeExibicao'])

                    observadores = join_data(observadores)

                hipotese = tarefa['campos']['hipoteseLegal']['valor']
                hipoteselegal = []
                if hipotese:
                    for i, hip in enumerate(hipotese):
                        hipoteselegal.append(hip['nomeExibicao'])

                    hipoteselegal = join_data(hipoteselegal)

                coordenadorequipe = tarefa['campos']['CoordenadorEquipe']['valor']
                coordenador = []
                if coordenadorequipe:
                    for i, coordequipe in enumerate(coordenadorequipe):
                        coordenador.append(coordequipe['nomeExibicao'])

                    coordenador = join_data(coordenador)

                equipegeral = tarefa['campos']['EquipeGeral']['valor']
                equipe = []
                if equipegeral:
                    for i, geralequipe in enumerate(equipegeral):
                        equipe.append(geralequipe['nomeExibicao'])

                    equipe = join_data(equipe)

                supervisores = tarefa['campos']['EquipeGeral']['valor']
                supervisor = []
                if supervisores:
                    for i, super in enumerate(supervisores):
                        supervisor.append(super['nomeExibicao'])

                    supervisor = join_data(supervisor)

                papeis = tarefa['campos']['papeisTrabalho']['valor']
                papeistrabalho = []
                if papeis:
                    for i, papers in enumerate(papeis):
                        papeistrabalho.append(papers['nomeExibicao'])

                    papeistrabalho = join_data(papeistrabalho)

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
                    'unidadesenvolvidas': unidadesenvol,
                    'anexosgerais': anexos,
                    'tarefasprecedentes': tarefasprec,
                    'observadores': observadores,
                    'hipoteselegal': hipoteselegal,
                    'coordenadorequipe': coordenador,
                    'equipegeral': equipe,
                    'supervisores': supervisor,
                    'papeistrabalho': papeistrabalho,
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
                 tarefa['anexosgerais'],
                 tarefa['tarefasprecedentes'],
                 tarefa['observadores'],
                 tarefa['hipoteselegal'],
                 tarefa['coordenadorequipe'],
                 tarefa['equipegeral'],
                 tarefa['supervisores'],
                 tarefa['papeistrabalho'],
                 tarefa['estadosituacao'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO execucao_consultoria (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,unidadesenvolvidas,anexosgerais,tarefasprecedentes,
                                                observadores,hipoteselegal,coordenadorequipe,equipegeral,supervisores,papeistrabalho,estadosituacao,
                                                arquivocomportamentoespecifico,tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_execucao_requisicao(id):
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
