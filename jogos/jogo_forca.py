import random

def jogar():

	imprimir_msg_abertura()

	palavra_secreta = definir_palavra_secreta()

	letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
	print(letras_acertadas)

	enforcou = False # variaveis responsaveis por coordenar a dinamica do jogo
	acertou = False
	erros = 0

	while(not enforcou and not acertou): # o jogo continua ate que o jogador perca todas as suas chances ou acerte

		chute = pede_chute()

		index = 0	# define um indice como zero para contar a quantidade de tentativas

		if(chute in palavra_secreta): # i.e. se o chute for acertado

			chutou_corretamente(chute, letras_acertadas, palavra_secreta)
		else:
			erros += 1	
			desenha_forca(erros)
			print("Voce errou! Faltam {} tentativas".format(6 - erros))

		enforcou = (erros == 7) # bool que verifica se o jogador ja errou 6 vezes (numero maximo)
		acertou = ("_" not in letras_acertadas) # se a string que inicialmente coloca "_" correspondentes ao numero de letras nao possuir
												# mais nenhum "_" isso significa que o usuario acertou todas as letras
		print(letras_acertadas)


	if(enforcou):
		imprime_msg_perdedor(palavra_secreta)
	elif(acertou):
		imprime_msg_ganhador()



def imprimir_msg_abertura():
	print("\n*********************************")
	print("***Bem vindo ao jogo da Forca!***")
	print("*********************************\n")


def definir_palavra_secreta():
	arquivo = open("palavras.txt", "r")
	palavras_secretas[]

	for linha in arquivo:
		linha = linha.strip()
		palavras_secretas.append(linha)

	arquivo.close()

	numero = random.randrange(0, len(palavras_secretas)) # gera um indice aleatorio de 0 ate o numero de palavras na lista de
														# palavras secretas

	palavra_secreta = palavras_secretas.[numero].upper()

	return palavra_secreta


def inicializar_letras_acertadas(palavra_secreta):
	return ["_" for letra in palavra_secreta] 


def pede_chute():
	chute = input("Chute uma letra:")
	chute = chute.strip().upper() # remove possiveis espacos no inicio ou fim do chute e converte o chute para letra maiuscula
	return chute


def chutou_corretamente(chute, letras_acertadas, palavra_secreta):
	for letra in palavra_secreta:
		if(chute == letra):
			letras_acertadas[index] = letra								
		index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_msg_perdedor(palavra_secreta):
	def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_msg_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


if(__name__ == "__main__"):
	jogar()
