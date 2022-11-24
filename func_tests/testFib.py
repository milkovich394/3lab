from func import functions
import pytest
import numpy as numpy

class TestFib:

    # тестируем функцию на корректных данных
    def testTry(self):
        arr = numpy.array([1, 1, 2, 3, 5])
        assert (functions.Fib(5) == arr).all()

    # тестируем функцию на некорректных данных
    def testFalse(self):
        assert (functions.Fib(0) == 0).all()

    # тестируем функцию на некорректно введеных данных
    # n - целое, т.к равно коичеству элементов
    # запускаем функцию с числом неверного типа
    # вызвано исключение TypeError
    def test1(self):
        with pytest.raises(TypeError):
            functions.Fib(0.2)
