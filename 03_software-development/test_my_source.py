from my_source import add_func


def test_add_one():
    assert add_func(2, 5) == 7


def test_add_fail():
    assert add_func(5, 5) == 9