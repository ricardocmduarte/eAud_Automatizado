import os
import db_teste
import pandas as pd
import automessage_teste

from geral_teste import login
from datetime import datetime
from log_teste import get_log
import xlsxwriter


def converter_teste():
    try:
        mk_dir()
        banco = db_teste.db_connection_teste()

        tabela_banco = ['achados_auditoria_teste',
                        'analise_auditoria_teste',
                        'analise_preliminar_teste',
                        'apuracao_preliminar_teste',
                        'atividade_continuada_teste',
                        'auditorias_teste',
                        'auto_avaliacao_iacm_teste',
                        'beneficios_teste',
                        'comunicacao_auditoria_teste',
                        'escopo_auditoria_teste',
                        'execucao_consultoria_teste',
                        'interacoes_teste',
                        'item_analise_tce_teste',
                        'item_trabalho_atividade_teste',
                        'item_trabalho_projeto_teste',
                        'kpa_iacm_teste',
                        'matriz_planejamento_teste',
                        'minuta_posicionamento_teste',
                        'monitoramento_teste',
                        'planejamento_consultoria_teste',
                        'projeto_geral_teste',
                        'relatorio_final_teste',
                        'relatorio_preliminar_teste',
                        'resultados_consultoria_teste',
                        'tarefas_teste',
                        'termo_compromisso_consultoria_teste'
                        ]

        print("Lendo as tabelas")
        get_log("Iniciando conversão das tabelas em csv/excel")

        for tabela in tabela_banco:
            sql_query = pd.read_sql_query(
                f''' SELECT * FROM {tabela}''', banco)

            df = pd.DataFrame(sql_query)

            #####################
            # Save local server #
            #####################
            print(
                f"Iniciando processo, convertendo tabela {tabela} para csv  - pasta de rede")

            df.to_csv(f"C:\\E-aud\\Dados_E-aud\\dados_teste_{datahora()}\\csv\\{tabela}.csv",
                      index=False, encoding='utf-8-sig')

            print(
                f"Iniciando processo, convertendo tabela {tabela} para excel - pasta de rede")
            df.to_excel(f"C:\\E-aud\\Dados_E-aud\\dados_teste_{datahora()}\\excel\\{tabela}.xlsx",
                        index=False, engine='xlsxwriter')

            ###################
            # Save cloud path #
            ###################
            print(
                f"Iniciando processo, convertendo tabela {tabela} para csv - nuvem")
            get_log("Convertendos as tabelas em csv")
            df.to_csv(f"C:\\Users\\m1503249\\OneDrive - Cidade Administrativa MG\\Planilha e-Aud_teste\\dados_teste_{datahora()}\\csv\\{tabela}.csv",
                      index=False, encoding='utf-8-sig')

            print(
                f"Iniciando processo, convertendo tabela {tabela} para excel - nuvem")
            get_log("Convertendo as tabelas em xlsx")
            df.to_excel(f"C:\\Users\\m1503249\\OneDrive - Cidade Administrativa MG\\Planilha e-Aud_teste\\dados_teste_{datahora()}\\excel\\{tabela}.xlsx",
                        index=False, engine='xlsxwriter')

        automessage_teste.send_message_teste()
        return print("Processo finalizado")
    except NameError as err:
        return print("Erro", err)


def datahora():
    hora_now = datetime.now().strftime("%Y-%m-%d")
    return hora_now


def mk_dir():
    #####################
    # Save local server #
    #####################
    local_path_csv = f'C:\\E-aud\\Dados_E-aud\\dados_teste_{datahora()}\\csv'
    local_path_excel = f'C:\\E-aud\\Dados_E-aud\\dados-teste_{datahora()}\\excel'

    #####################
    # Save local server #
    #####################
    cloud_path_csv = f'C:\\Users\\{login}\\OneDrive - Cidade Administrativa MG\\Planilha e-Aud_teste\\dados_teste_{datahora()}\\csv'
    cloud_path_excel = f'C:\\Users\\{login}\\OneDrive - Cidade Administrativa MG\\Planilha e-Aud_teste\\dados-teste_{datahora()}\\excel'

    path_list = [local_path_csv, local_path_excel,
                 cloud_path_csv, cloud_path_excel]

    try:
        for dir in path_list:
            if os.path.exists(dir):
                get_log(f"Pasta {dir} já existe")
                print(f"Pasta {dir} já existe")
            else:
                os.makedirs(dir)
                get_log(f"Pasta {dir} criada com sucesso!")
                print(f"Pasta {dir} criada com sucesso!")
        return print("Criação de pastas finalizada com sucesso!")
    except NameError as err:
        get_log(f"Erro {err}")
        return print(f"Erro {err}")
converter_teste()