import db
import requests
import geral_env as geral
from log import get_log
import json
from join_function import join_data
from datetime import datetime

tipo_arquivo = 'get_analise_auditoria'

def get_analise_auditoria(ids):
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
                lista_dados.append(get_analise_auditoria_requisicao(id))

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
                unidadesenvolvidas = tarefa['campos'].get('unidEnvolvidas', {}).get('valor')
                nomeunidadesenvolvidas = []
                if unidadesenvolvidas:
                    for envolvidasunidades in unidadesenvolvidas:
                        nomeunidadesenvolvidas.append(
                            envolvidasunidades['nome'])
                    nomeunidadesenvolvidas = join_data(nomeunidadesenvolvidas)
                else:
                    nomeunidadesenvolvidas = ''
                
                itemanaliseauditoria = tarefa['campos'].get('itensDaAnaliseAuditoria', {}).get('valor', [])
                
                # Inicialização de listas para acumular dados dos itens
                idanaliseauditoria = []
                descteste = []
                desccriterio = []
                descinformacao = []
                descfonte = []
                desclimitacao = []
                descachado = []
                observacoes = []
                descricaoescopo = []
                valortotalescopo = []
                valorauditadoescopo = []
                anexoescopo = []
                responsavelitem = []
                anexoevidencia = []
                autoranexoevidencia = []
                
                for itens in itemanaliseauditoria:
                    idanaliseauditoria.append(itens['idAnaliseAuditoria'])
                    # SOLUÇÃO: Usar get() para acessar campos dentro do teste
                    teste = itens.get('teste', {})
                    descteste.append(teste.get('descTeste', ''))
                    desccriterio.append(teste.get('descCriterio', ''))
                    descinformacao.append(teste.get('descInformacao', ''))
                    descfonte.append(teste.get('descFonte', ''))
                    desclimitacao.append(teste.get('descLimitacao', ''))
                    descachado.append(teste.get('descAchado', ''))
                    observacoes.append(itens.get('observacao', ''))

                    descescopo = itens.get('escopos', [])
                    for esc in descescopo:
                        descricaoescopo.append(esc.get('descricao', ''))
                        valortotalescopo.append(esc.get('valorTotal', ''))
                        valorauditadoescopo.append(esc.get('valorAuditado', ''))
                        anexo = esc.get('anexo', {})
                        if anexo:
                            anexoescopo.append(anexo.get('nome', ''))

                    responsaveisitem = itens.get('responsaveis', [])
                    for resp in responsaveisitem:
                        responsavelitem.append(resp.get('nomeExibicao', ''))

                    evidenciasitem = itens.get('evidencias', [])
                    for evi in evidenciasitem:
                        anexo = evi.get('anexo', {})
                        if anexo:
                            anexoevidencia.append(anexo.get('nome', ''))
                        autor = evi.get('autor', {})
                        if autor:
                            autoranexoevidencia.append(autor.get('nome', ''))

                # SOLUÇÃO: Converter listas para strings usando join_data
                descteste = join_data(descteste)
                desccriterio = join_data(desccriterio)
                descinformacao = join_data(descinformacao)
                descfonte = join_data(descfonte)
                desclimitacao = join_data(desclimitacao)
                descachado = join_data(descachado)
                observacoes = join_data(observacoes)
                descricaoescopo = join_data(descricaoescopo)
                responsavelitem = join_data(responsavelitem)
                anexoescopo = join_data(anexoescopo)
                anexoevidencia = join_data(anexoevidencia)
                autoranexoevidencia = join_data(autoranexoevidencia)

                # SOLUÇÃO: Usar get() para todos os campos opcionais
                tarefasprecedentes = tarefa['campos'].get('tarefasPrecedentes', {}).get('valor')
                observadores = tarefa['campos'].get('observadores', {}).get('valor')
                hipoteselegal = tarefa['campos'].get('hipoteseLegal', {}).get('valor')

                matrizachados = tarefa['campos'].get('matrizAchados', {}).get('valor')
                matriz = matrizachados.get('nome', '') if matrizachados else ''

                coordenadorequipe = tarefa['campos'].get('CoordenadorEquipe', {}).get('valor')
                coordenador = []
                if coordenadorequipe:
                    for coordequipe in coordenadorequipe:
                        coordenador.append(coordequipe.get('nomeExibicao', ''))
                    coordenador = join_data(coordenador)
                else:
                    coordenador = ''

                equipegeral = tarefa['campos'].get('EquipeGeral', {}).get('valor')
                equipe = []
                if equipegeral:
                    for geralequipe in equipegeral:
                        equipe.append(geralequipe.get('nomeExibicao', ''))
                    equipe = join_data(equipe)
                else:
                    equipe = ''

                supervisores = tarefa['campos'].get('EquipeGeral', {}).get('valor')
                supervisor = []
                if supervisores:
                    for super in supervisores:
                        supervisor.append(super.get('nomeExibicao', ''))
                    supervisor = join_data(supervisor)
                else:
                    supervisor = ''

                estadosituacao = tarefa.get('estadoSituacao', '')

                filecomport = tarefa.get('arquivoComportamentoEspecifico')
                arquivocomportamento = filecomport if filecomport else ''

                descricaotag = tarefa['campos'].get('tags', {}).get('valor')
                tags = []
                if descricaotag:
                    for tagdesc in descricaotag:
                        tags.append(tagdesc.get('descricao', ''))
                    tags = join_data(tags)
                else:
                    tags = ''

                pendencias = tarefa.get('pendencias', [])
                listapendencia = []
                if pendencias:
                    for pendencia in pendencias:
                        listapendencia.append(pendencia.get('nomeUsuarioUnidade', ''))
                    listapendencia = join_data(listapendencia)
                else:
                    listapendencia = ''

                abasatividade = tarefa.get('abasAtividade', [])
                listaabaatividades = []
                if abasatividade:
                    for abas in abasatividade:
                        listaabaatividades.append(abas.get('descricao', ''))
                    listaabaatividades = join_data(listaabaatividades)
                else:
                    listaabaatividades = ''

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
                    'unidadesenvolvidas': nomeunidadesenvolvidas,
                    'descteste': descteste,
                    'desccriterio': desccriterio,
                    'descinformacao': descinformacao,
                    'descfonte': descfonte,
                    'desclimitacao': desclimitacao,
                    'descachado': descachado,
                    'observacoes': observacoes,
                    'descricaoescopo': descricaoescopo,
                    'responsavelitem': responsavelitem,
                    'anexoescopo': anexoescopo,
                    'anexoevidencia': anexoevidencia,
                    'autoranexoevidencia': autoranexoevidencia,
                    'matrizachados': matriz,
                    'tarefasprecedentes': tarefasprecedentes,
                    'observadores': observadores,
                    'hipoteselegal': hipoteselegal,
                    'coordenadorequipe': coordenador,
                    'equipegeral': equipe,
                    'supervisores': supervisor,
                    'arquivocomportamentoespecifico': arquivocomportamento,
                    'estadosituacao': estadosituacao,
                    'tags': tags,
                    'pendencias': listapendencia,
                    'abasatividade': listaabaatividades,
                })
        get_log(f"Lista {tipo_arquivo} tratada com sucesso")
        return lista_final
    except NameError as err:
        get_log(
            f"Erro ao tratar os {tipo_arquivo} get_analise_auditoria".upper())
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
                 tarefa['unidadesenvolvidas'],
                 tarefa['descteste'],
                 tarefa['desccriterio'],
                 tarefa['descinformacao'],
                 tarefa['descfonte'],
                 tarefa['desclimitacao'],
                 tarefa['descachado'],
                 tarefa['observacoes'],
                 tarefa['descricaoescopo'],
                 tarefa['responsavelitem'],
                 tarefa['anexoescopo'],
                 tarefa['anexoevidencia'],
                 tarefa['autoranexoevidencia'],
                 tarefa['matrizachados'],
                 tarefa['tarefasprecedentes'],
                 tarefa['observadores'],
                 tarefa['hipoteselegal'],
                 tarefa['coordenadorequipe'],
                 tarefa['equipegeral'],
                 tarefa['supervisores'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO analise_auditoria_auxiliar (id, situacao, estado, atividade, titulo, titulotarefaassociada, idtarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,unidadesenvolvidas,
                                                descteste,desccriterio,descricaoescopo,responsavelitem,anexoescopo,anexoevidencia,autoranexoevidencia,
                                                descinformacao,descfonte,desclimitacao,descachado,observacoes,arquivoComportamentoEspecifico,
                                                matrizachados,tarefasprecedentes,observadores, hipoteselegal, estadosituacao,
                                                coordenadorequipe,equipegeral,supervisores, tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log("Analise_auditoria salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log("Erro ao salvar os dados get_analise_auditoria".upper())
        get_log(err)
        return print("Erro ao salvar os dados get_analise_auditoria", err)

def get_analise_auditoria_requisicao(id):
    try:
        url = geral.url + \
            f"tarefa/{id}/dto/json"
        resp = requests.get(url, headers=geral.header)

        if resp.status_code != 200:
            get_log(
                f"Erro ao conectar com a url get_analise_auditoria, código do erro HTTP: {str(resp.status_code)}".upper())
            print(
                f"Erro ao conectar com a url get_analise_auditoria, código do erro HTTP: {str(resp.status_code)}")
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