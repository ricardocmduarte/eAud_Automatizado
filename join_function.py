def join_data(lista):
    lista_join = []
    full_data = []

    for i, teste in enumerate(lista):
        if teste != None or teste != '':
            full_data.append(teste)

    lista_join = '; '.join(full_data)

    return lista_join
