from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"

    word = "test"
    assert count_ocurrences(path, word) == 2687

    word_joao = "joao"
    assert count_ocurrences(path, word_joao) == 0
