import RPi.GPIO as GPIO
import sys

# Configuraciones
FAN_PIN = 21    # Pin BCM utilizado
PWM_FREQ = 30   # [Hz] 

# Setup GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)

fan=GPIO.PWM(FAN_PIN,PWM_FREQ)
fan.start(0);
i = 0

try:
    while 1:
        fanSpeed=float(input("Velocidad del cooler: "))
        fan.ChangeDutyCycle(fanSpeed)

# Si el programa se interrumpe (ctrl + c), el GPIO se establece en 0 y el programa sale
except(KeyboardInterrupt):
    print("Control interrumpido por teclado")
    GPIO.cleanup()
    sys.exit()
    
