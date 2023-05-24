import db
import requests
import geral
from log import get_log
import json
from join_function import join_data

tipo_arquivo = 'get_analise_auditoria'


def get_analise_auditoria(ids):
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
                lista_dados.append(get_analise_auditoria_requisicao(id))

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

            unidadesenvolvidas = tarefa['campos']['unidEnvolvidas']['valor']
            nomeunidadesenvolvidas = []
            if unidadesenvolvidas:
                for i, envolvidasunidades in enumerate(unidadesenvolvidas):
                    nomeunidadesenvolvidas.append(envolvidasunidades['nome'])
                nomeunidadesenvolvidas = join_data(nomeunidadesenvolvidas)
            else:
                nomeunidadesenvolvidas = ''

            itemanaliseauditoria = tarefa['campos']['itensDaAnaliseAuditoria']['valor']
            idanaliseauditoria = []
            descteste = []
            desccriterio = []
            descinformacao = []
            descfonte = []
            desclimitacao = []
            descachado = []
            observacoes = []
            descricaoescopo = []
            valortotalescopo = []
            valorauditadoescopo = []
            anexoescopo = []
            responsavelitem = []
            anexoevidencia = []
            autoranexoevidencia = []
            for i, itens in enumerate(itemanaliseauditoria):
                idanaliseauditoria.append(itens['idAnaliseAuditoria'])
                descteste.append(itens['teste']['descTeste'])
                desccriterio.append(itens['teste']['descCriterio'])
                descinformacao.append(itens['teste']['descInformacao'])
                descfonte.append(itens['teste']['descFonte'])
                desclimitacao.append(itens['teste']['descLimitacao'])
                descachado.append(itens['teste']['descAchado'])
                observacoes.append(itens['observacao'])

            descescopo = itens['escopos']
            descricaoescopo = []
            for i, esc in enumerate(descescopo):
                descricaoescopo.append(esc['descricao'])
                valortotalescopo.append(esc['valorTotal'])
                valorauditadoescopo.append(esc['valorAuditado'])
                anexo = esc['anexo']
                if anexo:
                    anexoescopo.append(anexo['nome'])

                responsaveisitem = itens['responsaveis']
                for i, resp in enumerate(responsaveisitem):
                    responsavelitem.append(resp['nomeExibicao'])

                evidenciasitem = itens['evidencias']
                for i, evi in enumerate(evidenciasitem):
                    anexoevidencia.append(evi['anexo']['nome'])
                    autoranexoevidencia.append(evi['autor']['nome'])

            descteste = join_data(descteste)
            desccriterio = join_data(desccriterio)
            descinformacao = join_data(descinformacao)
            descfonte = join_data(descfonte)
            desclimitacao = join_data(desclimitacao)
            descachado = join_data(descachado)
            observacoes = join_data(observacoes)
            descricaoescopo = join_data(descricaoescopo)
            responsavelitem = join_data(responsavelitem)
            anexoescopo = join_data(anexoescopo)
            anexoevidencia = join_data(anexoevidencia)
            autoranexoevidencia = join_data(autoranexoevidencia)

            tarefasprecedentes = tarefa['campos']['tarefasPrecedentes']['valor']
            observadores = tarefa['campos']['observadores']['valor']
            hipoteselegal = tarefa['campos']['hipoteseLegal']['valor']

            matrizachados = tarefa['campos']['matrizAchados']['valor']
            matriz = matrizachados['nome'] if matrizachados else ''

            coordenadorequipe = tarefa['campos']['CoordenadorEquipe']['valor']
            coordenador = []
            if coordenadorequipe:
                for i, coordequipe in enumerate(coordenadorequipe):
                    coordenador.append(coordequipe['nomeExibicao'])

                coordenador = join_data(coordenador)
            else:
                coordenador = ''

            equipegeral = tarefa['campos']['EquipeGeral']['valor']
            equipe = []
            if equipegeral:
                for i, geralequipe in enumerate(equipegeral):
                    equipe.append(geralequipe['nomeExibicao'])

                equipe = join_data(equipe)
            else:
                equipe = ''

            supervisores = tarefa['campos']['EquipeGeral']['valor']
            supervisor = []
            if supervisores:
                for i, super in enumerate(supervisores):
                    supervisor.append(super['nomeExibicao'])

                supervisor = join_data(supervisor)
            else:
                supervisor = ''

            estadosituacao = tarefa['estadoSituacao'] if tarefa['estadoSituacao'] else ''

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
                'unidadesenvolvidas': nomeunidadesenvolvidas,
                'descteste': descteste,
                'desccriterio': desccriterio,
                'descinformacao': descinformacao,
                'descfonte': descfonte,
                'desclimitacao': desclimitacao,
                'descachado': descachado,
                'observacoes': observacoes,
                'descricaoescopo': descricaoescopo,
                'responsavelitem': responsavelitem,
                'anexoescopo': anexoescopo,
                'anexoevidencia': anexoevidencia,
                'autoranexoevidencia': autoranexoevidencia,
                'matrizachados': matriz,
                'tarefasprecedentes': tarefasprecedentes,
                'observadores': observadores,
                'hipoteselegal': hipoteselegal,
                'coordenadorequipe': coordenador,
                'equipegeral': equipe,
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
        get_log(
            f"Erro ao tratar os {tipo_arquivo} get_analise_auditoria".upper())
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
                 tarefa['unidadesenvolvidas'],
                 tarefa['descteste'],
                 tarefa['desccriterio'],
                 tarefa['descinformacao'],
                 tarefa['descfonte'],
                 tarefa['desclimitacao'],
                 tarefa['descachado'],
                 tarefa['observacoes'],
                 tarefa['descricaoescopo'],
                 tarefa['responsavelitem'],
                 tarefa['anexoescopo'],
                 tarefa['anexoevidencia'],
                 tarefa['autoranexoevidencia'],
                 tarefa['matrizachados'],
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
            insert_query = (f"""INSERT INTO analise_auditoria (id, situacao, estado, atividade, titulo, titulotarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,unidadesenvolvidas,
                                                descteste,desccriterio,descricaoescopo,responsavelitem,anexoescopo,anexoevidencia,autoranexoevidencia,
                                                descinformacao,descfonte,desclimitacao,descachado,observacoes,arquivoComportamentoEspecifico,
                                                matrizachados,tarefasprecedentes,observadores, hipoteselegal, estadosituacao,
                                                coordenadorequipe,equipegeral,supervisores, tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log("Analise_auditoria salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log("Erro ao salvar os dados get_analise_auditoria".upper())
        get_log(err)
        return print("Erro ao salvar os dados get_analise_auditoria", err)


def get_analise_auditoria_requisicao(id):
    try:
        url = geral.url + \
            f"tarefa/{id}/dto/json"
        resp = requests.get(url, headers=geral.header)

        if resp.status_code != 200:
            get_log(
                f"Erro ao conectar com a url get_analise_auditoria, código do erro HTTP: {str(resp.status_code)}".upper())
            print(
                f"Erro ao conectar com a url get_analise_auditoria, código do erro HTTP: {str(resp.status_code)}")
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
