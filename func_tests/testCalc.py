from func import functions
import pytest

class TestCalc:

    # тестируем функцию на корректных данных
    def testTry(self):
        assert functions.Calc(3, 2, '+') == 5

    # тестируем функцию на некорректных данных
    def testFalse(self):
        assert functions.Calc(3, 2, '*') == 2

    # тестируем функцию на некорректных данных
    # при введенных (0, 0, '/') должно возвращаться деление на 0
    # вызвано исключение ZeroDivisionError
    def test1(self):
        with pytest.raises(ZeroDivisionError):
            functions.Calc(0, 0, '/')
