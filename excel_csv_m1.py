import os
import db
import pandas as pd
import automessage

from geral_env import login
from datetime import datetime
from log import get_log
import xlsxwriter


def converter_m1():
    try:
        mk_dir()
        banco = db.db_connection()

        tabela_banco = ['achados_auditoria_auxiliar',
                        'analise_auditoria_auxiliar',
                        'analise_preliminar_auxiliar',
                        'apuracao_preliminar_auxiliar',
                        'atividade_continuada_auxiliar',
                        'auditorias_auxiliar',
                        'auto_avaliacao_iacm_auxiliar',
                        'beneficios_auxiliar',
                        'comunicacao_auditoria_auxiliar',
                        'escopo_auditoria_auxiliar',
                        'execucao_consultoria_auxiliar',
                        'interacoes_auxiliar',
                        'item_analise_tce_auxiliar',
                        'item_trabalho_atividade_auxiliar',
                        'item_trabalho_projeto_auxiliar',
                        'kpa_iacm_auxiliar',
                        'matriz_planejamento_auxiliar',
                        'minuta_posicionamento_auxiliar',
                        'monitoramento_auxiliar',
                        'planejamento_consultoria_auxiliar',
                        'projeto_geral_auxiliar',
                        'relatorio_final_auxiliar',
                        'relatorio_preliminar_auxiliar',
                        'resultados_consultoria_auxiliar',
                        'tarefas_auxiliar',
                        'tarefas_id_auxiliar',
                        'beneficios_id_auxiliar',
                        'termo_compromisso_consultoria_auxiliar'
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

            df.to_csv(f"U:\\30_Dashboards para E-aud\\4_Dados do E-aud\\dados_{datahora()}\\csv\\{tabela}.csv",
                      index=False, encoding='utf-8-sig')

            print(
                f"Iniciando processo, convertendo tabela {tabela} para excel - pasta de rede")
            df.to_excel(f"U:\\30_Dashboards para E-aud\\4_Dados do E-aud\\dados_{datahora()}\\excel\\{tabela}.xlsx",
                        index=False, engine='xlsxwriter')

            ###################
            # Save cloud path #
            ###################
            print(
                f"Iniciando processo, convertendo tabela {tabela} para csv - nuvem")
            get_log("Convertendos as tabelas em csv")
            df.to_csv(f"C:\\Users\\m1503249\\OneDrive - Cidade Administrativa MG\\Planilha e-Aud\\dados_{datahora()}\\csv\\{tabela}.csv",
                      index=False, encoding='utf-8-sig')

            print(
                f"Iniciando processo, convertendo tabela {tabela} para excel - nuvem")
            get_log("Convertendo as tabelas em xlsx")
            df.to_excel(f"C:\\Users\\m1503249\\OneDrive - Cidade Administrativa MG\\Planilha e-Aud\\dados_{datahora()}\\excel\\{tabela}.xlsx",
                        index=False, engine='xlsxwriter')

        automessage.send_message()
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
    local_path_csv = f'U:\\30_Dashboards para E-aud\\4_Dados do E-aud\\dados_{datahora()}\\csv'
    local_path_excel = f'U:\\30_Dashboards para E-aud\\4_Dados do E-aud\\dados_{datahora()}\\excel'

    #####################
    # Save local server #
    #####################
    cloud_path_csv = f'C:\\Users\\{login}\\OneDrive - Cidade Administrativa MG\\Planilha e-Aud\\dados_{datahora()}\\csv'
    cloud_path_excel = f'C:\\Users\\{login}\\OneDrive - Cidade Administrativa MG\\Planilha e-Aud\\dados_{datahora()}\\excel'

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
converter_m1()