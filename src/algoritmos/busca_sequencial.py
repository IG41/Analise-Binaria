def busca_sequencial(chave, lista):
    for indice, elemento in enumerate(lista):
        if elemento == chave:
            return indice

    return -1
