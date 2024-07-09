import RPi.GPIO as GPIO
from time import sleep

PIN_SERVO = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_SERVO, GPIO.OUT)

pwm = GPIO.PWM(PIN_SERVO, 50)  # Fréquence de PWM de 50 Hz

def set_servo_angle(angle):
    # Convertir l'angle en pourcentage de cycle de travail
    duty_cycle = 2.5 + (angle / 18.0)
    pwm.ChangeDutyCycle(duty_cycle)
    sleep(0.5)  # Laisser le servo-moteur atteindre la position

try:
    pwm.start(2.5)  # Position initiale

    while True:
        # Demander à l'utilisateur d'entrer l'angle du servo
        angle = float(input("Entrez l'angle du servo (0-180 degrés): "))
        
        # Limiter l'angle entre 0 et 180 degrés
        angle = max(0, min(angle, 180))

        set_servo_angle(angle)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup() 
