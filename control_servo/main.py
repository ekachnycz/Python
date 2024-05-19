from machine import PWM, Pin, ADC
from servo import Servo
import utime

x_axis = ADC(0)
y_axis = ADC(1)

button = Pin(14,Pin.IN, Pin.PULL_UP)


def servo(x_val, y_val):
    x_servo_val = x_val * 15
    y_servo_val = y_val * 15
    x_servo = Servo(pin_id = 13)
    y_servo = Servo(pin_id = 14)
    x_servo.write(x_servo_val)
    y_servo.write(y_servo_val)

    
def fan(buttonValue):
    fan = Pin(15, machine.Pin.OUT)
    if buttonValue == 1:

        utime.sleep(.5)
        fan.low()
    



if __name__ == '__main__':
    while True:
        x_val = x_axis.read_u16() #results from 0 to 65535
        x_val = int(x_val * .00018311)
        y_val = y_axis.read_u16() #results from 0 to 65535
        y_val = int(y_val * .00018311)
        servo(x_val, y_val)
        buttonValue= button.value()
        #fan(buttonValue)
        print(f"X: {x_val} Y:{y_val} Button:{buttonValue}")