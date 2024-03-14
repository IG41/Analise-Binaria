def busca_sequencial_otimizada(chave, lista_ordenada):
    for indice, elemento in enumerate(lista_ordenada):
        if elemento == chave:
            return indice
        if elemento > chave:
            return -1

    return -1
