def jogar():

	print("\n*********************************")
	print("***Bem vindo ao jogo da Forca!***")
	print("*********************************\n")

	palavra_secreta = "banana".upper()

	letras_acertadas = ["_" for letra in palavra_secreta] 

	enforcou = False
	acertou = False
	erros = 0

	print(letras_acertadas)

	while(not enforcou and not acertou): 	# o jogo continua ate que o jogador perca todas as suas chances ou acerte

		chute = input("Chute uma letra:")
		chute = chute.strip().upper() # remove possiveis espacos no inicio ou fim do chute e converte o chute para letra maiuscula

		index = 0	# define um indice como zero para contar a quantidade de tentativas

		if(chute in palavra_secreta): # i.e. se o chute for acertado

			for letra in palavra_secreta:
				if(chute == letra):
					letras_acertadas[index] = letra								
				index += 1

		else:
			erros += 1	
			print("Voce errou! Faltam {} tentativas".format(6 - erros))

		enforcou = (erros == 6) # bool que verifica se o jogador ja errou 6 vezes (numero maximo)
		acertou = ("_" not in letras_acertadas) # se a string que inicialmente coloca "_" correspondentes ao numero de letras nao possuir
												# mais nenhum "_" isso significa que o usuario acertou, entao, todas as letras
		print(letras_acertadas)


	if(enforcou):
		print("Voce perdeu!")
	elif(acertou):
		print("Voce ganhou!")

	print("Fim do jogo!")

if(__name__ == "__main__"):
	jogar()
