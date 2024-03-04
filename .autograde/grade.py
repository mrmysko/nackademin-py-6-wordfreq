import pytest

fn_name = "wordfreq"


class ImportDetailsError(Exception):
    pass


try:
    import uppgift

    fn = getattr(uppgift, fn_name)

    if not callable(fn):
        raise ImportDetailsError(f"Function {fn_name} is not callable")

    # Kontrollerar att funktionen tar ett argument
    if not fn.__code__.co_argcount == 1:
        raise ImportDetailsError(f"Function {fn_name} must take exactly one argument")

    def test_exempel_1():
        assert fn("hej hej på dig") == {"hej": 2, "på": 1, "dig": 1}

    def test_exempel_2():
        assert fn("ett två tre två") == {"ett": 1, "två": 2, "tre": 1}

    def test_exempel_3():
        assert fn("") == {}

    def test_exempel_4():
        assert fn("python programmering python") == {"python": 2, "programmering": 1}

    def test_exempel_5():
        assert fn("test test test") == {"test": 3}

except ImportDetailsError as e:
    pytest.fail(str(e))

except ImportError:
    pytest.fail(f"Function {fn_name} has not been implemented")
