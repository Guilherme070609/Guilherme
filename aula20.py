# EXERCICIOS

# 1. Na lista pares = [0, 2, 4, 8]:
# a) Acrecente o valor 10 ao final da lista
# b) Acrecemte o valor 6 na posição 3.
pares = [0, 2, 4, 8]
pares.append(10)
pares.insert(3, 6)
print(pares)


# 2. Na lista impares = [1, 3, 3, 5, 7, 9]
# a) Remova o valor 3.
# b) Remova o valor da posição (indice) 4. 
# c) Mostre o valor que sera removido da posição
impares = [1, 3, 3, 5, 7, 9]
impares.remove(3)
impares.remove(impares[4])
print(impares)


# 3. Na lista Fibonancci = [8, 1, 0, 5, 13, 1, 3, 2]:
# a) Ordene a lista.
# b) Coloque em valor reverso a lista Fibonacci.
Fibonancci = [8, 1, 0, 5, 13, 1, 3, 2]
Fibonancci.sort()
print(Fibonancci)

# 4. Na lista pi [3, 1, 4, 1, 5, 9, 2, 6, 5]
# a) Busque o elemento que está no indice 5 da lista.
# b) imprima o tamanho da lista
# c) imprima o valor maximo da lista
# d) imprima o valor minimo da lista
# e) imprima apenas o resultado [4, 5]
pi = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(pi[5])
print(len(pi))
print(max(pi))
print(min(pi))
mova_lista = (4, 5)
print(mova_lista)
