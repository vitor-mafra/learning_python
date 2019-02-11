import jogo_forca
import jogo_adivinhacao

def escolhe_jogo():

	print("*********************************")
	print("*******Escolha o seu jogo!*******")
	print("*********************************\n")

	print("(1) Forca\n(2) Adivinhacao")
	jogo = int(input("Digite o jogo que voce quer jogar: "))

	if(jogo == 1):
		print("\nJogando Forca!")
		jogo_forca.jogar()

	elif(jogo == 2):
		print("\nJogando Adivinhacao!")	
		jogo_adivinhacao.jogar()

if(__name__ == "__main__"):
	escolhe_jogo()