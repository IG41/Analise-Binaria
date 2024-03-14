def busca_binaria(chave, lista_ordenada):
    return busca_binaria_(chave, lista_ordenada, 0, len(lista_ordenada) - 1)


def busca_binaria_(chave, lista, lim_inferior, lim_superior):
    if lim_inferior > lim_superior:
        return -1

    centro = (lim_inferior + lim_superior) // 2
    elemento_central = lista[centro]

    if elemento_central > chave:
        return busca_binaria_(chave, lista, lim_inferior, centro - 1)
    elif elemento_central < chave:
        return busca_binaria_(chave, lista, centro + 1, lim_superior)
    else:
        return centro


# def busca_binaria(chave, lista_ordenada):
#     limite_inferior = 0
#     limite_superior = len(lista_ordenada) - 1

#     while limite_inferior <= limite_superior:
#         centro = (limite_inferior + limite_superior) // 2
#         elemento_central = lista_ordenada[centro]

#         if elemento_central > chave:
#             limite_superior = centro - 1
#         elif elemento_central < chave:
#             limite_inferior = centro + 1
#         else:
#             return centro

#     return -1
