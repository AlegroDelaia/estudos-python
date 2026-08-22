# Tema 2: Estruturas Condicionais (if, elif, else)

# Exercício 2.1: Validador de Empréstimo 
# Objetivo: Peça o salário e o valor da parcela de um empréstimo (ambos float).
# Regras:Se a parcela for menor ou igual a 30% do salário (salario * 0.30), exiba: "Empréstimo Aprovado!".Caso contrário, exiba: "Empréstimo Negado: Parcela excede 30% do salário".

# Exercício 2.2: Calculadora de IMC (Índice de Massa Corporal)
# Objetivo: Peça o peso (kg) e a altura (m) de uma pessoa.
# Regra: Calcule IMC = {peso}/{altura^2} (Dica: altura ** 2).IMC < 18.5: Imprima "Abaixo do peso"18.5 <= IMC < 25.0: Imprima "Peso normal"IMC >= 25.0: Imprima "Sobrepeso"

#Exercicio 2.1 - Pedir o salario e o valor da parcela do emprestimo

salario = float(input("Digite qual é sua renda: "))
parcela = float(input("Digite qual o valor da parcela do seu empréstimo: "))

if parcela <= salario * 0.3:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado: parcela excede 30% do salário")    

#Exercicio 2.2: Calculadora de IMC.
#Pedir o peso (kg) e altura em (m) de uma pessoa.

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em m (utilize . e não ,): "))

#Calcular imc conforme exemplo do exercicio
imc = peso / (altura**2)

#Adicionar as condicionais para as variantes possiveis do resultado imc. #Cada print informará uma condição de imc, conforme solicitado.
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25.0:
    print("Peso ideal")
else:
    print("Sobre peso")