#Exercicio5.1 Crie uma função chamada saudar(nome) que recebe um nome como parâmetro e exibe a mensagem "olá, [nome]! Seja bem-vindo(a)"

#Definir função com parâmetro nome:

def saudar(nome):
    print(f"Olá {nome} ! Seja bem-vindo(a).")

#Pedir nome ao usuario
nome_usuario = input("Digite seu nome: ")

#Chamar a função e passar o nome q o usuario escolheu.
saudar(nome_usuario)

#Exercicio 5.2 criar função chamada somar(a,b) q recebe dois números, retorna a soma deles usando return, e exiba o resultado retornado no terminal.

#Criar a função com o retorno da soma:

def somar(a, b):
    return a + b

#Pedir valor de a e b ao usuario:
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

#Criar uma variavel para receber o resultado da função.

resultado = somar(a, b)

#Mostrar o valor da soma.

print(f"A soma de {a} + {b} é igual a {resultado}")

#Exercicio5.3 criar função chamada eh_par(numero) que recebe um numero inteiro e retorna true se par e false se impar.

#Criar função e o retorno.
def eh_par(numero):
    return numero % 2 == 0

numero = int(input("Digite um número pra saber se é par: "))

print(eh_par(numero))

#Exercicio 5.4 criar função calcular_area_retangulo(largura,altura) que retorna a area de um triangulo, teste a função chamando-a com diferentes valores:

#Criar a função para calcular area. lado x lado
def calcular_area_retangulo(largura, altura):
    return largura * altura
#pedir valores para calcular
largura = float(input("Digite a largura do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))

resultado = calcular_area_retangulo(largura, altura)

print(f"A área do retangulo de lados {largura} e {altura} é igual a {resultado:.2f}!")

#Exercicio 5.5 criar função chamada potencia(base,expoente=2) que calcula a potência de um número, se o expoente não for informado na chamada ela deve elevar o número ao quadrado por padrão.

def potencia(base, expoente=2):
    return base ** expoente

resultado_sem_expoente = potencia(5)
print(f"5 elevado ao quadrado é : {resultado_sem_expoente}")

resultado_normal = potencia(2,3)
print(f"2 elevado a 3: {resultado_normal}")

base = float(input("Digite o valor da base: "))
expoente = (input("Digite o valor do expoente ou aperte enter: "))

if expoente == "":
    print(f"Resultado: {potencia(base)}")
else:
    print(f"Resultado: {potencia(base, float(expoente))}")
