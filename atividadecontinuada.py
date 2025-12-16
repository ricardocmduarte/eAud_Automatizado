import db
import requests
import geral_env as geral
from log import get_log
import json
from join_function import join_data
from datetime import datetime

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
                detalhamento = tarefa['campos'].get('Detalhamento', {}).get('valor')
                localidades = tarefa['campos'].get('localidadesPlanoTrabalho', {}).get('valor')
                localtrabalho = []
                if localidades:
                    for local in localidades:
                        localtrabalho.append(local['nomeExibicao'])
                    localtrabalho = join_data(localtrabalho)

                proponenteplanotrabalho = tarefa['campos'].get('proponentePlanoTrabalho', {}).get('valor')
                etapaplanotrabalho = tarefa['campos'].get('etapaPlanoTrabalho', {}).get('valor')
                responsavelplanotrabalho = tarefa['campos'].get('responsavelPlanoTrabalho', {}).get('valor')
                links = tarefa['campos'].get('links', {}).get('valor')
                linktarefa = []
                if links:
                    for link in links:
                        linktarefa.append(
                            link['descricao'] + ' | ' + link['url'])
                    linktarefa = join_data(linktarefa)

                anexosplanotrabalho = tarefa['campos'].get('anexosPlanoTrabalho', {}).get('valor')
                anexos = []
                if anexosplanotrabalho:
                    for anexo in anexosplanotrabalho:
                        anexos.append(anexo['nomeExibicao'])
                    anexos = join_data(anexos)

                processoplanotrabalho = tarefa['campos'].get('processoTrabalhoPlanoTrabalho', {}).get('valor')
                resultadoesperado = tarefa['campos'].get('resultadosEsperadosPlanoTrabalho', {}).get('valor')
                resultados = []
                if resultadoesperado:
                    for resul in resultadoesperado:
                        resultados.append(resul['nomeExibicao'])
                    resultados = join_data(resultados)

                tarefasprecedentes = tarefa['campos'].get('tarefasPrecedentes', {}).get('valor')
                recursofinanceiro = tarefa['campos'].get('recursoFinanceiroPlanoTrabalho', {}).get('valor')
                envolvidosplanotrabalho = tarefa['campos'].get('envolvidosPlanoTrabalho', {}).get('valor')
                envolvidos = []
                if envolvidosplanotrabalho:
                    for envolv in envolvidosplanotrabalho:
                        envolvidos.append(envolv['nomeExibicao'])
                    envolvidos = join_data(envolvidos)

                homemhora = tarefa['campos'].get('homemHorasPlanoTrabalho', {}).get('valor')
                gerentes = tarefa['campos'].get('gerentesPlanoTrabalho', {}).get('valor')
                gerente = []
                if gerentes:
                    for gere in gerentes:
                        gerente.append(gere['nomeExibicao'])
                    gerente = join_data(gerente)

                supervisoresplano = tarefa['campos'].get('supervisoresPlanoTrabalho', {}).get('valor')
                supervisorplano = []
                if supervisoresplano:
                    for supervi in supervisoresplano:
                        supervisorplano.append(supervi['nomeExibicao'])
                    supervisorplano = join_data(supervisorplano)

                planotipo = tarefa['campos'].get('tipoPlanoTrabalho', {}).get('valor')
                tipoplano = planotipo['valor'] if planotipo else ''

                estadosituacao = tarefa['estadoSituacao']
                arquivocomportamento = tarefa['arquivoComportamentoEspecifico']
                descricaotag = tarefa['campos'].get('tags', {}).get('valor')
                tags = []
                if descricaotag:
                    for tagdesc in descricaotag:
                        tags.append(tagdesc['descricao'])
                    tags = join_data(tags)

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
                    'detalhamento': detalhamento,
                    'proponenteplanotrabalho': proponenteplanotrabalho,
                    'etapaplanotrabalho': etapaplanotrabalho,
                    'responsavelplanotrabalho': responsavelplanotrabalho,
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
                 tarefa['detalhamento'],
                 tarefa['proponenteplanotrabalho'],
                 tarefa['etapaplanotrabalho'],
                 tarefa['responsavelplanotrabalho'],
                 tarefa['processoplanotrabalho'],
                 tarefa['localidade'],
                 tarefa['links'],
                 tarefa['tarefasprecedentes'],
                 tarefa['resultados'],
                 tarefa['recurso'],
                 tarefa['envolvidos'],
                 tarefa['homemhora'],
                 tarefa['gerentes'],
                 tarefa['supervisorplanotrabalho'],
                 tarefa['tipoplano'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade'],
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO atividade_continuada_auxiliar (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,detalhamento,proponenteplanotrabalho,etapaplanotrabalho,
                                                responsavelplanotrabalho,processoplanotrabalho,
                                                localidade,links,tarefasprecedentes,resultados,recurso,envolvidos,homemhora,gerentes,supervisorplanotrabalho,
                                                tipoplano,arquivocomportamentoespecifico,estadosituacao, tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)

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