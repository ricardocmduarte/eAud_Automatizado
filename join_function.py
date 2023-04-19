def join_data(lista):
    lista_join = []
    empty_data = ''
    for i, teste in enumerate(lista):
        if teste != None:
            lista_join = '; '.join(lista)

            return lista_join

    return empty_data
