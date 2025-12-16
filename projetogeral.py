import db
import requests
import geral_env as geral
from log import get_log
import json
from join_function import join_data
from datetime import datetime

tipo_arquivo = 'get_projeto_geral'

def get_projeto_geral(ids):
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
                lista_dados.append(get_projeto_requisicao(id))
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
                detalhamento = tarefa['campos'].get('Detalhamento', {}).get('valor')
                denuncianum = tarefa['campos'].get('numDenuncia', {}).get('valor')
                numdenuncia = ''
                if denuncianum:
                    if denuncianum.startswith('&#34;'):
                        numdenuncia = ''
                    else:
                        numdenuncia = denuncianum

                localtrabalho = tarefa['campos'].get('localidadesPlanoTrabalho', {}).get('valor')
                localidadesplanotrabalho = []
                if localtrabalho:
                    for local in localtrabalho:
                        local_nome = local.get('nomeExibicao', '')
                        local_grupos = local.get('gruposLocalidade', '')
                        localidadesplanotrabalho.append(f"{local_nome}{local_grupos}")
                    localidadesplanotrabalho = join_data(localidadesplanotrabalho)

                proponenteplanotrabalho = tarefa['campos'].get('proponentePlanoTrabalho', {}).get('valor')
                planoetapa = tarefa['campos'].get('etapaPlanoTrabalho', {}).get('valor')
                etapaplanotrabalho = ''
                if planoetapa:
                    etapaplanotrabalho = planoetapa.get('valor', '')

                tprocess = tarefa['campos'].get('processT', {}).get('valor')
                processt = ''
                if tprocess:
                    processt = tprocess.get('valor', '')

                responsavelplanotrabalho = tarefa['campos'].get('responsavelPlanoTrabalho', {}).get('valor')
                origindemadna = tarefa['campos'].get('origemDemanda', {}).get('valor')
                origemdemanda = ''
                if origindemadna:
                    origemdemanda = origindemadna.get('valor', '')

                link = tarefa['campos'].get('links', {}).get('valor')
                links = []
                if link:
                    for lin in link:
                        link_descricao = lin.get('descricao', '')
                        link_url = lin.get('url', '')
                        links.append(f"{link_descricao} | {link_url}")
                    links = join_data(links)

                anexplanotrabalho = tarefa['campos'].get('anexosPlanoTrabalho', {}).get('valor')
                anexoplanotrabalho = []
                if anexplanotrabalho:
                    for file in anexplanotrabalho:
                        anexoplanotrabalho.append(file.get('nomeExibicao', ''))
                    anexoplanotrabalho = join_data(anexoplanotrabalho)

                processoplanotrabalho = tarefa['campos'].get('processoTrabalhoPlanoTrabalho', {}).get('valor')
                resulesperado = tarefa['campos'].get('resultadosEsperadosPlanoTrabalho', {}).get('valor')
                resultadosesperados = []
                if resulesperado:
                    for resultado in resulesperado:
                        resultadosesperados.append(resultado.get('nomeExibicao', ''))
                    resultadosesperados = join_data(resultadosesperados)

                objetocge = tarefa['campos'].get('objetoscgemg', {}).get('valor')
                objetoscgemg = []
                if objetocge:
                    for objetos in objetocge:
                        objetoscgemg.append(objetos.get('valor', ''))
                    objetoscgemg = join_data(objetoscgemg)

                duracaomeses = tarefa['campos'].get('duracaoMesesPlanoTrabalho', {}).get('valor')
                recursofinanceiro_valor = tarefa['campos'].get('recursoFinanceiroPlanoTrabalho', {}).get('valor')
                recursofinanceiro = str(recursofinanceiro_valor) if recursofinanceiro_valor is not None else ''

                envolplanotrabalho = tarefa['campos'].get('envolvidosPlanoTrabalho', {}).get('valor')
                envolvidosplanotrabalho = []
                if envolplanotrabalho:
                    for envolvidos in envolplanotrabalho:
                        envolvidosplanotrabalho.append(envolvidos.get('nomeExibicao', ''))
                    envolvidosplanotrabalho = join_data(envolvidosplanotrabalho)

                tag = tarefa['campos'].get('tags', {}).get('valor')
                tags = []
                if tag:
                    for tagtag in tag:
                        tags.append(tagtag.get('descricao', ''))
                    tags = join_data(tags)

                homemhora = tarefa['campos'].get('homemHorasPlanoTrabalho', {}).get('valor')
                gerenteplanotrabalho = tarefa['campos'].get('gerentesPlanoTrabalho', {}).get('valor')
                gerentesplanotrabalho = []
                if gerenteplanotrabalho:
                    for gerente in gerenteplanotrabalho:
                        gerentesplanotrabalho.append(gerente.get('nomeExibicao', ''))
                    gerentesplanotrabalho = join_data(gerentesplanotrabalho)

                equipe = tarefa['campos'].get('EquipeGeral', {}).get('valor')
                equipegeral = []
                if equipe:
                    for team in equipe:
                        equipegeral.append(team.get('nomeExibicao', ''))
                    equipegeral = join_data(equipegeral)

                supervisor = tarefa['campos'].get('supervisoresPlanoTrabalho', {}).get('valor')
                supervisores = []
                if supervisor:
                    for super in supervisor:
                        supervisores.append(super.get('nomeExibicao', ''))
                    supervisores = join_data(supervisores)

                objetivoplanotrabalho = tarefa['campos'].get('objetivoPlanoTrabalho', {}).get('valor')
                tipoplanotrablho = tarefa['campos'].get('tipoPlanoTrabalho', {}).get('valor')
                arquivocomportamento = tarefa.get('arquivoComportamentoEspecifico')
                estadosituacao = tarefa.get('estadoSituacao')

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
                    'numdenuncia': numdenuncia,
                    'detalhamento': detalhamento,
                    'localidadesplanotrabalho': localidadesplanotrabalho,
                    'proponenteplanotrabalho': proponenteplanotrabalho,
                    'etapaplanotrabalho': etapaplanotrabalho,
                    'processt': processt,
                    'responsavelplanotrabalho': responsavelplanotrabalho,
                    'origemdemanda': origemdemanda,
                    'links': links,
                    'anexoplanotrabalho': anexoplanotrabalho,
                    'processoplanotrabalho': processoplanotrabalho,
                    'resultadosesperados': resultadosesperados,
                    'objetoscgemg': objetoscgemg,
                    'duracaomeses': duracaomeses,
                    'recursofinanceiro': recursofinanceiro,
                    'envolvidosplanotrabalho': envolvidosplanotrabalho,
                    'homemhora': homemhora,
                    'gerentesplanotrabalho': gerentesplanotrabalho,
                    'equipegeral': equipegeral,
                    'supervisores': supervisores,
                    'objetivoplanotrabalho': objetivoplanotrabalho,
                    'tipoplanotrabalho': tipoplanotrablho,
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
                 tarefa['numdenuncia'],
                 tarefa['detalhamento'],
                 tarefa['etapaplanotrabalho'],
                 tarefa['processt'],
                 tarefa['responsavelplanotrabalho'],
                 tarefa['origemdemanda'],
                 tarefa['links'],
                 tarefa['anexoplanotrabalho'],
                 tarefa['processoplanotrabalho'],
                 tarefa['resultadosesperados'],
                 tarefa['objetoscgemg'],
                 tarefa['duracaomeses'],
                 tarefa['recursofinanceiro'],
                 tarefa['envolvidosplanotrabalho'],
                 tarefa['homemhora'],
                 tarefa['gerentesplanotrabalho'],
                 tarefa['equipegeral'],
                 tarefa['supervisores'],
                 tarefa['objetivoplanotrabalho'],
                 tarefa['tipoplanotrabalho'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO projeto_geral_auxiliar (id, situacao, estado, atividade, titulo, idtarefaassociada, titulotarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,numdenuncia,detalhamento,etapaplanotrabalho, processt,
                                                responsavelplanotrabalho,origemdemanda,links,anexoplanotrabalho,processoplanotrabalho,
                                                resultadosesperados,objetoscgemg,duracaomeses,recursofinanceiro,envolvidosplanotrabalho,homemhora,
                                                gerentesplanotrabalho,equipegeral,supervisores,objetivoplanotrabalho,tipoplanotrabalho,arquivocomportamentoespecifico, estadosituacao,
                                                tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)

def get_projeto_requisicao(id):
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