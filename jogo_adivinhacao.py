import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)

print("Qual o nivel de dificuldade?")
print("(1) Facil \n(2) Medio \n(3) Dificil\n")

nivel = int(input("Defina o nivel: "))

total_de_rodadas = 0
rodada_atual = 1
pontos = 1000

if(nivel == 1):
	total_de_rodadas = 20
elif(nivel == 2):
	total_de_rodadas = 10
elif(nivel == 3):
	total_de_rodadas = 5	

for rodada_atual in range(1, (total_de_rodadas + 1)):

	chute = int(input("Digite um número entre 1 e 100: ")) # a funcao input sempre gera uma entrada do tipo string
												# como vamos comparar com um número inteiro, precisamos
												# fazer a conversao para que o programa funcione

	print("Rodada {} de {}".format(rodada_atual,str(total_de_rodadas)))

	rodada_atual = rodada_atual + 1

	acertou = (chute == numero_secreto)
	maior   = chute > numero_secreto
	menor   = chute < numero_secreto


	if(chute < 1 or chute > 100):
		rodada_atual = (rodada_atual - 1) # como o numero eh invalido, a rodada nao eh utilizada
		print("Digite um numero entre 1 e 100!")
		continue


	if(acertou):
		print("Voce acertou! O número secreto era: ", numero_secreto)
		print("Sua pontuacao: {} pontos".format(pontos))
		break # se acertou, entao o jogo acabou
	else:
		pontos_perdidos = abs(numero_secreto - chute)
		pontos -= pontos_perdidos	
		if(maior):
			print("Voce errou! O chute foi maior do que o número secreto")
		elif(menor):
			print("Voce errou! O chute foi menor do que o número secreto")



print("Fim do jogo!")