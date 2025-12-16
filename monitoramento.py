import db
import requests
import geral_env as geral
from log import get_log
import json
from join_function import join_data
from datetime import datetime

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
        if ids:
            for i, id in enumerate(ids):
                lista_dados.append(get_monitoramento_requisicao(id))
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
                detalhesmonitoramento = tarefa['campos'].get('detalhesMonitoramento', {}).get('valor')
                
                prov = tarefa['campos'].get('providencia', {}).get('valor')
                providencia = ''
                if prov and isinstance(prov, dict):
                    providencia = prov.get('valor', '')

                unidadeauditoria = tarefa['campos'].get('unidadesAuditoria', {}).get('valor')
                unidadesauditoria = []
                if unidadeauditoria:
                    for aud in unidadeauditoria:
                        unidadesauditoria.append(aud.get('nomeExibicao', ''))
                    unidadesauditoria = join_data(unidadesauditoria)

                unidadeenvolvida = tarefa['campos'].get('unidEnvolvidas', {}).get('valor')
                unidadesenvolvidas = []
                if unidadeenvolvida:
                    for envol in unidadeenvolvida:
                        unidadesenvolvidas.append(envol.get('nomeExibicao', ''))
                    unidadesenvolvidas = join_data(unidadesenvolvidas)

                categoriamonitoramento = tarefa['campos'].get('categoriasMonitoramento', {}).get('valor')
                categoriasmonitoramento = []
                if categoriamonitoramento:
                    for cat in categoriamonitoramento:
                        categoriasmonitoramento.append(cat.get('nomeExibicao', ''))
                    categoriasmonitoramento = join_data(categoriasmonitoramento)

                tarefasprec = tarefa['campos'].get('tarefasPrecedentes', {}).get('valor')
                tarefasprecedentes = []
                if tarefasprec:
                    for tarefapre in tarefasprec:
                        tarefasprecedentes.append(tarefapre.get('nomeExibicao', ''))
                    tarefasprecedentes = join_data(tarefasprecedentes)

                valorprejuizoestimado = tarefa['campos'].get('valorPrejuizoEstimado', {}).get('valor')

                observador = tarefa['campos'].get('observadores', {}).get('valor')
                observadores = []
                if observador:
                    for obs in observador:
                        observadores.append(obs.get('nomeExibicao', ''))
                    observadores = join_data(observadores)

                descricaotag = tarefa['campos'].get('tags', {}).get('valor')
                tags = []
                if descricaotag:
                    for tagdesc in descricaotag:
                        tags.append(tagdesc.get('descricao', ''))
                    tags = join_data(tags)

                # SOLUÇÃO: Tratamento seguro para acesso encadeado com get()
                unidade_gestora_data = tarefa['campos'].get('unidadeGestora', {}).get('valor')
                unidadegestora = ''
                if unidade_gestora_data and isinstance(unidade_gestora_data, dict):
                    unidadegestora = unidade_gestora_data.get('nomeExibicao', '')

                fundamento = tarefa['campos'].get('fundamentos', {}).get('valor')
                fundamentos = []
                if fundamento:
                    for fund in fundamento:
                        fundamentos.append(fund.get('descricao', ''))
                    fundamentos = join_data(fundamentos)

                ultimoposicionamento = tarefa['campos'].get('tipoUltimoPosicionamento', {}).get('valor')
                tipoultimoposicionamento = []
                if ultimoposicionamento:
                    for pos in ultimoposicionamento:
                        tipoultimoposicionamento.append(pos.get('valor', ''))
                    tipoultimoposicionamento = join_data(tipoultimoposicionamento)

                textoultimoposicionamento = tarefa['campos'].get('textoUltimoPosicionamento', {}).get('valor')
                textoultimopamanifestacao = tarefa['campos'].get('textoUltimaManifestacao', {}).get('valor')

                anexorel = tarefa['campos'].get('anexosRelatorio', {}).get('valor')
                anexosrelatorio = []
                if anexorel:
                    for file in anexorel:
                        anexosrelatorio.append(file.get('nome', ''))
                    anexosrelatorio = join_data(anexosrelatorio)

                estadosituacao = tarefa.get('estadoSituacao')
                arquivocomportamento = tarefa.get('arquivoComportamentoEspecifico')

                pendencias = tarefa.get('pendencias', [])
                listapendencia = []
                if pendencias:
                    for pendencia in pendencias:
                        listapendencia.append(pendencia.get('nomeUsuarioUnidade', ''))
                    listapendencia = join_data(listapendencia)

                abasatividade = tarefa.get('abasAtividade', [])
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
            insert_query = (f"""INSERT INTO monitoramento_auxiliar (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada,
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