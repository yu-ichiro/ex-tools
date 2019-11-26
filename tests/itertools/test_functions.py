from ex_tools import find, X, NotFound


def test_find_basic():
    range10 = range(10)
    assert find(X == 5, range10) == 5


def test_find_not_found():
    range10 = range(10)
    raised = False
    try:
        find(X == 100, range10)
    except NotFound:
        raised = True
    assert raised
