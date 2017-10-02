
# Inconsistências

## Plano de Testes

1. Casos de teste implementados diferem do que foi documentado;
2. A implementação denota que o método `topo()` retorna o *operando* no topo da pilha, porém em um teste `expressaoComVariosOperandos` é esperado um *operador*;
    ?? método `topo()` retorna operando ou operador ??
3. É assumido que `getTamanho()` retorne o nº de *operandos*, porém em um teste `expressaoComVariosOperandos` é esperado que se retorne um resultado contando com os *operadores*; 
4. ...
