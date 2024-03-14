from algoritmos import busca_sequencial, busca_sequencial_otimizada, busca_binaria
from auxiliares import cria_sequencia_aleatoria, print_resultados
from time import time

valores_q = (10, 100, 1000)
valores_n = (10000, 100000, 1000000)


def teste_busca(busca, ordena=False):
    tempos = {}

    for n in valores_n:
        for q in valores_q:
            sequencia = cria_sequencia_aleatoria(n)
            chaves_para_buscar = cria_sequencia_aleatoria(q)
            qts_encontrados = 0

            tempo_inicial = time()

            if ordena:
                sequencia.sort()

            for chave in chaves_para_buscar:
                indice = busca(chave, sequencia)

                if indice is not None:
                    qts_encontrados += 1

            tempo_total = time() - tempo_inicial

            print_resultados(n, q, qts_encontrados, tempo_total)

    return tempos


if __name__ == "__main__":
    print("******** BUSCA SEQUENCIAL *********")
    teste_busca(busca_sequencial)

    print("******** BUSCA SEQUENCIAL OTIMIZADA *********")
    teste_busca(busca_sequencial_otimizada, ordena=True)

    print("******** BUSCA BINARIA *********")
    teste_busca(busca_binaria, ordena=True)
