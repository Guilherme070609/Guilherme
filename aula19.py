nomes = ["Ana", "Paula", "Maria", "Sophia", "Fernanda", "sophia"]

print(f"a primeira ocorrencia de sohpia é no indice: {nomes.index("Sophia")}")

print(f"Sophia aparece {nomes.count("Sophia")} vezes na lista")

nomes.sort()
print(nomes)

nomes.reverse()
print(nomes)

copianomes = nomes.copy()
print(f"Nomes copiados: {copianomes}")