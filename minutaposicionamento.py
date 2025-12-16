import db
import requests
import geral_env as geral
from log import get_log
import json
from join_function import join_data
from datetime import datetime

tipo_arquivo = 'get_minuta_posicionamento'


def get_minuta_posicionamento(ids):
    response = geral.check_url_health('tarefa')
    get_log(f"Iniciado {tipo_arquivo}")

    if response != 200:
        get_log(
            f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP:  {str(response)}".upper())
        return print(f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP:  {str(response)}")

    lista_dados = []
    lista_final = []
    try:
        if ids:
            for i, id in enumerate(ids):
                lista_dados.append(get_minuta_requisicao(id))

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

                # SOLUÇÃO: Usar get() para evitar KeyError quando campos não existirem
                provminuta = tarefa['campos'].get('providenciaMinuta', {}).get('valor')
                providenciaminuta = ''
                if provminuta:
                    providenciaminuta = provminuta.get('valor', '')

                anexosgeral = tarefa['campos'].get('anexosGerais', {}).get('valor')
                anexosgerais = []
                if anexosgeral:
                    for file in anexosgeral:
                        anexosgerais.append(file.get('nomeExibicao', ''))
                    anexosgerais = join_data(anexosgerais)

                destiny = tarefa['campos'].get('destinatarioUsuarioUnidade', {}).get('valor')
                destinatariousuariounidade = ''
                if destiny:
                    destinatariousuariounidade = destiny.get('nomeExibicao', '')

                tarefasprec = tarefa['campos'].get('tarefasPrecedentes', {}).get('valor')
                tarefasprecedentes = []
                if tarefasprec:
                    for tarefapre in tarefasprec:
                        tarefasprecedentes.append(tarefapre.get('nomeExibicao', ''))
                    tarefasprecedentes = join_data(tarefasprecedentes)

                textodohistorico = tarefa['campos'].get('textoDoHistorico', {}).get('valor')
                acaoposicionamento = tarefa['campos'].get('acaoPosicionamento', {}).get('valor')
                
                # SOLUÇÃO: Acesso seguro a refMonitoramento com get() aninhado
                refmonitoramento_val = tarefa['campos'].get('refMonitoramento', {}).get('valor')
                refmonitoramento = refmonitoramento_val.get('nomeExibicao') if refmonitoramento_val else None

                unidadeauditoria = tarefa['campos'].get('unidadesAuditoriaMinuta', {}).get('valor')
                unidadesauditoriaminuta = []
                if unidadeauditoria:
                    for minuta in unidadeauditoria:
                        unidadesauditoriaminuta.append(minuta.get('nomeExibicao', ''))
                    unidadesauditoriaminuta = join_data(unidadesauditoriaminuta)

                tipoposicionamento = tarefa['campos'].get('tipoPosicionamentoMinuta', {}).get('valor')
                tipoposicionamentominuta = []
                if tipoposicionamento:
                    for tipo in tipoposicionamento:
                        tipoposicionamentominuta.append(tipo.get('valor', ''))
                    tipoposicionamentominuta = join_data(tipoposicionamentominuta)

                # SOLUÇÃO: Acesso seguro a unidadeMonitorada com get() aninhado
                unidademonitorada_val = tarefa['campos'].get('unidadeMonitorada', {}).get('valor')
                unidademonitorada = unidademonitorada_val.get('nomeExibicao') if unidademonitorada_val else None

                recomendacaominuta = tarefa['campos'].get('RecMinutas', {}).get('valor')
                detalhamentomonitoramento = tarefa['campos'].get('detalhesMonitoramentoMinuta', {}).get('valor')

                estadosituacao = tarefa.get('estadoSituacao')
                arquivocomportamento = tarefa.get('arquivoComportamentoEspecifico')

                descricaotag = tarefa['campos'].get('tags', {}).get('valor')
                tags = []
                if descricaotag:
                    for tagdesc in descricaotag:
                        tags.append(tagdesc.get('descricao', ''))
                    tags = join_data(tags)

                pendencias = tarefa.get('pendencias')
                listapendencia = []
                if pendencias:
                    for pendencia in pendencias:
                        listapendencia.append(pendencia.get('nomeUsuarioUnidade', ''))
                    listapendencia = join_data(listapendencia)

                abasatividade = tarefa.get('abasAtividade')
                listaabaatividades = []
                if abasatividade:
                    for abas in abasatividade:
                        listaabaatividades.append(abas.get('descricao', ''))
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
                    'providenciaminuta': providenciaminuta,
                    'anexosgerais': anexosgerais,
                    'destinatariousuariounidade': destinatariousuariounidade,
                    'tarefasprecedentes': tarefasprecedentes,  # Corrigido: estava tarefasprec
                    'textohistorico': textodohistorico,
                    'acaoposicionamento': acaoposicionamento,
                    'referenciarecomendacao': refmonitoramento,
                    'unidadesauditorias': unidadesauditoriaminuta,
                    'tipoposicionamento': tipoposicionamentominuta,
                    'unidademonitorada': unidademonitorada,
                    'recomendacaominuta': recomendacaominuta,
                    'detalhamentomonitoramento': detalhamentomonitoramento,
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
                 tarefa['providenciaminuta'],
                 tarefa['anexosgerais'],
                 tarefa['destinatariousuariounidade'],
                 tarefa['tarefasprecedentes'],
                 tarefa['textohistorico'],
                 tarefa['acaoposicionamento'],
                 tarefa['referenciarecomendacao'],  # Adicionado campo faltante
                 tarefa['unidadesauditorias'],
                 tarefa['tipoposicionamento'],
                 tarefa['unidademonitorada'],  # Adicionado campo faltante
                 tarefa['recomendacaominuta'],
                 tarefa['detalhamentomonitoramento'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO minuta_posicionamento_auxiliar (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,providenciaminuta,anexosgerais,destinatariousuariounidade, 
                                                tarefasprecedentes, textohistorico,acaoposicionamento,referenciarecomendacao,unidadesauditorias, tipoposicionamento,
                                                unidademonitorada,recomendacaominuta, detalhamentomonitoramento,arquivocomportamentoespecifico, estadosituacao,
                                                tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_minuta_requisicao(id):
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