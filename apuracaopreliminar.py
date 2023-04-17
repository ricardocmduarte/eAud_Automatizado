import db
import requests
import geral
from log import get_log
import json
from join_function import join_data


def get_apuracao_preliminar(ids_analise_preliminar):
    lista_dados = []
    lista_final = []
    try:
        if ids_analise_preliminar:
            for i, id in enumerate(ids_analise_preliminar):
                lista_dados.append(get_apuracao_preliminar_requisicao(id))
                if lista_dados == None:
                    break
                print(
                    f"Iteração get_apuracao_preliminar {str(i)} registrada com sucesso")

        # lista final passa por um tratamento de dados
        if lista_dados:
            lista_final = tratamento_dados(lista_dados)

        # comando para salvar os dados tratados
        if lista_final:
            salvar_dados(lista_final)
        get_log("Lista de achados ok")
        return print("Lista de achados ok")
    except NameError as err:
        get_log("Erro ao salvar os dados get_apuracao_preliminar".upper())
        get_log(err)
        return print("Erro ao salvar os dados get_apuracao_preliminar", err)


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

            anexosgerais = tarefa['campos']['anexosGerais']['valor']
            linkanalise = tarefa['campos']['linksDaAnalise']['valor']

            tarefasprecedentes = tarefa['campos']['tarefasPrecedentes']['valor']
            observadores = tarefa['campos']['observadores']['valor']
            hipoteselegal = tarefa['campos']['hipoteseLegal']['valor']

            descricaotag = tarefa['campos']['tags']['valor']
            tags = []
            if descricaotag:
                for i, tagdesc in enumerate(descricaotag):
                    tags.append(tagdesc['descricao'])

                tags = join_data(tags)

            matrizriscos = tarefa['campos']['matrizRiscosControles']['valor']
            matriz = matrizriscos

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
                'anexosgerais': anexosgerais,
                'linkanalise': linkanalise,
                'matrizachados': matriz,
                'tarefasprecedentes': tarefasprecedentes,
                'observadores': observadores,
                'hipoteselegal': hipoteselegal,
                'coordenadorequipe': coordenador,
                'equipegeral': equipe,
                'supervisores': supervisor,
                'tags': tags,
                'pendencias': listapendencia,
                'abasatividade': listaabaatividades,
            })
        get_log("Lista apuracao_preliminar tratada com sucesso")
        return lista_final
    except NameError as err:
        get_log("Erro ao tratar os dados apuracao_preliminar".upper())
        get_log(err)
        return print("Erro ao tratar os dados apuracao_preliminar", err)


def salvar_dados(lista_achados):
    try:
        banco = db.db_connection
        cur = banco.cursor()

        lista_achados = db.current_datetime_query(lista_achados)

        for tarefa in lista_achados:
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
                 tarefa['anexosgerais'],
                 tarefa['linkanalise'],
                 tarefa['matriz'],
                 tarefa['tarefasprecedentes'],
                 tarefa['observadores'],
                 tarefa['hipoteselegal'],
                 tarefa['coordenador'],
                 tarefa['equipe'],
                 tarefa['supervisor'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO achados_auditoria (id, situacao, estado, atividade, titulo, titulotarefaassociada,
                                                titulotarefaassociada,dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,anexosgerais,linkanalise,matriz,
                                                arquivoComportamentoEspecifico,matriz,tarefasprecedentes,observadores, hipoteselegal,
                                                coordenador,equipe,supervisor, tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
            get_log("Apuracao_preliminar salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log("Erro ao salvar os dados get_apuracao_preliminar".upper())
        get_log(err)
        return print("Erro ao salvar os dados get_apuracao_preliminar", err)


def get_apuracao_preliminar_requisicao(id):
    try:
        url = geral.url + \
            f"tarefa/{id}/dto/json"
        resp = requests.get(url, headers=geral.header)

        if resp.status_code != 200:
            get_log(
                f"Erro ao conectar com a url get_apuracao_preliminar, código do erro HTTP: {str(resp.status_code)}".upper())
            print(
                f"Erro ao conectar com a url get_apuracao_preliminar, código do erro HTTP: {str(resp.status_code)}")
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
