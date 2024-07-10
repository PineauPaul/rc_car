import sys
import RPi.GPIO as GPIO
import time
import numpy as np

class Servo():
    def __init__(self, servo_pin):
        self.servo_pin = servo_pin
        self.frequency = 50
        self.is_init = False
    def init_servo(self):
        print("Initializing servomotor")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        GPIO.setwarnings(False)
        p = GPIO.PWM(self.servo_pin, self.frequency)  # GPIO 17 for PWM with 50Hz
        p.start(2.5)  # Initialization
        self.is_init = True
        self.servo = p

    def send_angle_to_servo(self, angle):
        if(not self.is_init):
            print("Servo not initialized, do it now")
            self.init_servo()
            return

        if (abs(angle) > 45):
            angle = np.sign(angle) * 45
            print('max angle is 45 degrée')

        angle = ((angle - 45) / (-45 - 45)) * 8 + 3
        self.servo.ChangeDutyCycle(angle)
        time.sleep(0.5)


if __name__ == "__main__":
    ser = Servo(17)
    ser.init_servo()
    angles_list = [-45,-20,0,25,40]
    for angle in angles_list:
        ser.send_angle_to_servo(angle)
