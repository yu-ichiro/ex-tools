from ex_tools import DeferContext


def test_defer_basic():
    result = []
    with DeferContext() as defer:
        defer(lambda: result.append(1))
        defer(lambda: result.append(2))
        result.append(0)
    assert result == [0, 1, 2]


def test_defer_reverse():
    result = []
    with DeferContext(reverse=True) as defer:
        defer(lambda: result.append(2))
        defer(lambda: result.append(1))
        result.append(0)
    assert result == [0, 1, 2]


def test_defer_suppress():
    result = []

    class SuppressedException(BaseException):
        pass

    with DeferContext(suppress=SuppressedException) as defer:
        defer(lambda: result.append(1))
        result.append(0)
        raise SuppressedException

    assert result == [0, 1]


def test_defer_raise():
    result = []

    class RaisedException(BaseException):
        pass

    try:
        with DeferContext(suppress=RuntimeError) as defer:
            defer(lambda: result.append(1))
            result.append(0)
            raise RaisedException
    except RaisedException:
        result.append(2)

    assert result == [0, 1, 2]
