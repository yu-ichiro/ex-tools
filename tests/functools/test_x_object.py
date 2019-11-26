from ex_tools import X, Partial, F


def test_x_object_basic():
    assert list(map(X + 1, range(5))) == [1, 2, 3, 4, 5]


def test_x_object_with_f():
    assert list(map(F[X + 1], range(5))) == [1, 2, 3, 4, 5]


def test_x_object_func():
    def a():
        return "h"

    def b():
        return "e"

    def c():
        return "l"

    def d():
        return "l"

    def e():
        return "o"
    assert ''.join(map(F[X()], [a, b, c, d, e])) == "hello"


def test_x_object_iterable():
    assert list(map(F[[X, X]], range(3))) == [[0, 0], [1, 1], [2, 2]]


def test_x_object_nested():
    assert list(map(F[dict(index=X, list=[X, X])], range(3))) == [
        dict(index=0, list=[0, 0]),
        dict(index=1, list=[1, 1]),
        dict(index=2, list=[2, 2]),
    ]


def test_x_object_x_partial():
    assert list(map(F[dict(index=X, range=Partial(range, X))], range(3))) == [
        dict(index=0, range=range(0)),
        dict(index=1, range=range(1)),
        dict(index=2, range=range(2)),
    ]


