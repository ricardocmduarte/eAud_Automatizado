import db
import pandas as pd
from geral import login
from datetime import datetime
from log import get_log


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
                        'termo_compromisso_consultoria',
                        ]

        print("Lendo as tabelas")
        get_log("Iniciando conversão das tabelas em csv/excel")

        tabelas_banco = ['achados_auditoria',
                         'arquivos',
                         'auditorias',
                         'auditorias_pendencias',
                         'auditorias_localidade',
                         'auditorias_unidades_envolvidas',
                         'auditorias_unidades_auditadas',
                         'achados_auditoria_pendencias',
                         'analise_auditoria',
                         'analise_auditoria_pendencias',
                         'analise_preliminar',
                         'analise_preliminar_pendencias',
                         'beneficios',
                         'beneficios_pendencias',
                         'escopo_auditoria',
                         'escopo_auditoria_pendencias',
                         'indicadores',
                         'localidades',
                         'matriz_planejamento',
                         'matriz_planejamento_pendencias',
                         'monitoramento',
                         'monitoramento_manifestacao',
                         'monitoramento_pendencias',
                         'monitoramento_posicionamento',
                         'monitoramento_unidades',
                         'plano_operacional',
                         'plano_operacional_pactuacao',
                         'plano_operacional_pendencias',
                         'plano_trabalho',
                         'plano_trabalho_localidades',
                         'plano_trabalho_pendencias',
                         'plano_trabalho_unidades_envolvidas',
                         'relatorio_auditoria',
                         'relatorio_auditoria_pendencias',
                         'tarefas',
                         'tarefas_pendencias',
                         'unidade',
                         'unidade_gestores',
                         'unidade_tipos',
                         'usuario']

        for tabela in tabela_banco:
            sql_query = pd.read_sql_query(
                f''' SELECT * FROM {tabela}''', banco)

            df = pd.DataFrame(sql_query)
            # Save to cloud
            # df.to_csv(f"C:\\Users\\{login}\\OneDrive - SEPLAG MG\\Planilha e-Aud\\csv\\{tabela}.csv",
            #           index=False, encoding='utf-8-sig')
            # df.to_excel(f"C:\\Users\\{login}\\OneDrive - SEPLAG MG\\Planilha e-Aud\\excel\\{tabela}.xlsx",
            #             index=False, encoding='utf-8-sig')

            ''' print(f"Iniciando processo, convertendo tabela {tabela} para csv ")
            # Save local server
            df.to_csv(f"R:\\BASES_DADOS\\e-AUD\\dados_{datahora()}\\csv\\{tabela}.csv",
                      index=False, encoding='utf-8-sig')

            print(
                f"Iniciando processo, convertendo tabela {tabela} para excel ")
            df.to_excel(f"R:\\BASES_DADOS\\e-AUD\\dados_{datahora()}\\excel\\{tabela}.xlsx",
                        index=False, encoding='utf-8-sig', engine='xlsxwriter')'''

            # Save cloud path
            print(f"Iniciando processo, convertendo tabela {tabela} para csv ")
            get_log("Convertendos as tabelas em csv")
            df.to_csv(f"C:\\Users\\m1478769\\OneDrive - SEPLAG MG\\Planilha e-Aud\\csv\\{tabela}.csv",
                      index=False, encoding='utf-8-sig')

            print(
                f"Iniciando processo, convertendo tabela {tabela} para excel ")
            get_log("Convertendo as tabelas em xlsx")
            df.to_excel(f"C:\\Users\\m1478769\\OneDrive - SEPLAG MG\\Planilha e-Aud\\excel\\{tabela}.xlsx",
                        index=False, encoding='utf-8-sig', engine='xlsxwriter')

            return print("Processo finalizado")
    except NameError as err:
        return print("Erro", err)


def datahora():
    hora_now = datetime.now().strftime("%Y-%m-%d")
    return hora_now
