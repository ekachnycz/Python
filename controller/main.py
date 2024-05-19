from machine import Pin, ADC
import utime


#joystick requires 2 adc inputs. ESP8266 only has 1 input, pico has 3. 
x_axis = ADC(0)
y_axis = ADC(1)

button = Pin(14,Pin.IN, Pin.PULL_UP)

while True:
    #for ESP32/8266
    #x_axis.read() #results from 0 to 1024
    #y_axis.read() #results from 0 to 1024

    #for rpi pico
    x_val = x_axis.read_u16() #results from 0 to 65535
    y_val = y_axis.read_u16() #results from 0 to 65535
    buttonValue= button.value()
    print(f"X: {x_val} Y:{y_val} Button:{buttonValue}")
    utime.sleep(0.1)
