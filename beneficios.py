import db
import requests
import geral
from log import get_log
import json
from join_function import join_data
import db


tipo_arquivo = 'get_beneficios'


def get_beneficios():
    response = geral.check_url_health('tarefa')
    get_log(f"Iniciado {tipo_arquivo}")

    if response != 200:
        get_log(
            f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP:  {str(response)}".upper())
        return print(f"Erro ao conectar com a url {tipo_arquivo}, código do erro HTTP:  {str(response)}")

    lista_dados = []
    lista_final = []
    try:
        banco = db.db_connection()
        ids = db.get_idbeneficios('beneficios_id', banco)
        if ids:
            for i, id in enumerate(ids):
                lista_dados.append(get_beneficios_requisicao(id['id']))

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

            beneficioavulso = tarefa['campos']['benAvulso']['valor']

            descricaobeneficio = tarefa['campos']['descricaoBenef']['valor']

            valorbruto = tarefa['campos']['valorBruto']['valor']
            descricaocusto = tarefa['campos']['descricaoCusto']['valor']

            drben = tarefa['campos']['drben']['valor']
            dimensaoerepercussao = []
            if drben:
                dimensaoerepercussao = drben['valor']

            valorcusto = tarefa['campos']['valorCusto']['valor']

            unidadeenvolvida = tarefa['campos']['unidadesEnvolvidas']['valor']
            unidadesenvolvidas = []
            if unidadeenvolvida:
                for i, envol in enumerate(unidadeenvolvida):
                    unidadesenvolvidas.append(envol['nomeExibicao'])

                unidadesenvolvidas = join_data(unidadesenvolvidas)

            unidgestora = tarefa['campos']['unidadeGestoraBeneficio']['valor']
            unidadegestora = []
            if unidgestora:
                unidadegestora = unidgestora['nomeExibicao']

            anexoben = tarefa['campos']['anexosBeneficio']['valor']
            anexosbeneficio = []
            if anexoben:
                for i, file in enumerate(anexoben):
                    anexosbeneficio.append(file['nome'])

                anexosbeneficio = join_data(anexosbeneficio)

            providenciabeneficio = tarefa['campos']['providenciaBenef']['valor']

            dimensaoben = tarefa['campos']['dimensaoMEBeneficio']['valor']
            dimensaomebeneficio = []
            if dimensaoben:
                dimensaoerepercussao = dimensaoben['valor']

            parcelasbeneficio = tarefa['campos']['parcelasBeneficio']['valor']

            fundbeneficio = tarefa['campos']['fundamentoBenef']['valor']
            titulofundamento = ''
            if fundbeneficio:
                titulofundamento = fundbeneficio['nomeExibicao']

            textofundamentobeneficio = tarefa['campos']['textoFundamentoBenef']['valor']
            valorliquido = tarefa['campos']['valorLiquido']['valor']

            classben = tarefa['campos']['classeBenef']['valor']
            classebeneficio = ''
            if classben:
                classebeneficio = classben['valor']
            bentipo = tarefa['campos']['tipoBeneficio']['valor']
            tipobeneficio = []
            if bentipo:
                tipobeneficio = bentipo['valor']

            tarefasprec = tarefa['campos']['tarefasPrecedentes']['valor']
            tarefasprecedentes = []
            if tarefasprec:
                for i, tarefapre in enumerate(tarefasprec):
                    tarefasprecedentes.append(tarefapre['nomeExibicao'])
                tarefasprecedentes = join_data(tarefasprecedentes)

            unidproponente = tarefa['campos']['unidadeProponenteBenef']['valor']
            unidadeproponente = ''
            if unidproponente:
                unidadeproponente = unidproponente['nomeExibicao']

            anofatogeradorbeneficio = tarefa['campos']['anoFatoGeradorBeneficio']['valor']

            descricaotag = tarefa['campos']['tags']['valor']
            tags = []
            if descricaotag:
                for i, tagdesc in enumerate(descricaotag):
                    tags.append(tagdesc['descricao'])

                tags = join_data(tags)

            situacaoanteriorbeneficio = tarefa['campos']['situacaoAnteriorBenef']['valor']
            anoimplementacaobeneficio = tarefa['campos']['anoImplementacaoBeneficio']['valor']

            benrepercussao = tarefa['campos']['repercussaoDoBeneficio']['valor']
            repercussaobeneficio = ''
            if benrepercussao:
                repercussaobeneficio = benrepercussao['valor']

            classbf = tarefa['campos']['classeBF']['valor']
            classebf = ''
            if classbf:
                classebf = classbf['valor']

            nivelbeneficio = tarefa['campos']['nivelBeneficio']['valor']

            classbnf = tarefa['campos']['classebnf']['valor']
            classebnf = ''
            if classbnf:
                classebnf = classbnf['valor']

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
                'beneficioavulso': beneficioavulso,
                'descricaobeneficio': descricaobeneficio,
                'valorbruto': valorbruto,
                'descricaocusto': descricaocusto,
                'dimensaorepercussao': dimensaoerepercussao,
                'valorcusto': valorcusto,
                'unidadesenvolvidas': unidadesenvolvidas,
                'unidadegestora': unidadegestora,
                'anexosbeneficio': anexosbeneficio,
                'providenciabeneficio': providenciabeneficio,
                'dimenssaobeneficio': dimensaomebeneficio,
                'parcelasbeneficio': parcelasbeneficio,
                'titulofundamento': titulofundamento,
                'textofundamentobeneficio': textofundamentobeneficio,
                'valorliquido': valorliquido,
                'classebeneficio': classebeneficio,
                'tipobeneficio': tipobeneficio,
                'tarefasprecedentes': tarefasprecedentes,
                'unidadeproponente': unidadeproponente,
                'anofatogeradorbeneficio': anofatogeradorbeneficio,
                'situacaoanateriorbeneficio': situacaoanteriorbeneficio,
                'anoimplementacaobeneficio': anoimplementacaobeneficio,
                'repercussaobeneficio': repercussaobeneficio,
                'classebf': classebf,
                'nivelbeneficio': nivelbeneficio,
                'classebnf': classebnf,
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
                 tarefa['beneficioavulso'],
                 tarefa['descricaobeneficio'],
                 tarefa['valorbruto'],
                 tarefa['descricaocusto'],
                 tarefa['dimensaorepercussao'],
                 tarefa['valorcusto'],
                 tarefa['unidadesenvolvidas'],
                 tarefa['unidadegestora'],
                 tarefa['anexosbeneficio'],
                 tarefa['providenciabeneficio'],
                 tarefa['dimenssaobeneficio'],
                 tarefa['parcelasbeneficio'],
                 tarefa['titulofundamento'],
                 tarefa['textofundamentobeneficio'],
                 tarefa['valorliquido'],
                 tarefa['classebeneficio'],
                 tarefa['tipobeneficio'],
                 tarefa['tarefasprecedentes'],
                 tarefa['unidadeproponente'],
                 tarefa['anofatogeradorbeneficio'],
                 tarefa['situacaoanateriorbeneficio'],
                 tarefa['anoimplementacaobeneficio'],
                 tarefa['repercussaobeneficio'],
                 tarefa['classebf'],
                 tarefa['nivelbeneficio'],
                 tarefa['classebnf'],
                 tarefa['arquivocomportamentoespecifico'],
                 tarefa['estadosituacao'],
                 tarefa['tags'],
                 tarefa['pendencias'],
                 tarefa['abasatividade']
                 )]
            array_records = ", ".join(["%s"] * len(lista))
            insert_query = (f"""INSERT INTO beneficios (id, situacao, estado, atividade, titulo, titulotarefaassociada,
                                                dtprevisaoinicio,dtprevisaofim,dtrealizadainicio,dtrealizadafim,
                                                prioridade,assunto,idatividade,descricaoatividade, idsituacao,
                                                dataultimamodificacao,autorultimamodificacao,beneficioavulso,descricaobeneficio,valorbruto,
                                                descricaocusto,dimensaorepercussao,valorcusto,unidadesenvolvidas,unidadegestora,
                                                anexosbeneficio,providenciabeneficio,dimenssaobeneficio,parcelasbeneficio,
                                                titulofundamento,textofundamentobeneficio,valorliquido,classebeneficio,tipobeneficio,
                                                tarefasprecedentes,unidadeproponente,anofatogeradorbeneficio,situacaoanateriorbeneficio,
                                                anoimplementacaobeneficio,repercussaobeneficio,classebf,nivelbeneficio,classebnf,
                                                arquivocomportamentoespecifico, estadosituacao,tags,pendencias,abasatividade) VALUES {array_records}""")

            cur.execute(insert_query, lista)
        get_log(f"{tipo_arquivo} salvo com sucesso")
        banco.commit()
        banco.close()
    except NameError as err:
        get_log(f"Erro ao salvar os dados {tipo_arquivo}".upper())
        get_log(err)
        return print(f"Erro ao salvar os dados {tipo_arquivo}", err)


def get_beneficios_requisicao(id):
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
