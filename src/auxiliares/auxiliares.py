from random import choices


def cria_sequencia_aleatoria(tamanho):
    return choices(range(-2 * tamanho, 2 * tamanho), k=tamanho)


def print_resultados(n, q, qts_encontrados, tempo):
    print(
        f"\n-------------------------------------------------\n\
    - Para q = {q} e n = {n}\n\
        Encontradas {qts_encontrados} chaves.\n\
        O tempo de execução foi:\n\
        {tempo} segundos.\n"
    )
