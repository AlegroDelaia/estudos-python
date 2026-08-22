#AULA 1 - REVISÃO - EXERCÍCIOS
#EXERCICIO 1 - Peça ao usuário uma temperatura em graus Celsius (float).
# Regra: Converta essa temperatura para Fahrenheit usando a fórmula: F = (C x 1.8) + 32 .
# Saída: Exiba uma mensagem usando f-string: "X°C equivalem a Y°F".
##EXERCICIO 2 - Exercício 1.2: Calculadora de Média e Aprovação Simples 
# Objetivo: Peça duas notas ao usuário (use float).
# Regra: Calcule a média simples das duas notas e exiba uma frase informando a média final e se o valor é maior ou igual a 6.0 (bool).


#Pedir o número ao usuário
celsius = float(input("Digite a temperatura em graus Celsius: "))

#Calcular a temperatura em Fahrenheit
fahrenheit = (celsius * 1.8) + 32

#Exibir o resultado usando f-string
print(f"{celsius}°C equivalem a {fahrenheit}°F")

#EXERCICIO 2 - Calculadora de Média e Aprovação Simples
#Pedir as notas ao usuário

nota_1 = float(input("Digite a nota da prova 1: "))
nota_2 = float(input("Digite a nota da prova 2: "))

#Calcular a média das 2 notas
resultado = (nota_1 + nota_2) / 2

#mostrar o resultado da média final
print(f"Sua média final é: {resultado}")
if resultado >= 6.0:
#Informar se é maior ou igual a 6.0
    print(f"Sua média final é maior ou igual a 6.0")
