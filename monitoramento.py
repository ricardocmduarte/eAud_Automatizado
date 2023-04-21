import db
import requests
import geral
from log import get_log
import json
from join_function import join_data


tipo_arquivo = 'get_monitoramento'


def get_monitoramento(ids):
    response = geral.check_url_health('tarefa')
    get_log(f"Iniciado {tipo_arquivo}")

    if response != 200:
        get_log(
            f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP:  {str(response)}".upper())
        return print(f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP:  {str(response)}")

    lista_dados = []
    lista_final = []
    try:
        if id:
            for i, id in enumerate(ids):
                lista_dados.append(get_monitoramento_requisicao(id))
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

            detalhesmonitoramento = tarefa['campos']['detalhesMonitoramento']['valor']

            providencia = tarefa['campos']['providencia']['valor']['valor']

            unidadeauditoria = tarefa['campos']['unidadesAuditoria']['valor']
            unidadesauditoria = []
            if unidadeauditoria:
                for i, aud in enumerate(unidadeauditoria):
                    unidadesauditoria.append(aud['nomeExibicao'])

                unidadesauditoria = join_data(unidadesauditoria)

            unidadeenvolvida = tarefa['campos']['unidEnvolvidas']['valor']
            unidadesenvolvidas = []
            if unidadeenvolvida:
                for i, envol in enumerate(unidadeenvolvida):
                    unidadesenvolvidas.append(envol['nomeExibicao'])

                unidadesenvolvidas = join_data(unidadesenvolvidas)

            categoriamonitoramento = tarefa['campos']['categoriasMonitoramento']['valor']
            categoriasmonitoramento = []
            if categoriamonitoramento:
                for i, cat in enumerate(categoriamonitoramento):
                    categoriasmonitoramento.append(cat['nomeExibicao'])

                categoriasmonitoramento = join_data(categoriasmonitoramento)

            tarefasprec = tarefa['campos']['tarefasPrecedentes']['valor']
            tarefasprecedentes = []
            if tarefasprec:
                for i, tarefapre in enumerate(tarefasprec):
                    tarefasprecedentes.append(tarefapre['nomeExibicao'])
                tarefasprecedentes = join_data(tarefasprecedentes)

            valorprejuizoestimado = tarefa['campos']['valorPrejuizoEstimado']['valor']

            observador = tarefa['campos']['observadores']['valor']
            observadores = []
            if observador:
                for i, obs in enumerate(observador):
                    observadores.append(obs['nomeExibicao'])

                observadores = join_data(observadores)

            descricaotag = tarefa['campos']['tags']['valor']
            tags = []
            if descricaotag:
                for i, tagdesc in enumerate(descricaotag):
                    tags.append(tagdesc['descricao'])

                tags = join_data(tags)

            unidadegestora = tarefa['campos']['unidadeGestora']['valor']['nomeExibicao']

            fundamento = tarefa['campos']['fundamentos']['valor']
            fundamentos = []
            if fundamento:
                for i, fund in enumerate(fundamento):
                    fundamentos.append(fund['descricao'] +
                                       ' | ' + fund['anexo']['nome'])

                fundamentos = join_data(fundamentos)

            ultimoposicionamento = tarefa['campos']['tipoUltimoPosicionamento']['valor']
            tipoultimoposicionamento = []
            if ultimoposicionamento:
                for i, pos in enumerate(ultimoposicionamento):
                    tipoultimoposicionamento.append(pos['valor'])

                tipoultimoposicionamento = join_data(tipoultimoposicionamento)

            textoultimoposicionamento = tarefa['campos']['textoUltimoPosicionamento']['valor']
            textoultimopamanifestacao = tarefa['campos']['textoUltimaManifestacao']['valor']

            anexorel = tarefa['campos']['anexosRelatorio']['valor']
            anexosrelatorio = []
            if anexorel:
                for i, file in enumerate(anexorel):
                    anexosrelatorio.append(file['nome'])

                anexosrelatorio = join_data(anexosrelatorio)

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
                'detalhesmonitoramento': detalhesmonitoramento,
                'providencia': providencia,
                'unidadesauditoria': unidadesauditoria,
                'unidadesenvolvidas': unidadesenvolvidas,
                'categoriasmonitoramento': categoriasmonitoramento,
                'tarefasprecedentes': tarefasprecedentes,
                'valorprejuizoestimado': valorprejuizoestimado,
                'observadores': observadores,
                'unidadegestora': unidadegestora,
                'fundamentos': fundamentos,
                'ultimoposicionamento': tipoultimoposicionamento,
                'textoultimoposicionamento': textoultimoposicionamento,
                'textoultimamanifestacao': textoultimopamanifestacao,
                'anexorelatorio': anexosrelatorio,
                'estadosituacao': estadosituacao,
                'arquivocomportamentoespecifico': arquivocomportamento,
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
                 tarefa['detalhesmonitoramento'],
                 tarefa['providencia'],
                 tarefa['unidadesauditoria'],
                 tarefa['unidadesenvolvidas'],
                 tarefa['categoriasmonitoramento'],
                 tarefa['tarefasprecedentes'],
                 tarefa['valorprejuizoestimado'],
                 tarefa['observadores'],
                 tarefa['unidadegestora'],
                 tarefa['fundamentos'],
                 tarefa['ultimoposicionamento'],
                 tarefa['textoultimoposicionamento'],
                 tarefa['textoultimamanifestacao'],
                 tarefa['anexorelatorio'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO monitoramento (id, situacao, estado, atividade, titulo, titulotarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,detalhesmonitoramento,providencia,unidadesauditoria, 
                                                unidadesenvolvidas, categoriasmonitoramento,tarefasprecedentes,valorprejuizoestimado, observadores,
                                                unidadegestora, fundamentos,ultimoposicionamento,textoultimoposicionamento,textoultimamanifestacao,
                                                anexorelatorio,arquivocomportamentoespecifico, estadosituacao,
                                                tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_monitoramento_requisicao(id):
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
