import RPi.GPIO as GPIO
import time     #para medir quanto tempo o pino esta em nivel logico ALTO

GPIO.setmode(GPIO.BOARD) #tipo de enderecamento dos pinos do Raspberry Pi

TRIG = 13
ECHO = 15

GPIO.setup(TRIG,GPIO.OUT) #configurando este pino como saida
GPIO.output(TRIG,0) # certificando de que e iniciado em valor logico BAIXO

GPIO.setup(ECHO,GPIO.IN) #configurando o pino ECHO como entrada

while 1       # para que o programa continue lendo as distancias enquanto o programa estiver executando
  time.sleep(0.1) #atraso para certificacao do bom funcionamento do sensor

  GPIO.output(TRIG,1) #emite o pulso
  time.sleep(0.00001) #espera de 10ms(tempo de do sensor HC-RS04)
  GPIO.output(TRIG,0) 

  while GPIO.input(ECHO) == 0; # o while-loop vai esperar ate o recebimento do pulso emitido
    pass
  inicio = time.time()  #esta funcionamento le o tempo e guarda o valor na variavel
        # expressa o tempo atual em segundos

  while GPIO.input(ECHO) == 1; # o tempo final guardado e aquele quando o
    pass     # pino ECHO recebe o pulso de volta e esta em nivel logico ALTO
  parada = time.time()

  print (parada - inicio)*17000 # distancia Do objeto em centimetros

GPIO.cleanup()  # reseta os pinos de GPIO e limpa a tela
