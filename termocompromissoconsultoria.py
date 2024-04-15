import db
import requests
import geral
from log import get_log
import json
from join_function import join_data
from datetime import datetime

tipo_arquivo = 'get_termo_compromisso_consultoria'


def get_termo_compromisso_consultoria(ids):
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
                lista_dados.append(get_termo_compromisso_consultoria_requisicao(id))

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
                dtprevisaoinicio = datetime.strptime(tarefa['dtPrevisaoInicio'], '%d/%m/%Y') if tarefa['dtPrevisaoInicio'] else None
                dtprevisaofim = datetime.strptime(tarefa['dtPrevisaoFim'], '%d/%m/%Y') if tarefa['dtPrevisaoFim'] else None
                dtrealizadainicio = datetime.strptime(tarefa['dtRealizadaInicio'], '%d/%m/%Y') if tarefa['dtRealizadaInicio'] else None
                dtrealizadafim = datetime.strptime(tarefa['dtRealizadaFim'], '%d/%m/%Y') if tarefa['dtRealizadaFim'] else None
                prioridade = tarefa['prioridade']
                assunto = tarefa['assunto']
                idatividade = tarefa['idAtividade']
                descricaoatividade = tarefa['descricaoAtividade']
                idsituacao = tarefa['idSituacao']
                dataultimamodificacao = datetime.strptime(tarefa['dataUltimaModificacao'], '%d/%m/%Y %H:%M:%S') if tarefa['dataUltimaModificacao'] else None
                autorultimamodificacao = tarefa['autorUltimaModificacao']

                unidenvolvidas = tarefa['campos']['unidEnvolvidas']['valor']
                unidadesenvolvidas = []
                if unidenvolvidas:
                    for i, envolvidos in enumerate(unidenvolvidas):
                        unidadesenvolvidas.append(envolvidos['nomeExibicao'])

                    unidadesenvolvidas = join_data(unidadesenvolvidas)

                anexgeral = tarefa['campos']['anexosGerais']['valor']
                anexosgerais = []
                if anexgeral:
                    for i, file in enumerate(anexgeral):
                        anexosgerais.append(file['nome'])

                    anexosgerais = join_data(anexosgerais)

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

                docsolicitado = tarefa['campos']['docSolicitacao']['valor']
                docsolicitacao = ''
                if docsolicitado:
                    docsolicitacao = docsolicitado['nome']

                tag = tarefa['campos']['tags']['valor']
                tags = []
                if tag:
                    for i, tagtag in enumerate(tag):
                        tags.append(tagtag['descricao'])

                    tags = join_data(tags)

                coordequipe = tarefa['campos']['CoordenadorEquipe']['valor']
                coordenadorequipe = []
                if coordequipe:
                    for i, coord in enumerate(coordequipe):
                        coordenadorequipe.append(coord['nomeExibicao'])

                    coordenadorequipe = join_data(coordenadorequipe)

                equipe = tarefa['campos']['EquipeGeral']['valor']
                equipegeral = []
                if equipe:
                    for i, team in enumerate(equipe):
                        equipegeral.append(team['nomeExibicao'])

                    equipegeral = join_data(equipegeral)

                supervisor = tarefa['campos']['supervisores']['valor']
                supervisores = []
                if supervisor:
                    for i, super in enumerate(supervisor):
                        supervisores.append(super['nomeExibicao'])

                    supervisores = join_data(supervisores)

                tempocompro = tarefa['campos']['termoCompromisso']['valor']
                termocompromisso = ''
                if tempocompro:
                    termocompromisso = tempocompro['nome']

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
                    'unidadesenvolvidas': unidadesenvolvidas,
                    'anexosgerais': anexosgerais,
                    'observadores': observadores,
                    'hipoteselegal': hipoteselegal,
                    'docsolicitacao': docsolicitacao,
                    'coordenadorequipe': coordenadorequipe,
                    'equipegeral': equipegeral,
                    'supervisores': supervisores,
                    'termocompromisso': termocompromisso,
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
                 tarefa['observadores'],
                 tarefa['hipoteselegal'],
                 tarefa['docsolicitacao'],
                 tarefa['coordenadorequipe'],
                 tarefa['equipegeral'],
                 tarefa['supervisores'],
                 tarefa['termocompromisso'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO termo_compromisso_consultoria_teste (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada,
                                                dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim, prioridade, assunto, idatividade, descricaoatividade, 
                                                idsituacao, dataultimamodificacao, autorultimamodificacao, unidadesenvolvidas, anexosgerais, observadores, hipoteselegal, 
                                                docsolicitacao, coordenadorequipe, equipegeral, supervisores, termocompromisso, arquivocomportamentoespecifico, 
                                                estadosituacao, tags, pendencias, abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_termo_compromisso_consultoria_requisicao(id):
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
