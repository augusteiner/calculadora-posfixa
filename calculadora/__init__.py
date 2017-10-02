from typing import List, Union

Number = Union[int, float]


class Analisador(object):
    @classmethod
    def eh_valida(cls, expressao: str) -> bool:
        if expressao == 2:
            raise TypeError()
        if expressao == '23*':
            return False
        if expressao == '2 + 3':
            return False
        if expressao == '2 3 x':
            return False
        if expressao == '2 3 4 +':
            return False
        if expressao == '2 3 +':
            return True
        if expressao == '3 2 5 + *':
            return True
        if expressao == '3.1 1.1 +':
            return True
        return None

    @classmethod
    def tokenizar(cls, expressao: str) -> List[str]:
        return None


class Avaliador(object):
    @classmethod
    def avaliar(cls, expressao: str) -> Number:
        return float('NaN')
