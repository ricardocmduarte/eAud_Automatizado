import db
import requests
import geral
from log import get_log
import json
from join_function import join_data

tipo_arquivo = 'get_atividade_continuada'


def get_atividade_continuada(ids):
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
                lista_dados.append(get_atividade_continuada_requisicao(id))
                if lista_dados == None:
                    break
                print(
                    f"Iteração get_atividade_continuada {str(i)} registrada com sucesso")

        get_log(
            f"Esta requisicao {tipo_arquivo} contém {len(lista_final)} itens")

        # lista final passa por um tratamento de dados
        if lista_dados:
            lista_final = tratamento_dados(lista_dados)

        # comando para salvar os dados tratados
        if lista_final:
            salvar_dados(lista_final)
        get_log("Lista de atividade continuada ok")
        return print("Lista de atividade continuada ok")
    except NameError as err:
        get_log("Erro ao salvar os dados get_atividade_continuada".upper())
        get_log(err)
        return print("Erro ao salvar os dados get_atividade_continuada", err)


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
            localidades = tarefa['campos']['localidadesPlanoTrabalho']['valor']
            localtrabalho = []
            if localidades:
                for i, local in enumerate(localidades):
                    localtrabalho.append(local['nomeExibicao'])

                localtrabalho = join_data(localtrabalho)

            proponenteplanotrabalho = tarefa['campos']['proponentePlanoTrabalho']['valor']
            etapaplanotrabalho = tarefa['campos']['etapaPlanoTrabalho']['valor']
            responsavelplanotrabalho = tarefa['campos']['responsavelPlanoTrabalho']['valor']

            links = tarefa['campos']['links']['valor']
            linktarefa = []
            if links:
                for i, link in enumerate(links):
                    linktarefa.append(link['descricao'] + ' | ' + link['url'])

                linktarefa = join_data(linktarefa)

            anexosplanotrabalho = tarefa['campos']['anexosPlanoTrabalho']['valor']
            anexos = []
            if anexosplanotrabalho:
                for i, anexo in enumerate(anexosplanotrabalho):
                    anexos.append(anexo['nomeExibicao'])

                anexos = join_data(anexos)

            processoplanotrabalho = tarefa['campos']['processoTrabalhoPlanoTrabalho']['valor']

            resultadoesperado = tarefa['campos']['resultadosEsperadosPlanoTrabalho']['valor']
            resultados = []
            if resultadoesperado:
                for i, resul in enumerate(resultadoesperado):
                    resultados.append(resul['nomeExibicao'])

                resultados = join_data(resultados)

            tarefasprecedentes = tarefa['campos']['tarefasPrecedentes']['valor']
            recursofinanceiro = tarefa['campos']['recursoFinanceiroPlanoTrabalho']['valor']

            envolvidosplanotrabalho = tarefa['campos']['envolvidosPlanoTrabalho']['valor']
            envolvidos = []
            if envolvidosplanotrabalho:
                for i, envolv in enumerate(envolvidosplanotrabalho):
                    envolvidos.append(envolv['nomeExibicao'])

                envolvidos = join_data(envolvidos)

            homemhora = tarefa['campos']['homemHorasPlanoTrabalho']['valor']

            descricaotag = tarefa['campos']['tags']['valor']
            tags = []
            if descricaotag:
                for i, tagdesc in enumerate(descricaotag):
                    tags.append(tagdesc['descricao'])

                tags = join_data(tags)

            gerentes = tarefa['campos']['gerentesPlanoTrabalho']['valor']
            gerente = []
            if gerentes:
                for i, gere in enumerate(gerentes):
                    gerente.append(gere['nomeExibicao'])

                gerente = join_data(gerente)

            supervisoresplano = tarefa['campos']['supervisoresPlanoTrabalho']['valor']
            supervisorplano = []
            if supervisoresplano:
                for i, supervi in enumerate(supervisoresplano):
                    supervisorplano.append(supervi['nomeExibicao'])

                supervisorplano = join_data(supervisorplano)

            tipoplano = tarefa['campos']['tipoPlanoTrabalho']['valor']['valor']

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
            'detalhamento': detalhamento,
            'propopenente': proponenteplanotrabalho,
            'etapaplano': etapaplanotrabalho,
            'responsavel': responsavelplanotrabalho,
            'processoplanotrabalho': processoplanotrabalho,
            'localidade': localtrabalho,
            'links': linktarefa,
            'tarefasprecedentes': tarefasprecedentes,
            'resultados': resultados,
            'recurso': recursofinanceiro,
            'envolvidos': envolvidos,
            'homemhora': homemhora,
            'gerentes': gerente,
            'supervisorplanotrabalho': supervisorplano,
            'tipoplano': tipoplano,
            'tags': tags,
            'pendencias': listapendencia,
            'abasatividade': listaabaatividades,
        })
        get_log("Lista get_atividade_continuada tratada com sucesso")
        return lista_final
    except NameError as err:
        get_log("Erro ao tratar os dados get_atividade_continuada".upper())
        get_log(err)
        return print("Erro ao tratar os dados get_atividade_continuada", err)


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
                 tarefa['detalhamento'],
                 tarefa['proponenteplanotrabalho'],
                 tarefa['etapaplanotrabalho'],
                 tarefa['responsavelplanotrabalho'],
                 tarefa['processoplanotrabalho'],
                 tarefa['localtrabalho'],
                 tarefa['linktarefa'],
                 tarefa['tarefasprecedentes'],
                 tarefa['resultados'],
                 tarefa['recursofinanceiro'],
                 tarefa['envolvidos'],
                 tarefa['homemhora'],
                 tarefa['gerente'],
                 tarefa['supervisorplano'],
                 tarefa['tipoplano'],
                 tarefa['tags'],
                 tarefa['listapendencia'],
                 tarefa['listaabaatividades'],
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO achados_auditoria (id, situacao, estado, atividade, titulo, titulotarefaassociada,
                                                titulotarefaassociada,dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,detalhamento,proponenteplanotrabalho,etapaplanotrabalho,
                                                localtrabalho,linktarefa,resultados,recursofinanceiro,envolvidos,homemhora,gerente,supervisorplano,
                                                tipoplano,arquivoComportamentoEspecifico, tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
            get_log("Atividade_continuada salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log("Erro ao salvar os dados get_atividade_continuada".upper())
        get_log(err)
        return print("Erro ao salvar os dados get_atividade_continuada", err)


def get_atividade_continuada_requisicao(id):
    try:
        url = geral.url + \
            f"tarefa/{id}/dto/json"
        resp = requests.get(url, headers=geral.header)

        if resp.status_code != 200:
            get_log(
                f"Erro ao conectar com a url get_atividade_continuada, código do erro HTTP: {str(resp.status_code)}".upper())
            print(
                f"Erro ao conectar com a url get_atividade_continuada, código do erro HTTP: {str(resp.status_code)}")
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
