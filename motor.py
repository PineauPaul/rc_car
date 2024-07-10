import time
import pigpio

class Motor():
    def __init__(self, esc_pin = 18):
        self.max_speed = 2000
        self.min_speed = 1000
        self.zero_speed = 1500
        self.esc_pin = esc_pin
        self.pi_gpio = pi = pigpio.pi()


    def __del__(self):
        self.set_speed(0)
        self.pi_gpio.stop()
    def initialise_esc(self):
        if(self.pi_gpio.connected):
            self.pi_gpio.set_servo_pulsewidth(self.esc_pin, 0)  # Send a neutral signal to initialize
            time.sleep(4)
        else:
            print("esc not connected")

    def set_speed(self, speed):
        # speed is between -100 and + 100
        if(not self.pi_gpio.connected):
            print("esc not connected")
            return

        if (abs(speed) > 100):
            print("cannot set this speed")
            return

        pulse_speed = 1500 + (speed * 500) / 100
        if (pulse_speed > self.max_speed or pulse_speed < self.min_speed):
            print("Error while compute pulse_speed", pulse_speed, speed)

        self.pi_gpio.set_servo_pulsewidth(self.esc_pin, pulse_speed)
        print(f"Speed set to: {speed}")

    def set_esc_pin(self, pin):
        self.esc_pin = pin

    def set_max_speed(self, speed):
        self.max_speed = speed

    def set_min_speed(self, speed):
        self.min_speed = speed

    def set_zero_speed(self, speed):
        self.zero_speed = speed


if __name__=="__main__":
    motor = Motor()

    # Testing PWM range
    print("Setting speed to neutral...")
    motor.set_speed(0)  # Neutral
    time.sleep(2)

    print("Setting speed to forward...")
    motor.set_speed(30)  # Forward
    time.sleep(5)

    print("Setting speed to neutral...")
    motor.set_speed(0)  # Neutral
    time.sleep(2)

    print("Setting speed to backward...")
    motor.set_speed(-20)  # Backward
    time.sleep(5)

    print("Setting speed to neutral...")
    motor.set_speed(0)  # Neutral
    time.sleep(2)