import sys
import RPi.GPIO as GPIO
import time
import numpy as np

def init_servo(servoPin,hz=50):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPin, GPIO.OUT)
    GPIO.setwarnings(False)
    p = GPIO.PWM(servoPin, hz)  # GPIO 17 for PWM with 50Hz
    p.start(2.5)  # Initialization
    return p

def send_angle_to_servo(servo, angle):
    if(abs(angle) > 45):
        angle = np.sign(angle)*45
        print('max angle is 45 degrée')

    angle = ((angle - 45) / (-45-45))*8 + 3
    servo.ChangeDutyCycle(angle)
    time.sleep(0.5)



if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Usage python servo.py angle (degree)")
        sys.exit(1)
    servo = init_servo(17)
    send_angle_to_servo(servo,float(sys.argv[1]))
    servo.stop()
    GPIO.setup(17, GPIO.OUT)
