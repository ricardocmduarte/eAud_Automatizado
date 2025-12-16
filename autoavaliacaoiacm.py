import db
import requests
import geral_env as geral
from log import get_log
import json
from join_function import join_data
from datetime import datetime

tipo_arquivo = 'get_autoavaliacao_iacm'

def get_autoavaliacao_iacm(ids):
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
                lista_dados.append(get_iacm_requisicao(id))
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
                # Extração dos campos básicos da tarefa
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

                # SOLUÇÃO: Usar get() para evitar KeyError em campos opcionais
                filegeral = tarefa['campos'].get('anexosGerais', {}).get('valor')
                anexosgerais = []
                if filegeral:
                    for file in filegeral:
                        anexosgerais.append(file['nome'])
                    anexosgerais = join_data(anexosgerais)

                teamexterno = tarefa['campos'].get('equipeValidacaoExternaIACM', {}).get('valor')
                equipevalidacaoexterna = []
                if teamexterno:
                    for team in teamexterno:
                        equipevalidacaoexterna.append(team['nomeExibicao'])
                    equipevalidacaoexterna = join_data(equipevalidacaoexterna)

                unidval = tarefa['campos'].get('unidadesValidadorasIACM', {}).get('valor')
                unidadevalidadoras = []
                if unidval:
                    for uni in unidval:
                        unidadevalidadoras.append(uni['nomeExibicao'])
                    unidadevalidadoras = join_data(unidadevalidadoras)

                relatoriovalidacao = tarefa['campos'].get('relvalex', {}).get('valor')

                equipeavaliacao = tarefa['campos'].get('equipeAvaliacaoIACM', {}).get('valor')
                equipeiacm = []
                if equipeavaliacao:
                    for equipe in equipeavaliacao:
                        equipeiacm.append(equipe['nomeExibicao'])
                    equipeiacm = join_data(equipeiacm)

                unidadeauditoriasuptec = tarefa['campos'].get('unidadeAuditoriaSupTec', {}).get('valor')
                tarefaprecedentes = tarefa['campos'].get('tarefasPrecedentes', {}).get('valor')

                nivel = tarefa['campos'].get('nivelIACM', {}).get('valor')
                valorniveliacm = 0
                if nivel:
                    for level in nivel:
                        valorniveliacm = level['valor']

                textohistorico = tarefa['campos'].get('textoDoHistorico', {}).get('valor')

                iacmplanoacao = tarefa['campos'].get('iacmPlanoDeAcao', {}).get('valor')
                
                # SOLUÇÃO: Verificar campos aninhados antes de acessar
                unidadesup_valor = tarefa['campos'].get('unidadeSup', {}).get('valor')
                nomeexibicaosup = unidadesup_valor['nomeExibicao'] if unidadesup_valor else None
                
                mesconclusaoprevisto = tarefa['mesConclusaoPrevisto']
                textoajuda = tarefa['textoAjudaSituacao']
                estadosituacao = tarefa['estadoSituacao']
                arquivocomportamento = tarefa['arquivoComportamentoEspecifico']

                # SOLUÇÃO: Corrigir variável - estava usando descricaotag no loop
                descricaotag_valor = tarefa['campos'].get('tags', {}).get('valor')
                tags = []
                if descricaotag_valor:
                    for tagdesc in descricaotag_valor:
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
                    'anexosgerais': anexosgerais,
                    'equipevalidacaoexterna': equipevalidacaoexterna,
                    'unidadevalidadoras': unidadevalidadoras,
                    'relatoriovalidacao': relatoriovalidacao,
                    'equipeiacm': equipeiacm,
                    'unidadeauditoriasuptec': unidadeauditoriasuptec,
                    'tarefaprecedentes': tarefaprecedentes,
                    'niveliacm': valorniveliacm,
                    'textohistorico': textohistorico,
                    'iacmplanoacao': iacmplanoacao,
                    'unidadesuperior': nomeexibicaosup,
                    'mesconclusaoprevisto': mesconclusaoprevisto,
                    'textoajuda': textoajuda,
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
                 tarefa['anexosgerais'],
                 tarefa['equipevalidacaoexterna'],
                 tarefa['unidadevalidadoras'],
                 tarefa['relatoriovalidacao'],
                 tarefa['equipeiacm'],
                 tarefa['unidadeauditoriasuptec'],
                 tarefa['tarefaprecedentes'],
                 tarefa['niveliacm'],
                 tarefa['textohistorico'],
                 tarefa['iacmplanoacao'],
                 tarefa['unidadesuperior'],
                 tarefa['mesconclusaoprevisto'],
                 tarefa['textoajuda'],
                 tarefa['estadosituacao'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO auto_avaliacao_iacm_auxiliar (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,anexosgerais,equipevalidacaoexterna,unidadevalidadoras,
                                                relatoriovalidacao,equipeiacm,unidadeauditoriasuptec,tarefaprecedentes,estadosituacao,
                                                niveliacm,textohistorico,iacmplanoacao,unidadesuperior,mesconclusaoprevisto,arquivocomportamentoespecifico,
                                                textoajuda,tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)

def get_iacm_requisicao(id):
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