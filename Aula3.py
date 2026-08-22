# Tema 3: Laços de Repetição (for e while)
# Exercício 3.1: Soma de Números com while
# Objetivo: Crie um programa que fique pedindo para o usuário digitar números inteiros.
# Regra: O programa deve somar todos os números digitados e só parar quando o usuário digitar 0. No final, exiba o total acumulado.

# Exercício 3.2: Contagem Regressiva com for
# Objetivo: Use o laço for e a função range() para fazer uma contagem regressiva de 10 até 1.
# Saída: A cada número exibido, mostre no terminal (ex: 10, 9... 1). No final (fora do loop), exiba: "Decolagem! 🚀".
# (Dica: Lembre-se que o range(inicio, fim, passo) aceita um terceiro parâmetro negativo para contar de trás para frente!)

#Ex3.1: Somatório de números inteiros.
#Variavel soma e numero digitado

soma = 0
numero_digitado = ""

#Funçao while
while numero_digitado != 0:
    numero_digitado = int(input("Digite um número para somar com o próximo até que você se canse e digite 0: "))
    soma += numero_digitado
    print(f"Somatório atual: {soma}")

print(f"Fim do somatório, o resultado da soma é {soma}")

#Ex.3.2: Contagem regressiva com for

#Funçao for, contagem regressiva (lembrando do passo = -1) range(inicio, fim, passo)
for contagem in range(10,0,-1):
    print(f"Faltam:{contagem}s, para decolar")
print("Decolagem!🚀👩‍🚀") #OBS USEI (win + .) para selecionar o emoji, não estou copiando e colando respostas kkkk

