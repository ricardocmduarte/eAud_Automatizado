import db
import requests
import geral
from log import get_log
import json
from join_function import join_data


tipo_arquivo = 'get_kpa_iacm'


def get_kpa_iacm(ids):
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
                lista_dados.append(get_kpa_requisicao(id))
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

            kpaconclusao = tarefa['campos']['conclusaoKPA']['valor']
            conclusaokpa = []
            if kpaconclusao:
                for i, kpa in enumerate(kpaconclusao):
                    conclusaokpa.append(kpa['valor'])

                conclusaokpa = join_data(conclusaokpa)

            objetivokpa = tarefa['campos']['objkpa']['valor']

            anexgeral = tarefa['campos']['anexosGerais']['valor']
            anexosgerais = []
            if anexgeral:
                for i, file in enumerate(anexgeral):
                    anexosgerais.append(file['nome'])

                anexosgerais = join_data(anexosgerais)

            equipevalicadacao = tarefa['campos']['equipeValidacaoExternaIACM']['valor']
            equipevalidacaoexternaiacm = []
            if equipevalicadacao:
                for i, equipe in enumerate(equipevalicadacao):
                    equipevalidacaoexternaiacm.append(equipe['nomeExibicao'])

                equipevalidacaoexternaiacm = join_data(
                    equipevalidacaoexternaiacm)

            atividadeskpa = tarefa['campos']['atividadesKPA']['valor']

            equipeavaliacao = tarefa['campos']['equipeAvaliacaoIACM']['valor']
            equipeavaliacaoiacm = []
            if equipeavaliacao:
                for i, equipe in enumerate(equipeavaliacao):
                    equipeavaliacaoiacm.append(equipe['nomeExibicao'])

                equipeavaliacaoiacm = join_data(equipeavaliacaoiacm)

            kpamodel = tarefa['campos']['kpaModelo']['valor']
            titulokpamodelo = kpamodel['nomeExibicao']
            dtrealizadamodelokpa = kpamodel['dataRealizadaInicio']
            dtfimmodelokpa = kpamodel['dataRealizadaFim']
            assuntomodelokpa = kpamodel['assunto']

            unidadevalidadora = tarefa['campos']['unidadesValidadorasIACM']['valor']
            unidadesvalidadoras = []
            if unidadevalidadora:
                for i, unidade in enumerate(unidadevalidadora):
                    unidadesvalidadoras.append(unidade['nomeExibicao'])

                unidadesvalidadoras = join_data(unidadesvalidadoras)

            produtokpa = tarefa['campos']['produtoKPA']['valor']
            resultadoskpa = tarefa['campos']['resultadosKPA']['valor']

            tag = tarefa['campos']['tags']['valor']
            tags = []
            if tag:
                for i, tagtag in enumerate(tag):
                    tags.append(tagtag['descricao'])

                tags = join_data(tags)

            praticakpa = tarefa['campos']['praticasKPA']['valor']

            link = tarefa['campos']['links']['valor']
            links = []
            if link:
                for i, lin in enumerate(link):
                    links.append(lin['valor'])

                links = join_data(links)

            uaig = tarefa['campos']['uaig']['valor']['nomeExibicao']

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
                'conclusaokpa': conclusaokpa,
                'anexosgerais': anexosgerais,
                'objetivokpa': objetivokpa,
                'equipevalidacaoexternaiacm': equipeavaliacaoiacm,
                'atividaeskpa': atividadeskpa,
                'equipeavaliacaoiacm': equipeavaliacaoiacm,
                'titulokpamodelo': titulokpamodelo,
                'datarealizadamodelokpa': dtrealizadamodelokpa,
                'datafimmodelokpa': dtfimmodelokpa,
                'assundomodelokpa': assuntomodelokpa,
                'unidadesvalidadoras': unidadesvalidadoras,
                'produtokpa': produtokpa,
                'resultadoskpa': resultadoskpa,
                'praticakpa': praticakpa,
                'links': links,
                'uaigs': uaig,
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
                 tarefa['conclusaokpa'],
                 tarefa['anexosgerais'],
                 tarefa['objetivokpa'],
                 tarefa['equipevalidacaoexternaiacm'],
                 tarefa['atividaeskpa'],
                 tarefa['equipeavaliacaoiacm'],
                 tarefa['titulokpamodelo'],
                 tarefa['datarealizadamodelokpa'],
                 tarefa['datafimmodelokpa'],
                 tarefa['assundomodelokpa'],
                 tarefa['unidadesvalidadoras'],
                 tarefa['produtokpa'],
                 tarefa['resultadoskpa'],
                 tarefa['praticakpa'],
                 tarefa['links'],
                 tarefa['uaigs'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['listapendencia'],
                 tarefa['listaabaatividades']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO kpa_iacm (id, situacao, estado, atividade, titulo, titulotarefaassociada,
                                                titulotarefaassociada,dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,conclusaokpa,anexosgerais,estadosituacao,
                                                objetivokpa,equipevalidacaoexternaiacm, atividaeskpa,titulokpamodelo, datarealizadamodelokpa, 
                                                datafimmodelokpa, assundomodelokpa,unidadesvalidadoras, produtokpa, resultadoskpa, 
                                                praticakpa, links,uaigs, arquivocomportamentoespecifico,estadosituacao
                                                tags,listapendencia,listaabaatividades) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_kpa_requisicao(id):
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
