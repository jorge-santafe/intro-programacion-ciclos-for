'''
Sintaxis de la funcion range()

range([inicio], fin, [paso])

- El inicio es 0 por defecto, si no se indica
- El paso es 1 por defecto si no lo indica

- La funcion range genera una serie de numeros int entre inicio y fin-1, con incremento dado por el paso

'''
# caso 1: range(fin)
print(list(range(10))) #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(list(range(101)))
print(list(range(32)))

# Caso 2: range (inicio, fin)
print(list(range(3, 10)))
print(list(range(11, 13)))
print(list(range(1001, 1002)))

# Caso 3: range(inicio, fin, paso)
print(list(range(3, 20, 2)))
print(list(range(3, 21, 2)))
print(list(range(5, 51, 5)))
print(list(range(21, 0, -2)))