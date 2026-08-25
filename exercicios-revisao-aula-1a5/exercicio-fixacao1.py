#Exercicio 1.1 Mensagem personalizada:
#Criar variaveis, nome, idade, cidade natal.

nome = "Antonio"
idade = 31
cidade_natal = "Vitória"

#Exibir texto.
print(f"Olá, {nome}, você tem {idade} anos e mora em {cidade_natal}!")

#Exercicio 1.2 Conversor de idade.
#Utilize a variavel idade acima e calcule a quantidade aproximada de dias que você já viveu (considere 1 ano = 365 dias)

dias_vividos = idade * 365

#Exibir texto em dias.

print(f"Você tem {idade} anos, por isso já viveu {dias_vividos} dias!")

#Exercicio 1.3 Tipos de Dados.
#Crie quatro variáveis com tipos diferentes e exiba no terminal o valor e o tipo de cada uma usando a função type().

nome = "Fernando"
idade = 40
altura = 1.75
masculino = True

print(nome)
print(type('Fernando')) 
print(idade)
print(type(40))
print(altura)
print(type(1.75))
print(masculino)
print(type(True))

#Exercicio 1.4 Calculadora de Desconto:
#Criando Variavel de preço, produto.

preco_o = 150.0
desconto_percentual = 15
preco_f = preco_o - preco_o * desconto_percentual / 100

print(f"Se o produto custa {preco_o} e o desconto é de {desconto_percentual} %, então o valor final será de R$ {preco_f}!")

#Exercicio 1.5 Troca de Variáveis:
#Criar 2 váriaveis e trocar seus valores.

a = 5
b = 10

#Trocar no modo python,sempre utilziar esse, pois o meu código principal será python, mas teria como utilizar o "temp = a | a = b | b = temp" .
a, b = b, a

print(f"a: {a} , b: {b}")

