import time
import pigpio

ESC_PIN = 18  # GPIO pin connected to the ESC signal wire
MAX_SPEED = 2000
MIN_SPEED = 1000
ZERO_SPEED = 1500


pi = pigpio.pi()
if not pi.connected:
    exit()

# Function to send a PWM signal to the ESC
def set_speed(speed):
    #speed is between -100 and + 100
    if(abs(speed) > 100):
        print("cannot set this speed")
        return

    pulse_speed = 1500 + (speed*500)/100
    if(pulse_speed > MAX_SPEED or pulse_speed < MIN_SPEED):
        print("Error while compute pulse_speed", pulse_speed, speed)

    pi.set_servo_pulsewidth(ESC_PIN, pulse_speed)
    print(f"Speed set to: {speed}")

# Initialize the ESC
pi.set_servo_pulsewidth(ESC_PIN, 0)  # Send a neutral signal to initialize
time.sleep(4)



# Testing PWM range
try:
    print("Setting speed to neutral...")
    set_speed(0)  # Neutral
    time.sleep(2)

    print("Setting speed to forward...")
    set_speed(30)  # Forward
    time.sleep(5)

    print("Setting speed to neutral...")
    set_speed(0)  # Neutral
    time.sleep(2)

    print("Setting speed to backward...")
    set_speed(-20)  # Backward
    time.sleep(5)

    print("Setting speed to neutral...")
    set_speed(0)  # Neutral
    time.sleep(2)

except KeyboardInterrupt:
    # Stop the motor on program exit
    set_speed(0)
    pi.stop()
