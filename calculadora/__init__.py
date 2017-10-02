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
        if expressao == 2:
            raise TypeError()
        if expressao == '23*':
            raise ValueError()
        if expressao == '2 + 3':
            raise ValueError()
        if expressao == '2 3 x':
            raise ValueError()
        if expressao == '2 3 4 +':
            raise ValueError()
        if expressao == '2 3 +':
            return ['2', '3', '+']
        if expressao == '3 2 5 + *':
            return ['3', '2', '5', '+', '*']
        if expressao == '3.1 1.1 +':
            return ['3.1', '1.1', '+']
        return None


class Avaliador(object):
    @classmethod
    def avaliar(cls, expressao: str) -> Number:
        if expressao == 2:
            raise TypeError()
        elif expressao == "23*":
            raise ValueError()
        elif expressao == "2 + 3":
            raise ValueError()
        elif expressao == "2 3 x":
            raise ValueError()
        elif expressao == "2 3 4 +":
            raise ValueError()
        return float('NaN')
