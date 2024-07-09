import RPi.GPIO as GPIO
import time

PIN_PWM = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_PWM, GPIO.OUT)

pwm = GPIO.PWM(PIN_PWM, 50)

def set_motor_speed(speed, reverse=False):
    duty_cycle = speed * 10

    if reverse:
        duty_cycle = 100 - duty_cycle  # Inverser le sens

    pwm.ChangeDutyCycle(duty_cycle)

try:
    pwm.start(100)  # Initialiser en envoyant un signal PWM au niveau maximal
    time.sleep(2)

    pwm.start(0)  # Arrêter le PWM pour revenir à l'état initial

    pwm.start(0)  # Redémarrer le PWM avec la configuration normale
    set_motor_speed(0)  # Arrêt du moteur
    time.sleep(2)

    set_motor_speed(50, reverse=True)  # Faire tourner le moteur à 50% en sens inverse
    time.sleep(5)

    set_motor_speed(100, reverse=True)  # Faire tourner le moteur à la vitesse maximale en sens inverse
    time.sleep(5)

    set_motor_speed(0)
    time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
