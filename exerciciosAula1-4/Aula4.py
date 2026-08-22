# Tema 4: Listas (list) e Iteração
# Exercício 4.1: O Maior e o Menor da Lista
# Objetivo: Crie uma lista com 5 números de sua escolha: numeros = [12, 45, 7, 89, 23].
# Regra: Use o laço for para percorrer a lista e calcular a soma de todos os números dela. Exiba a soma final na tela.

# Exercício 4.2: Filtrando Nomes com append()
# Objetivo: Crie uma lista inicial com 4 nomes: todos_nomes = ["Ana", "Bruno", "Amanda", "Carlos"].
# Regra: Crie uma segunda lista vazia nomes_com_a = []. 
# Percorra a lista todos_nomes com um for. Se o nome começar com a letra "A", adicione esse nome na lista nomes_com_a usando .append(). No final, imprima a nova lista.
# (Dica: Para verificar se um texto começa com a letra A, use nome.startswith("A") ou nome[0] == "A").

#Ex.4.1: O Maior e o Menor da lista.
#Lista com 5 números.

# lista_num = [15, 22, 7, 84, 63]
# soma = 0

# for numero in lista_num:
#     soma += numero

# print(f"A soma dos números é: {soma}")

#Ex4.2:Filtrando nomes com append()

#Criando uma lista vazia de nomes, e uma lista vazia que receberá os nomes
lista_nomes = ["Abel","Bernardo","Antonio","Emilly"]
nomes_com_a = []

#Funçao for, para contar dentro da lista_nomes o nome que contém A no inicio, por isso o uso do if (SE O NOME DA LISTA lista_nomes COMEÇAR COM "A") funçao .append Adicione o nome da condição SE dentro da lista nomes_com_a.

for nome in lista_nomes:
    if nome.startswith("A"):
        nomes_com_a.append(nome)

#Mostre o resultado da nova lista.
print(nomes_com_a)


