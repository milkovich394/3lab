from func import functions
import pytest

class TestSort:

    # тестируем функцию на корректных данных
    def testTry(self):
        a = ['a' 'b']
        b = ['a' 'b']
        assert (functions.Sort(a) == b)

    # тестируем функцию на некорректных данных
    def testFalse(self):
        a = [5, 4, 3, 2, 1]
        b = [1, 2, 4, 3, 5]
        assert (functions.Sort(a) == b)

    # тестируем функцию на некорректно введеных данных
    # a - массив(список)
    # запускаем функцию с данными неверного типа
    # вызвано исключение TypeError
    def test1(self):
        with pytest.raises(TypeError):
            functions.Sort(0)
