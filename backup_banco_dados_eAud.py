import os
import subprocess
from datetime import datetime
import geral_env as geral  # Corrigido o import
import logging
import psycopg2  # Importação do psycopg2

# Configuração do logging para salvar em um arquivo
data_atual = datetime.now().strftime('%d-%m-%Y')
caminho_diretorio = f"C:\\Users\\M1503249\\Documents\\logs_eAud\\log_eAud_Automatizado_Backup_{data_atual}.log"
caminho_diretorio1 = f"C:\\Users\\M1503249\\OneDrive - Cidade Administrativa MG\\Documents\\logs_eAud\\log_eAud_Automatizado_Backup_{data_atual}.log"
caminho_diretorio_backup = f"C:\\Users\\M1503249\\Desktop\\Backup_BD_eAud"
caminho_diretorio_backup1 = f"C:\\Users\\M1503249\\OneDrive - Cidade Administrativa MG\\Backup_BD_eAud"
logging.basicConfig(filename=caminho_diretorio, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename=caminho_diretorio1, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_db_conection():
    # Cria a conexão com o banco de dados
    conn = psycopg2.connect(
        dbname=geral.database2,
        user=geral.login2,
        password=geral.password2,
        host=geral.server2,
        port='5432'
    )
    return conn

def backup_banco_dados_eAud():
    # Obtém a conexão com o banco de dados
    conn = get_db_conection()

    # Diretório de backup
    diretorio_backup = caminho_diretorio_backup
    diretorio_backup1 = caminho_diretorio_backup1
    if not os.path.exists(diretorio_backup): 
        os.makedirs(diretorio_backup)
        
    if not os.path.exists(diretorio_backup1):
        os.makedirs(diretorio_backup1)
        
    # Nome do arquivo de backup
    nome_arquivo_backup = f"{geral.database2}_{data_atual}.backup"
    arquivo_backup = os.path.join(diretorio_backup, nome_arquivo_backup)
    
    nome_arquivo_backup1 = f"{geral.database2}_{data_atual}.backup"
    arquivo_backup1 = os.path.join(diretorio_backup1, nome_arquivo_backup1)
    
    # Definir a senha do banco de dados na variável de ambiente
    os.environ['PGPASSWORD'] = geral.password2

    # Comando para executar o pg_dump
    comando = [
        'C:\\Program Files\\PostgreSQL\\14\\bin\\pg_dump',  # Caminho completo para pg_dump
        '-h', geral.server2,
        '-p', '5432',
        '-U', geral.login2,
        '-F', 't',  # Formato tar
        '-b',       # Inclui blobs
        '-v',       # Modo verbose 
        '-f', arquivo_backup,
        geral.database2
    ]
    
    comando1 = [
        'C:\\Program Files\\PostgreSQL\\14\\bin\\pg_dump',  # Caminho completo para pg_dump
        '-h', geral.server2,
        '-p', '5432',
        '-U', geral.login2,
        '-F', 't',  # Formato tar
        '-b',       # Inclui blobs
        '-v',       # Modo verbose
        '-f', arquivo_backup1, 
        geral.database2
    ]


    try:
        # Executa o comando pg_dump
        subprocess.run(comando, check=True)
        subprocess.run(comando1, check=True)
        logging.info(f'Backup do banco de dados {geral.database2} concluído com sucesso. Arquivo: {arquivo_backup}')
        logging.info(f'Backup do banco de dados {geral.database2} concluído com sucesso. Arquivo: {arquivo_backup1}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Erro ao realizar o backup do banco de dados: {e}')
    finally:
        # Fecha a conexão com o banco de dados
        # Remover a variável de ambiente para segurança
        del os.environ['PGPASSWORD']
        
backup_banco_dados_eAud()
    