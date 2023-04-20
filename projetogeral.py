import db
import requests
import geral
from log import get_log
import json
from join_function import join_data


tipo_arquivo = 'get_projeto_geral'


def get_projeto_geral(ids):
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
                lista_dados.append(get_projeto_requisicao(id))
                if lista_dados == None:
                    break
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

            detalhamento = tarefa['campos']['Detalhamento']['valor']
            numdenuncia = tarefa['campos']['numDenuncia']['valor']

            localtrabalho = tarefa['campos']['localidadesPlanoTrabalho']['valor']
            localidadesplanotrabalho = []
            if localtrabalho:
                for i, local in enumerate(localtrabalho):
                    localidadesplanotrabalho.append(
                        local['nomeExibicao'] + local['gruposLocalidade'])

                localidadesplanotrabalho = join_data(localidadesplanotrabalho)

            proponenteplanotrabalho = tarefa['campos']['proponentePlanoTrabalho']['valor']
            etapaplanotrabalho = tarefa['campos']['etapaPlanoTrabalho']['valor']['valor']
            processt = tarefa['campos']['processT']['valor']['valor']
            responsavelplanotrabalho = tarefa['campos']['responsavelPlanoTrabalho']['valor']
            origemdemanda = tarefa['campos']['origemDemanda']['valor']['valor']

            link = tarefa['campos']['links']['valor']
            links = []
            if link:
                for i, lin in enumerate(link):
                    links.append(lin['valor'])

                links = join_data(links)

            anexplanotrabalho = tarefa['campos']['anexosPlanoTrabalho']['valor']
            anexoplanotrabalho = []
            if anexplanotrabalho:
                for i, file in enumerate(anexoplanotrabalho):
                    anexoplanotrabalho.append(file['nomeExibicao'])

                anexoplanotrabalho = join_data(anexoplanotrabalho)

            processoplanotrabalho = tarefa['campos']['processoTrabalhoPlanoTrabalho']['valor']

            resulesperado = tarefa['campos']['resultadosEsperadosPlanoTrabalho']['valor']
            resultadosesperados = []
            if resulesperado:
                for i, resultado in enumerate(resulesperado):
                    resultadosesperados.append(resultado['nomeExibicao'])

                resultadosesperados = join_data(resultadosesperados)

            objetocge = tarefa['campos']['objetoscgemg']['valor']
            objetoscgemg = []
            if objetocge:
                for i, objetos in enumerate(objetocge):
                    objetoscgemg.append(objetos['valor'])

                objetoscgemg = join_data(objetoscgemg)

            duracaomeses = tarefa['campos']['duracaoMesesPlanoTrabalho']['valor']
            recursofinanceiro = tarefa['campos']['recursoFinanceiroPlanoTrabalho']['valor']

            envolplanotrabalho = tarefa['campos']['envolvidosPlanoTrabalho']['valor']
            envolvidosplanotrabalho = []
            if envolplanotrabalho:
                for i, envolvidos in enumerate(envolplanotrabalho):
                    envolvidosplanotrabalho.append(envolvidos['nomeExibicao'])

                envolvidosplanotrabalho = join_data(envolvidosplanotrabalho)

            tag = tarefa['campos']['tags']['valor']
            tags = []
            if tag:
                for i, tagtag in enumerate(tag):
                    tags.append(tagtag['descricao'])

                tags = join_data(tags)

            homemhora = tarefa['campos']['homemHorasPlanoTrabalho']['valor']

            gerenteplanotrabalho = tarefa['campos']['gerentesPlanoTrabalho']['valor']
            gerentesplanotrabalho = []
            if gerenteplanotrabalho:
                for i, gerente in enumerate(gerenteplanotrabalho):
                    gerentesplanotrabalho.append(gerente['nomeExibicao'])

                gerentesplanotrabalho = join_data(gerentesplanotrabalho)

            equipe = tarefa['campos']['EquipeGeral']['valor']
            equipegeral = []
            if equipe:
                for i, team in enumerate(equipe):
                    equipegeral.append(team['nomeExibicao'])

                equipegeral = join_data(equipegeral)

            supervisor = tarefa['campos']['supervisoresPlanoTrabalho']['valor']
            supervisores = []
            if supervisor:
                for i, super in enumerate(supervisor):
                    supervisores.append(super['nomeExibicao'])

                supervisores = join_data(supervisores)

            objetivoplanotrabalho = tarefa['campos']['objetivoPlanoTrabalho']['valor']
            tipoplanotrablho = tarefa['campos']['tipoPlanoTrabalho']['valor']
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
                'numdenuncia': numdenuncia,
                'detalhamento': detalhamento,
                'localidadesplanotrabalho': localidadesplanotrabalho,
                'proponenteplanotrabalho': proponenteplanotrabalho,
                'etapaplanotrabalho': etapaplanotrabalho,
                'processt': processt,
                'responsavelplanotrabalho': responsavelplanotrabalho,
                'origemdemanda': origemdemanda,
                'links': links,
                'anexoplanotrabalho': anexoplanotrabalho,
                'processoplanotrabalho': processoplanotrabalho,
                'resultadosesperados': resultadosesperados,
                'objetoscgemg': objetoscgemg,
                'duracaomeses': duracaomeses,
                'recursofinanceiro': recursofinanceiro,
                'envolvidosplanotrabalho': envolvidosplanotrabalho,
                'homemhora': homemhora,
                'gerentesplanotrabalho': gerentesplanotrabalho,
                'equipegeral': equipegeral,
                'supervisores': supervisores,
                'objetivoplanotrabalho': objetivoplanotrabalho,
                'tipoplanotrabalho': tipoplanotrablho,
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
                 tarefa['numdenuncia'],
                 tarefa['detalhamento'],
                 tarefa['detalhamento'],
                 tarefa['proponenteplanotrabalho'],
                 tarefa['etapaplanotrabalho'],
                 tarefa['processt'],
                 tarefa['responsavelplanotrabalho'],
                 tarefa['origemdemanda'],
                 tarefa['links'],
                 tarefa['anexoplanotrabalho'],
                 tarefa['processoplanotrabalho'],
                 tarefa['resultadosesperados'],
                 tarefa['objetoscgemg'],
                 tarefa['duracaomeses'],
                 tarefa['recursofinanceiro'],
                 tarefa['envolvidosplanotrabalho'],
                 tarefa['homemhora'],
                 tarefa['gerentesplanotrabalho'],
                 tarefa['equipegeral'],
                 tarefa['supervisores'],
                 tarefa['objetivoplanotrabalho'],
                 tarefa['tipoplanotrabalho'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['listapendencia'],
                 tarefa['listaabaatividades']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO projeto_geral (id, situacao, estado, atividade, titulo, titulotarefaassociada,
                                                titulotarefaassociada,dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,numdenuncia,detalhamento,etapaplanotrabalho, processt,
                                                responsavelplanotrabalho,origemdemanda,links,anexoplanotrabalho,processoplanotrabalho,
                                                resultadosesperados,objetoscgemg,duracaomeses,recursofinanceiro,envolvidosplanotrabalho,homemhora,
                                                gerentesplanotrabalho,equipegeral,supervisores,objetivoplanotrabalho,tipoplanotrabalho,arquivocomportamentoespecifico, estadosituacao,
                                                tags,listapendencia,listaabaatividades) VALUES {array_records}""",)

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_projeto_requisicao(id):
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
