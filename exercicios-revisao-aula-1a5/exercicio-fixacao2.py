#Exercicio 2.1 Conversor de temperatura:
#Peça uma temperatura em Celsius(float). Converta para Fahrenheit, fórmula F=(C/1.8) + 32, exiba o resultado.

#Pedindo temperatura em C
c = float(input("Digite uma temperatura em Cº: "))
f = float((c*1.8) + 32)

#Exibir resultados
print(f"{c}º Celsius, equivale a {f:.2f} Fahrenheit !")

#Exercicio 2.2 Calculadora de média:
#Peça duas notas (float), calcule a média e exiba a média acompanhada de um valor booleano indicnado se a média é maior ou igual a 6.0

#pedindo notas.

nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))

media = (nota1 + nota2) / 2

if media > 6.0:
    print(f"Parabéns, sua média {media} é maior que 6.0!")
elif media == 6.0:
    print(f"Parabéns, sua média é {media} !")
else:
    print("Precisa melhorar!")

#Exercicio 2.3 Divistao inteira e Resto:
#Pedir 2 numeros inteiros, exebir resultado da divisão inteira e divisão resto entre eles.

#Pedir numeros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

print(f"A divisão inteira entre {numero1} e {numero2} é igual a {numero1 // numero2}!")

print(f"O resto da divisão entre {numero1} e {numero2} é {numero1 % numero2}!")

#Exercicio 2.4 calculadora de operadores logicos:
#Pedir idade, e se possui cnh(digite sim ou nao). Exibr True >= 18 e cnh (sim), ou False do contrário.

idade = int(input("Digite quantos anos você tem: "))
cnh = (input("Possui CNH? (digite sim ou nao)"))

if idade >=18 and cnh == str("sim"):
    print(True)
else:
    print(False)

#O CÓDIGO ANTERIOR FUNCIONA, MAS TEM MUITO MAIS INFORMAÇÃO DO QUE PRECISA ! PARA CONCERTAR ISSO, ELIMINE O IF ELSE, E COLOQUE AS CONDIÇÕES DIRETAMENTE DENTRO DO PRINT, OU SEJA PRINT(idade >= 18 and cnh == "sim"), desconsidere o str, JÁ QUE "SIM" JÁ É UMA STRING.

#Exercicio 2.5 Aumento Salarial:
#Peça o salario e a porcentagem de aumento, exiba o valor do aumento em reais e o novo salario ajustado.

#Pedir salario


salario = float(input("Fala praça, beleza!? Qual é o valor do seu salário atual? "))
aumento_p = float(input("Quantos % deveria ganhar de aumento? "))

reajuste_salario = salario + (salario * aumento_p) / 100

print(f"Seu salário atual é R${salario}, isso é pouco, você precisa de um aumento de pelo menos {aumento_p}%, com isso seu salário subiria para R${reajuste_salario:.2f}, o que acha?")