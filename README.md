# 🔍 Análise Binária

Este projeto é uma análise comparativa de diferentes algoritmos de busca, incluindo busca sequencial, busca sequencial otimizada e busca binária. O objetivo é avaliar a eficiência de cada método em diferentes cenários.

## 📁 Estrutura do Projeto

- **algoritmos/**
  - `__init__.py`
  - `busca_binaria.py`
  - `busca_sequencial.py`
  - `busca_sequencial_otimizada.py`
- **auxiliares/**
  - `__init__.py`
  - `auxiliares.py`
- `main.py`
- `testes.py`

## 🚀 Como Funciona

O arquivo `main.py` executa testes de busca usando os três algoritmos diferentes. Ele gera sequências aleatórias de dados e mede o tempo necessário para buscar elementos dentro dessas sequências. Os resultados são então exibidos para análise.

### 📜 Código Principal

```python
from algoritmos import busca_sequencial, busca_sequencial_otimizada, busca_binaria
from auxiliares import cria_sequencia_aleatoria, print_resultados
from time import time

valores_q = (10, 100, 1000)
valores_n = (10000, 100000, 1000000)

def teste_busca(busca, ordena=False):
    tempos = {}

    for n in valores_n:
        for q in valores_q:
            tempo_inicial = time()
            sequencia = cria_sequencia_aleatoria(n)
            chaves_para_buscar = cria_sequencia_aleatoria(q)
            qts_encontrados = 0

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
```

## 🛠️ Utilizados

Módulos de Algoritmos
busca_sequencial: Implementa a busca sequencial básica.
busca_sequencial_otimizada: Implementa a busca sequencial otimizada, ordenando os dados antes da busca.
busca_binaria: Implementa a busca binária, que é eficiente em listas ordenadas.
Módulos Auxiliares
cria_sequencia_aleatoria: Gera sequências aleatórias de dados.
print_resultados: Exibe os resultados dos testes, incluindo o tempo total gasto e a quantidade de elementos encontrados.
Biblioteca time
time: Utilizada para medir o tempo de execução das buscas.

## 📊 Resultados

Os resultados são apresentados na forma de tempos de execução para diferentes tamanhos de sequência (valores_n) e diferentes quantidades de chaves a serem buscadas (valores_q). Isso permite uma comparação clara da eficiência de cada algoritmo em diversos cenários.

📄 Licença

Este projeto está licenciado sob os termos da MIT License.
