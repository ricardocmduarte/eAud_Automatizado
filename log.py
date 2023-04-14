from datetime import datetime
from os import getlogin


def get_log(msg):
    lista_msg = []
    nova_lista = []
    hora_atualizacao = datetime.now().strftime("%d/%b/%Y - %H:%M:%S")

    if msg:
        lista_msg.append(msg)
    for linha in lista_msg:
        linha = (f"{linha} => {hora_atualizacao}")
        nova_lista.append(linha)

    save_log(nova_lista)


def save_log(lista_msg):
    dia = datetime.now().strftime("%d-%b-%Y")
    log_file = f"C:\\Users\\{getlogin()}\\OneDrive - SEPLAG MG\\logs eAud\\log eAud {dia}.txt"
    with open(log_file, 'a') as f:
        for linha in lista_msg:
            f.write(f"{linha}\n")
