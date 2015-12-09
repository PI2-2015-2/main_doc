import RPi.GPIO as GPIO
import time

#tipo de enderecamento dos pinos do Raspberry Pi
GPIO.setmode(GPIO.BOARD)

TRIG = 13
ECHO = 15

GPIO.setup(TRIG,GPIO.OUT) # Configurando pino de saida
GPIO.setup(ECHO,GPIO.IN) # Configurando pino de entrada

GPIO.output(TRIG,0) # Iniciado em valor logico BAIXO

while 1 # Leitura constante da distancia
  time.sleep(0.1) # Delay de seguranca

  GPIO.output(TRIG,1) # Emite pulso
  time.sleep(0.00001) # Espera de 10ms(tempo do sensor HC-RS04)
  GPIO.output(TRIG,0) 

  while GPIO.input(ECHO) == 0 # Espera do pulso emitido
    pass
  inicio = time.time()

  while GPIO.input(ECHO) == 1
    pass
  parada = time.time()

  # Distancia do objeto em centimetros
  print (parada - inicio)*17000

GPIO.cleanup()
