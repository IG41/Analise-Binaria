import pytest
from algoritmos import busca_sequencial, busca_sequencial_otimizada, busca_binaria


@pytest.mark.parametrize(
    "input, expected_result",
    [
        ((11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), -1),
        ((0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), -1),
        ((6, [1, 2, 3, 4, 5, 7, 8, 9, 10]), -1),
        ((5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 4),
        ((1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0),
        ((10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 9),
    ],
)
def test_busca_sequencial(input, expected_result):
    assert busca_sequencial(*input) == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [
        ((11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), -1),
        ((0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), -1),
        ((6, [1, 2, 3, 4, 5, 7, 8, 9, 10]), -1),
        ((5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 4),
        ((1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0),
        ((10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 9),
    ],
)
def test_busca_sequencial_otimizada(input, expected_result):
    assert busca_sequencial_otimizada(*input) == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [
        ((11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), -1),
        ((0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), -1),
        ((6, [1, 2, 3, 4, 5, 7, 8, 9, 10]), -1),
        ((5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 4),
        ((1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0),
        ((10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 9),
    ],
)
def test_busca_binaria(input, expected_result):
    assert busca_binaria(*input) == expected_result
