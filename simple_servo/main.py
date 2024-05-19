#mpfshell -c "open cu.usbserial-1420; put main.py"



from machine import PWM, Pin
import utime

#https://lastminuteengineers.com/esp8266-pinout-reference/
#https://www.kevsrobots.com/learn/micropython_gpio/14_servos.html
servo = PWM(Pin(14))
servo.freq(50)

#servo minimum position
servo.duty_u16(2000)
utime.sleep(2)

#servo mid position
servo.duty_u16(6000)
utime.sleep(2)

#servo max position
servo.duty_u16(12000)
utime.sleep(2)

servo.deinit()