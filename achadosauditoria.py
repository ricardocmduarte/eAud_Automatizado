import db
import requests
import geral
from log import get_log
import json


def get_achados(ids_achados):
    lista_dados = []
    lista_final = []
    try:
        if ids_achados:
            for i, id in enumerate(ids_achados):
                lista_dados.append(get_achados_requisicao(id))
                print(f"Iteração get_achados {str(i)} registrada com sucesso")

        # lista final passa por um tratamento de dados
        lista_final = tratamento_dados(lista_dados)

        # comando para salvar os dados tratados
        salvar_dados(lista_final)
        get_log("Lista de achados ok")
        return print("Lista de achados ok")
    except NameError as err:
        get_log("Erro ao salvar os dados get_achados".upper())
        get_log(err)
        return print("Erro ao salvar os dados get_achados", err)


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
            equipevalidacaoexterna = tarefa['campos']['equipeValidacaoExternaIACM']['valor']
            unidadevalidadoras = tarefa['campos']['unidadesValidadorasIACM']['valor']
            relatoriovalidacao = tarefa['campos']['relvalex']['valor']

            equipeavaliacao = tarefa['campos']['equipeAvaliacaoIACM']['valor']
            equipeiacm = []
            for i, equipe in enumerate(equipeavaliacao):
                equipeiacm.append(equipe['nomeExibicao'])

            unidadeauditoriasuptec = tarefa['campos']['unidadeAuditoriaSupTec']['valor']
            tarefaprecedentes = tarefa['campos']['tarefasPrecedentes']['valor']

            niveliacm = tarefa['campos']['nivelIACM']['valor']
            valorniveliacm = []
            for i, valor in enumerate(niveliacm):
                valorniveliacm.append(valor['valor'])

            textohistorico = tarefa['campos']['textoDoHistorico']['valor']

            tags = tarefa['campos']['tags']['valor']
            descricaotag = []
            for i, tagdesc in enumerate(tags):
                descricaotag.append(tagdesc['descricao'])

            iacmplanoacao = tarefa['campos']['iacmPlanoDeAcao']['valor']
            unidadesup = tarefa['campos']['unidadeSup']['valor']
            nomesup = unidadesup['nome']
            nomeexibicaosup = unidadesup['nomeExibicao']
            mesconclusaoprevisto = tarefa['mesConclusaoPrevisto']
            textoajuda = tarefa['textoAjudaSituacao']

            pendencias = tarefa['pendencias']
            listapendencia = []
            for i, pendencia in enumerate(pendencias):
                listapendencia.append(pendencia['nomeUsuarioUnidade'])

            abasatividade = tarefa['abasAtividade']
            listaabaatividades = []
            for i, abas in enumerate(abasatividade):
                listaabaatividades.append(abas['descricao'])

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
                'equipevalidacaoexterna': equipevalidacaoexterna,
                'unidadevalidadoras': unidadevalidadoras,
                'relatoriovalidacao': relatoriovalidacao,
                'equipeiacm': equipeiacm,
                'unidadeauditoriasuptec': unidadeauditoriasuptec,
                'tarefaprecedentes': tarefaprecedentes,
                'niveliacm': valorniveliacm,
                'textohistorico': textohistorico,
                'tags': descricaotag,
                'iacmplanoacao': iacmplanoacao,
                'unidadesuperior': nomeexibicaosup,
                'mesconclusaoprevisto': mesconclusaoprevisto,
                'textoajuda': textoajuda,
                'pendencias': listapendencia,
                'abasatividade': listaabaatividades,
            })
        get_log("Lista achados_auditoria tratada com sucesso")
        return lista_final
    except NameError as err:
        get_log("Erro ao tratar os dados get_achados".upper())
        get_log(err)
        return print("Erro ao tratar os dados get_achados", err)


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
                 tarefa['idtarefaassociada'],
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
                 tarefa['equipevalidacaoexterna'],
                 tarefa['unidadevalidadoras'],
                 tarefa['relatoriovalidacao'],
                 tarefa['equipeiacm'],
                 tarefa['unidadeauditoriasuptec'],
                 tarefa['tarefaprecedentes'],
                 tarefa['niveliacm'],
                 tarefa['textohistorico'],
                 tarefa['tags'],
                 tarefa['iacmplanoacao'],
                 tarefa['unidadesuperior'],
                 tarefa['mesconclusaoprevisto'],
                 tarefa['textoajuda'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO achados_auditoria (id, situacao, estado, atividade, titulo,
                                                tituloTarefaAssociada,dtPrevisaoInicio,dtPrevisaoFim,dtRealizadaInicio,dtRealizadaFim,
                                                prioridade,colunaCalculada,assunto,idAtividade,descricaoAtividade,
                                                dataUltimaModificacao,autorUltimaModificacao,campos,quantidade,qtdTotalInteracoes,
                                                arquivoComportamentoEspecifico,tarefaAssociada,papelPendencia,
                                                mesConclusaoPrevisto,mesConclusaoRealizado,idAnalisePreliminar,nomePessoaPendencia,
                                                siglaUnidadePendencia,nomeEquipePendencia,valorParaFiltragemDeFatiaDeGrafico,
                                                estadoSituacao,textoAjudaSituacao,acompanhamento,sistema,usuarioPodeGerenciarAtividade,
                                                mesAnoUltimaModificacao, dataatualizacao) VALUES {array_records}""")

            cur.execute(insert_query, lista)
            get_log("Auditorias salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log("Erro ao salvar os dados get_tarefas".upper())
        get_log(err)
        return print("Erro ao salvar os dados get_tarefas", err)


def get_achados_requisicao(id):
    try:
        url = geral.url + \
            f"tarefa/{id}/dto/json"
        resp = requests.get(url, headers=geral.header)

        if resp.status_code != 200:
            get_log(
                f"Erro ao conectar com a url get_tarefas, código do erro HTTP: {str(resp.status_code)}".upper())
            return print(f"Erro ao conectar com a url get_tarefas, código do erro HTTP: {str(resp.status_code)}")

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
