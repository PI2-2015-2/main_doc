import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) # Enderecamento dos pinos

Verm  = 11
Verde = 13
Azul  = 15

GPIO.setup(Verm,GPIO.OUT)	# Configurando pino de saida
GPIO.output(Verm,1)			# Desligado para o modelo "Catodo Comum"

GPIO.setup(Verde,GPIO.OUT)	# Configurando este pino como saida
GPIO.output(Verde,1)		# Desligado para o modelo "Catodo Comum"

GPIO.setup(Azul,GPIO.OUT)	# Configurando este pino como saida
GPIO.output(Azul,1)			# Desligado para o modelo "Catodo Comum"

# A variavel ind sera transmistida a partir do aplicativo junto de
# cada bloco de comando para entao configurar a cor correspondente 
ind = 0;

while(True):
# Neste exemplo ind=1 representa o bloco mova-se para frente,
# como exemplo atribui-se a cor verde para este bloco
# Serao utilizados no total um numero de tres Leds, todos em paralelo
	if ind = 1:
		Verm  = 1
		Verde = 0	
		Azul  = 1 
# Exemplo para um bloco de cor azul	
	elif ind = 2:
		Verm  = 1
		Verde = 1	
		Azul  = 0
# Exemplo para um bloco da cor vermelha	
	elif ind = 3:
		Verm  = 0
		Verde = 1
		Azul  = 1
 		
GPIO.cleanup()	# reseta os pinos de GPIO e limpa a tela

