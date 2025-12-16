import db
import requests
import geral_env as geral
from log import get_log
import json
from join_function import join_data
from datetime import datetime

tipo_arquivo = 'get_item_processo_analise_tce'

def get_item_processo_analise_tce(ids):
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
                lista_dados.append(get_item_tce_requisicao(id))
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
                # Extração de campos básicos da tarefa
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

                # SOLUÇÃO: Usar get() para evitar KeyError quando campos não existirem
                unidadeexecutora = tarefa['campos'].get('unidadeExecutora', {}).get('valor')
                
                # SOLUÇÃO: Para campos aninhados ['valor']['valor'], usar get() em cadeia
                fatosobapuracao_dict = tarefa['campos'].get('FATOtce', {}).get('valor', {})
                fatosobapuracao = fatosobapuracao_dict.get('valor') if fatosobapuracao_dict else None

                anexgeral = tarefa['campos'].get('anexosGerais', {}).get('valor')
                anexosgerais = []
                if anexgeral:
                    for file in anexgeral:
                        anexosgerais.append(file['nome'])
                    anexosgerais = join_data(anexosgerais)

                processosassociados = tarefa['campos'].get('processosAssociados', {}).get('valor')
                
                # SOLUÇÃO: Para campos aninhados ['valor']['valor']
                tceorigem_dict = tarefa['campos'].get('TCEorigem', {}).get('valor', {})
                tceorigem = tceorigem_dict.get('valor') if tceorigem_dict else None
                
                produtouaig = tarefa['campos'].get('produtoUaig', {}).get('valor')
                numprocessotribunal = tarefa['campos'].get('numproceTrib', {}).get('valor')

                # SOLUÇÃO: Este campo já usava get(), mantido
                localinteracao = tarefa['campos'].get('localidadesinteracao', {}).get('valor', None)
                localidadesinteracao = []
                if localinteracao:
                    for local in localinteracao:
                        localidadesinteracao.append(local['nomeExibicao'])
                    localidadesinteracao = join_data(localidadesinteracao)

                numresolucaoportaria = tarefa['campos'].get('numpor', {}).get('valor')
                
                # SOLUÇÃO: Verificar se o campo existe antes de acessar
                dataenc_valor = tarefa['campos'].get('dataEnc', {}).get('valor')
                dataencaminhado = datetime.strptime(dataenc_valor, '%d/%m/%Y') if dataenc_valor else None                                 
                
                fatoapuracao = tarefa['campos'].get('fatoApuracao', {}).get('valor')
                link = tarefa['campos'].get('links', {}).get('valor')
                links = []
                if link:
                    for lin in link:
                        links.append(lin['descricao'] + '|' + lin['url'])
                    links = join_data(links)

                # SOLUÇÃO: Verificar se o campo existe antes de acessar
                datainstauracao_valor = tarefa['campos'].get('CrgDthInstauracao', {}).get('valor')
                datainstauracao = datetime.strptime(datainstauracao_valor, '%Y-%m-%dT%H:%M:%S') if datainstauracao_valor else None 

                unidenvolvidas = tarefa['campos'].get('unidEnvolvidas', {}).get('valor')
                unidadesenvolvidas = []
                if unidenvolvidas:
                    for envolvidos in unidenvolvidas:
                        unidadesenvolvidas.append(envolvidos['nomeExibicao'])
                    unidadesenvolvidas = join_data(unidadesenvolvidas)

                # SOLUÇÃO: Para campos aninhados ['valor']['valor']
                procedenciatce_dict = tarefa['campos'].get('ProcedenciaTCE', {}).get('valor', {})
                procedenciatce = procedenciatce_dict.get('valor') if procedenciatce_dict else None

                destinatario = tarefa['campos'].get('destinatarioUsuarioUnidade', {}).get('valor')
                destinatariousuariounidade = []
                if destinatario:
                    for destiny in destinatario:
                        destinatariousuariounidade.append(destiny['nomeExibicao'])
                    destinatariousuariounidade = join_data(destinatariousuariounidade)

                executor = tarefa['campos'].get('executores', {}).get('valor')
                executores = []
                if executor:
                    for obs in executor:
                        executores.append(obs['nomeExibicao'])
                    executores = join_data(executores)

                valorprejuizoestimado = tarefa['campos'].get('valorPrejuizoEstimado', {}).get('valor')
                tag = tarefa['campos'].get('tags', {}).get('valor')
                tags = []
                if tag:
                    for tagtag in tag:
                        tags.append(tagtag['descricao'])
                    tags = join_data(tags)

                gerentesub = tarefa['campos'].get('gersubp', {}).get('valor')
                gerentesubprojeto = []
                if gerentesub:
                    for gerente in gerentesub:
                        gerentesubprojeto.append(gerente['nomeExibicao'])
                    gerentesubprojeto = join_data(gerentesubprojeto)

                # SOLUÇÃO: Para campos aninhados ['valor']['valor']
                tipopessoa_dict = tarefa['campos'].get('tpjpf', {}).get('valor', {})
                tipopessoa = tipopessoa_dict.get('valor') if tipopessoa_dict else None

                cp = tarefa['campos'].get('CPF', {}).get('valor')
                cpf = []
                if cp:
                    for c in cp:
                        cpf.append(c['nomeExibicao'])
                    cpf = join_data(cpf)

                cnpj = tarefa['campos'].get('CNPJs', {}).get('valor')
                cnpjs = []
                if cnpj:
                    for file in cnpj:
                        cnpjs.append(file['nomeExibicao'])
                    cnpjs = join_data(cnpjs)

                valoratualizado = tarefa['campos'].get('valoratu', {}).get('valor')
                arquivocomportamento = tarefa['arquivoComportamentoEspecifico']
                estadosituacao = tarefa['estadoSituacao']

                pendencias = tarefa['pendencias']
                listapendencia = []
                if pendencias:
                    for pendencia in pendencias:
                        listapendencia.append(pendencia['nomeUsuarioUnidade'])
                    listapendencia = join_data(listapendencia)

                abasatividade = tarefa['abasAtividade']
                listaabaatividades = []
                if abasatividade:
                    for abas in abasatividade:
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
                    'unidadeexecutora': unidadeexecutora,
                    'fatosobapuracao': fatosobapuracao,
                    'anexosgerais': anexosgerais,
                    'processosassociados': processosassociados,
                    'tceorigem': tceorigem,
                    'produtouaig': produtouaig,
                    'numprocessotribunal': numprocessotribunal,
                    'localidadesinteracao': localidadesinteracao,
                    'numresolucaoportaria': numresolucaoportaria,
                    'dataencaminhado': dataencaminhado,
                    'fatoapuracao': fatoapuracao,
                    'links': links,
                    'datainstauracao': datainstauracao,
                    'unidadesenvolvidas': unidadesenvolvidas,
                    'procedenciatce': procedenciatce,
                    'destinatariousuariounidade': destinatariousuariounidade,
                    'executores': executores,
                    'valorprejuizoestimado': valorprejuizoestimado,
                    'tags': tags,
                    'gerentesubprojeto': gerentesubprojeto,
                    'tipopessoa': tipopessoa,
                    'cpf': cpf,
                    'cnpjs': cnpjs,
                    'valoratualizado': valoratualizado,
                    'arquivocomportamentoespecifico': arquivocomportamento,
                    'estadosituacao': estadosituacao,
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
                 tarefa['unidadeexecutora'],
                 tarefa['fatosobapuracao'],
                 tarefa['anexosgerais'],
                 tarefa['processosassociados'],
                 tarefa['tceorigem'],
                 tarefa['produtouaig'],
                 tarefa['numprocessotribunal'],
                 tarefa['localidadesinteracao'],
                 tarefa['numresolucaoportaria'],
                 tarefa['dataencaminhado'],
                 tarefa['fatoapuracao'],
                 tarefa['links'],
                 tarefa['datainstauracao'],
                 tarefa['unidadesenvolvidas'],
                 tarefa['procedenciatce'],
                 tarefa['destinatariousuariounidade'],
                 tarefa['executores'],
                 tarefa['valorprejuizoestimado'],
                 tarefa['gerentesubprojeto'],
                 tarefa['tipopessoa'],
                 tarefa['cpf'],
                 tarefa['cnpjs'],
                 tarefa['valoratualizado'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO item_analise_tce_auxiliar (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada,
                                                dtprevisaoinicio, dtprevisaofim, dtrealizadainicio, dtrealizadafim,
                                                prioridade, assunto, idatividade, descricaoatividade, idsituacao,
                                                dataultimamodificacao, autorultimamodificacao, unidadeexecutora, fatosobapuracao, anexosgerais,
                                                processosassociados, tceorigem, produtouaig, numprocessotribunal, localidadesinteracao, numresolucaoportaria,
                                                dataencaminhado, fatoapuracao, links, datainstauracao, unidadesenvolvidas, valoratualizado, procedenciatce, destinatariousuariounidade,
                                                executores, valorprejuizoestimado, gerentesubprojeto, tipopessoa, cpf, cnpjs, arquivocomportamentoespecifico, estadosituacao,
                                                tags, pendencias, abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)

def get_item_tce_requisicao(id):
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