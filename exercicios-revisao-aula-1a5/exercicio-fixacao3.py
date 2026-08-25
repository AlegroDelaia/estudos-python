# #Exercicio 3.1 Classificador de números:
# #Criar um programa que classifica um numero como positivo, negativo ou zero.

#Pedir o número ao usuário.
numero = float(input("Digite um número para classificar-mos em, positivo, negativo ou zero: "))

if numero > 0:
    print(f"Seu número {numero}, é positivo")
elif numero < 0:
    print(f"Seu número {numero}, é negativo")
else:
    print("Esse é o zero!")

#Exercicio 3.2 Tabuada Automática:
#Peça um numero e retorne o valor da tabuada desse numero.

#Pedir número ao usuário.
numero = int(input("Digite um número e conheça sua tabuada: "))

for i in range(1,11):
    print(f"{numero} x {i} = {i*numero}")

#Exercicio 3.3 acumulador com while:
#Criar programa usando while, pedir numeros e somar todos, só parar ao digitar 0.

soma = 0
numero_escolhido = -1

while numero_escolhido != 0:
    numero_escolhido = int(input("Digite um número para somar infinitamente (ou 0 para encerrar): "))
    soma += numero_escolhido

    if numero_escolhido !=0:
        print(f"Soma atual: {soma}")

print(f"Esse é o zero, paramos por aqui. Soma final: {soma}")

#Exercicio 3.4 filtro de pares: use for e if para exibir no terminal apenas os números pares no intervalo de 1 a 30.

#Construir contagem for.

print("Esses são os números pares entre 1 e 30:")

for i in range(1,31):
    if i % 2 == 0:
        print(i)       #exibe resultados

#Exercicio 3.5 Validador de Empréstimo: Peça salário e valor de parcela, se a parcela for <= (30 / 100) * salário, exiba "Aprovado", do contrário "Negado".

#Solicitar salário e valor de parcela:

salario = float(input("Informe o valor do salário: "))
parcela = float(input("Informe o valor da parcela: "))

if parcela <= 30 * salario / 100:
    print("Aprovado")
else:
    print("Negado")