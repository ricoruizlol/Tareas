#El assert comprueba lo que tu deseas hacer con el programa asegurarse de que una expresión sea verdadera.
# Si la expresión es falsa,se levantará una excepción de tipo AssertionError.
import pytest

from funciones import duplicados

def test_duplicados():
    assert duplicados([1,2,3,1])== True
    assert duplicados([1,2,3]) == False

@pytest.mark.parametrize("nums, res",
                         [

                             ([1,2,3,1], True),
                             ([1,2,3], False),
                             ([1,2,3,4,5], False),
                         ])
def test_duplicados_parametrizado(nums, res):
    assert duplicados(nums) == res



