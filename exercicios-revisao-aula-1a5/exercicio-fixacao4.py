#Exercicio 4.1 Soma de elementos de uma lista, crie uma lista com 5 numeros inteiros, use um laço for para percorrer a lista exibir a soma total dos elementos.

# lista = [4,16,95,48,12]

# soma = 0

# for i in lista :
#     soma += i
#     print(f"Número atual: {i} | Soma acumulada até agora: {soma}")
# print(f"\nA soma total dos elementos é: {soma}")

#Exercicio 4.2 filtro de nomes com append: Crie lista com 5 nomes, crie uma segunda lista vazia e usando o if, adicione nessa segunda lista apenas os nomes que começam com a letra "A".

# lista_nomes = ["Antonio", "Abel", "Anilton" , "Abner", "Romário"]
# nomes_com_a = []

# for nome in lista_nomes:
#     if nome.startswith("A"):
#         nomes_com_a.append(nome)

# print(nomes_com_a)

#Exercicio 4.3: Cadastro e atualização de produto (dicionario), crie um dicionario para um produto com as chaves nome preco estoque, peça ao usuario um novo valor para o estoque e atualize o dicionário.

#Criar dict
produto = {
    "nome": "Caderno",
    "preco": 22.50,
    "estoque": 15
}

print (f"Estoque antigo: {produto['estoque']}")

novo_estoque = int(input("Dignte o novo valor para estoque: "))

produto["estoque"] = novo_estoque

# Exibindo os dados atualizados
print("\n--- Dados Atualizados do Produto ---")
print(f"Nome: {produto['nome']}")
print(f"Preço: R$ {produto['preco']:.2f}")
print(f"Estoque atualizado: {produto['estoque']}")

#Exercicio 4.4 remoção de duplicatas
#Lista com numero repetido, converter em conjunto set e continuar rodando a lista sem duplicadas.

lista_boa = [1, 2, 2, 3, 4, 4, 5]