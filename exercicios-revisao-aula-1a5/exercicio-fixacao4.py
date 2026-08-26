#Exercicio 4.1 soma de elementos de uma lista:
# Criar uma lista com 5 numeros int, use um laço for para percorrer a lista e somar todos os elementos.

#Criando lista:

numeros = [1, 2, 4, 6, 7]

soma = 0

for i in numeros:
    soma += i
    print(f"Soma atual: {soma}")

#Exercicio 4.2 filtro de nomes com append.
#Crie uma lista com 5 nomes, crie uma segunda lista vazia
#usando for e if, adicione nessa segunda lista apenas nomes com A.

nomes = ["Antonio", "Emilly", "Abel", "Gabriel", "Romulo"]

nomes_com_a = []

for nome in nomes:
      if nome.startswith("A"):
          nomes_com_a.append(nome)

print(nomes_com_a)

#Exercicio 4.3 cadastro e atualização de produta dicionario:
#Crie um dicionario para um produto com as chaves "nome" "preco" "estoque", peça ao usuario um novo valor para estoque e atualize o dicionario.

produto = {
    "nome": "Cerveja",
    "preco": 3.00,
    "estoque":  4,
}

print(f"Estoque atual: {produto['estoque']}")

novo_estoque = int(input("Digite a nova quantidade no estoque: "))

produto["estoque"] = novo_estoque

print("---- DADOS DO PRODUTO ATUALIZADOS ----")
print(f"Nome: {produto['nome']}")
print(f"Preço: {produto['preco']}")
print(f"Estoque: {produto['estoque']}")

#Exercicio 4.4 crie uma lista contendo números repetidos, converta a lista para um conjunto set, para remover as duplicatas e exiba o resultado.

#Criando a lista

numeros_r = [1,2,2,3,4,4,5]
numeros_sem_r = set(numeros_r)

print(numeros_sem_r)

lista_sem_r = list(numeros_sem_r)

print(lista_sem_r)

#Exercicio 4.5 criar uma tupla com dias da semana, pedir numero ao usuario e exibir o dia da semana.

#Criar tupla:

dias_da_semana = ("Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo")

#Para acessar um valor dentro da tupla, é feito da mesma maneira que na lista >>> dias_da_semana[0 a 6].

#Pedindo valor ao usuario.
dia = int(input("Digite um número de 1 a 7 para corresponder ao dia da semana: "))

while dia < 1 or dia > 7:
    print("Opção inválida!")
    dia = int(input("Digite novamente, escolha um número de 1 a 7: "))

print(f"O dia selecionado foi: {dias_da_semana[dia - 1]}")
  