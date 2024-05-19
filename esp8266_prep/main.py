from machine import Pin, ADC, PWM
import utime

servo_1_pin = Pin(5)
servo_2_pin = Pin(4)

x_axis = ADC(Pin(13))
y_axis = ADC(Pin(12))
button = Pin(14,Pin.IN, Pin.PULL_UP)


def yaw_left():
    servo_L = PWM(servo_1_pin, freq = 50)
    servo_L.duty_u16(6000)
    utime.sleep(.5)
    servo_L.duty_u16(2000)
    utime.sleep(2)
    servo_L.deinit()


def yaw_right():
    servo_R = PWM(servo_2_pin, freq = 50)
    servo_R.duty_u16(6000)
    utime.sleep(.5)
    servo_R.duty_u16(2000)
    utime.sleep(2)
    servo_R.deinit()


while True:
    x_value = x_axis.read_u16()
    yValue = y_axis.read_u16()
    buttonValue= button.value()
    if x_value is not None: 
        

    utime.sleep(0.1)

