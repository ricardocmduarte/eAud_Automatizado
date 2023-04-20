def join_data(lista):
    lista_join = []

    for i, texto in enumerate(lista):
        if texto is None or texto == '':
            pass
        else:
            lista_join.append(texto)

    lista_join = '; '.join(lista_join)

    return lista_join
