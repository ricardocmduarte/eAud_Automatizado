import db
import pandas as pd
from geral import login
from datetime import datetime
from log import get_log
import xlsxwriter


def converter():
    try:
        banco = db.db_connection()

        tabela_banco = ['achados_auditoria',
                        'analise_auditoria',
                        'analise_preliminar',
                        'apuracao_preliminar',
                        'atividade_continuada',
                        'auditorias',
                        'auto_avaliacao_iacm',
                        'beneficios',
                        'comunicacao_auditoria',
                        'escopo_auditoria',
                        'execucao_consultoria',
                        'item_analise_tce',
                        'item_trabalho_atividade',
                        'item_trabalho_projeto',
                        'kpa_iacm',
                        'matriz_planejamento',
                        'minuta_posicionamento',
                        'monitoramento',
                        'planejamento_consultoria',
                        'projeto_geral',
                        'relatorio_final',
                        'relatorio_preliminar',
                        'resultados_consultoria',
                        'tarefas',
                        'termo_compromisso_consultoria'
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

            df.to_csv(f"R:\\BASES_DADOS\\e-AUD\\dados_{datahora()}\\csv\\{tabela}.csv",
                      index=False, encoding='utf-8-sig')

            print(
                f"Iniciando processo, convertendo tabela {tabela} para excel - pasta de rede")
            df.to_excel(f"R:\\BASES_DADOS\\e-AUD\\dados_{datahora()}\\excel\\{tabela}.xlsx",
                        index=False, engine='xlsxwriter')

            ###################
            # Save cloud path #
            ###################
            print(
                f"Iniciando processo, convertendo tabela {tabela} para csv - nuvem")
            get_log("Convertendos as tabelas em csv")
            df.to_csv(f"C:\\Users\\m1478769\\OneDrive - SEPLAG MG\\Planilha e-Aud\\dados_{datahora()}\\csv\\{tabela}.csv",
                      index=False, encoding='utf-8-sig')

            print(
                f"Iniciando processo, convertendo tabela {tabela} para excel - nuvem")
            get_log("Convertendo as tabelas em xlsx")
            df.to_excel(f"C:\\Users\\m1478769\\OneDrive - SEPLAG MG\\Planilha e-Aud\\dados_{datahora()}\\excel\\{tabela}.xlsx",
                        index=False, engine='xlsxwriter')

        return print("Processo finalizado")
    except NameError as err:
        return print("Erro", err)


def datahora():
    hora_now = datetime.now().strftime("%Y-%m-%d")
    return hora_now
