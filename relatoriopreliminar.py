import db
import requests
import geral
from log import get_log
import json
from join_function import join_data


tipo_arquivo = 'get_relatorio_preliminar'


def get_relatorio_preliminar(ids_relatorio):

    lista_dados = []
    lista_final = []
    try:
        if ids_relatorio:
            for i, id in enumerate(ids_relatorio):
                lista_dados.append(get_relatorio_preliminar_requisicao(id))
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

            relatoriopreliminar = tarefa['campos']['relatorioPreliminar']['valor']['nome']

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

            relatorioword = tarefa['campos']['relatorioWord']['valor']['nome']

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

            observadores = tarefa['campos']['observadores']['valor']

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

                anexorelatoriopreliminar = join_data(anexorelatoriopreliminar)

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
                'supervisor': supervisores,
                'parecer': pareceres,
                'anexorelatorio': anexorelatoriopreliminar,
                'relatorioword': relatorioword,
                'unidadesenvolvidas': unidadesenvolvidas,
                'relatoriocom': relatoriocom,
                'observadores': observadores,
                'certificados': certificados,
                'equipegeral': equipegeral,
                'arquivocomportamento': arquivocomportamento,
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


def salvar_dados(lista_relatorio_preliminar):
    try:
        banco = db.db_connection
        cur = banco.cursor()

        lista_relatorio_preliminar = db.current_datetime_query(
            lista_relatorio_preliminar)

        for tarefa in lista_relatorio_preliminar:
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
                 tarefa['relatoriopreliminar'],
                 tarefa['hipoteselegal'],
                 tarefa['relatoriofinal'],
                 tarefa['coordenadorequipe'],
                 tarefa['supervisor'],
                 tarefa['parecer'],
                 tarefa['anexorelatorio'],
                 tarefa['relatorioword'],
                 tarefa['unidadesenvolvidas'],
                 tarefa['relatoriocom'],
                 tarefa['observadores'],
                 tarefa['certificados'],
                 tarefa['equipegeral'],
                 tarefa['arquivocomportamento'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['listapendencia'],
                 tarefa['listaabaatividades'],
                 tarefa['dataatualizacao'],
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO achados_auditoria (id, situacao, estado, atividade, titulo, titulotarefaassociada,
                                                titulotarefaassociada,dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,relatoriopreliminar,hipoteselegal,coordenadorequipe,supervisor,
                                                parecer,anexorelatorio,relatorioword,unidadesenvolvidas,relatoriocom,observadores,certificados,
                                                equipegeral,arquivocomportamento, estadosituacao,
                                                tags,listapendencia,listaabaatividades,dataatualizacao) VALUES {array_records}""",)

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
