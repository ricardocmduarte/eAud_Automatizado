import db
import requests
import geral
from log import get_log
import json
from join_function import join_data


tipo_arquivo = 'get_analise_preliminar'


def get_analise_preliminar(ids):
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
                lista_dados.append(get_analise_preliminar_requisicao(id))

                print(
                    f"Iteração {tipo_arquivo} {str(i)} registrada com sucesso")

        get_log(
            f"Esta requisicao {tipo_arquivo} contém {len(lista_final)} itens")

        # lista final passa por um tratamento de dados
        if lista_dados:
            lista_final = tratamento_dados(lista_dados)

        # comando para salvar os dados tratados
        if lista_final:
            salvar_dados(lista_final)
        get_log("Lista de achados ok")
        return print("Lista de achados ok")
    except NameError as err:
        get_log("Erro ao salvar os dados get_analise_preliminar".upper())
        get_log(err)
        return print("Erro ao salvar os dados get_analise_preliminar", err)


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

            unidadesenvolvidas = tarefa['campos']['unidEnvolvidas']['valor']
            nomeunidadesenvolvidas = []
            if unidadesenvolvidas:
                for i, envolvidasunidades in enumerate(unidadesenvolvidas):
                    nomeunidadesenvolvidas.append(envolvidasunidades['nome'])

                nomeunidadesenvolvidas = join_data(nomeunidadesenvolvidas)

            anexosgerais = tarefa['campos']['anexosGerais']['valor']
            anexos = []
            if anexosgerais:
                for i, anexo in enumerate(anexosgerais):
                    anexos.append(anexo['nome'])

                anexos = join_data(anexos)

            anexosanalisepreliminar = tarefa['campos']['anexosAnalisePreliminar']['valor']
            anexosanalise = []
            if anexosanalisepreliminar:
                for i, anexo in enumerate(anexosanalisepreliminar):
                    anexosanalise.append(anexo['nome'])

                anexosanalise = join_data(anexosanalise)

            tarefasprecedentes = tarefa['campos']['tarefasPrecedentes']['valor']
            observadores = tarefa['campos']['observadores']['valor']
            hipoteselegal = tarefa['campos']['hipoteseLegal']['valor']

            universoauditavel = tarefa['campos']['universosAuditaveisAnalisePreliminar']['valor']
            objetosauditoria = tarefa['campos']['objetosAuditoriaAnalisePreliminar']['valor']

            coordenadorequipe = tarefa['campos']['CoordenadorEquipe']['valor']
            coordenador = []
            if coordenadorequipe:
                for i, coordequipe in enumerate(coordenadorequipe):
                    coordenador.append(coordequipe['nomeExibicao'])

                coordenador = join_data(coordenador)

            matriz = tarefa['campos']['matrizRiscosControles']['valor']
            if matriz:
                matrizcontrole = matriz['nome']

            equipegeral = tarefa['campos']['EquipeGeral']['valor']
            equipe = []
            if equipegeral:
                for i, geralequipe in enumerate(equipegeral):
                    equipe.append(geralequipe['nomeExibicao'])

                equipe = join_data(equipe)

            classificacaoacesso = tarefa['campos']['classificacaoAcesso']['valor']

            supervisores = tarefa['campos']['EquipeGeral']['valor']
            supervisor = []
            if supervisores:
                for i, super in enumerate(supervisores):
                    supervisor.append(super['nomeExibicao'])

                supervisor = join_data(supervisor)

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
            'unidadesenvolvidas': nomeunidadesenvolvidas,
            'universosauditaveis': universoauditavel,
            'anexosgerais': anexos,
            'objetosauditoria': objetosauditoria,
            'matrizcontrole': matrizcontrole,
            'tarefasprecedentes': tarefasprecedentes,
            'observadores': observadores,
            'hipoteselegal': hipoteselegal,
            'coordenadorequipe': coordenador,
            'equipegeral': equipe,
            'classificacaoacesso': classificacaoacesso,
            'supervisores': supervisor,
            'arquivocomportamentoespecifico': arquivocomportamento,
            'estadosituacao': estadosituacao,
            'tags': descricaotag,
            'pendencias': listapendencia,
            'abasatividade': listaabaatividades,
        })
        get_log("Lista analise_preliminar tratada com sucesso")
        return lista_final
    except NameError as err:
        get_log("Erro ao tratar os dados get_analise_preliminar".upper())
        get_log(err)
        return print("Erro ao tratar os dados get_analise_preliminar", err)


def salvar_dados(resultado_array):
    try:
        banco = db.db_connection
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
                 tarefa['nomeunidadesenvolvidas'],
                 tarefa['universoauditavel'],
                 tarefa['anexos'],
                 tarefa['objetosauditoria'],
                 tarefa['matrizcontrole'],
                 tarefa['tarefasprecedentes'],
                 tarefa['observadores'],
                 tarefa['hipoteselegal'],
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
            insert_query = (f"""INSERT INTO analise_preliminar (id, situacao, estado, atividade, titulo, titulotarefaassociada,
                                                titulotarefaassociada,dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,nomeunidadesenvolvidas,universoauditavel,anexos,
                                                arquivoComportamentoEspecifico,objetosauditoria,matrizcontrole,tarefasprecedentes,
                                                observadores, hipoteselegal,coordenadorequipe,equipegeral,supervisores, arquivocomportamentoespecifico,
                                                estadosituacao,tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
            get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_analise_preliminar_requisicao(id):
    try:
        url = geral.url + \
            f"tarefa/{id}/dto/json"
        resp = requests.get(url, headers=geral.header)

        if resp.status_code != 200:
            get_log(
                f"Erro ao conectar com a url get_analise_preliminar, código do erro HTTP: {str(resp.status_code)}".upper())
            print(
                f"Erro ao conectar com a url get_analise_preliminar, código do erro HTTP: {str(resp.status_code)}")
            return None

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
