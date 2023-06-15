from fila_prioritaria import FilaPrioritaria
from fila_normal import FilaNormal

fila_teste1 = FilaPrioritaria()
fila_teste2 = FilaNormal()

fila_teste1.atualiza_fila()
fila_teste1.atualiza_fila()
fila_teste1.atualiza_fila()
print(fila_teste1.chama_cliente(10))
print(fila_teste1.chama_cliente(11))
print(fila_teste1.chama_cliente(12))
print(fila_teste1.estatistica('15/06/2023', 141, 'detail'))

print('--------------')

fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
print(fila_teste2.chama_cliente(2))
print(fila_teste2.chama_cliente(3))
