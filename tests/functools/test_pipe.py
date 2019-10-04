from ex_tools import Pipe


def test_pipe_normal():
    p = Pipe | range | list
    assert p(5) == [0, 1, 2, 3, 4]


def test_pipe_normal_collection():
    p = Pipe | range | (filter, lambda x: x % 2 == 1) | list
    assert p(10) == [1, 3, 5, 7, 9]
