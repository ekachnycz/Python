#find port from arduino ide

#bobo
esptool.py --port /dev/cu.usbserial-1410 erase_flash
esptool.py --port /dev/cu.usbserial-1410 --baud 115200 write_flash --flash_size=detect 0 ESP8266_GENERIC-20240222-v1.22.2.bin

mpfshell -c "open cu.usbserial-1410; put main.py"

screen /dev/cu.usbserial-1410 115200

#upload scripts:
#https://github.com/wendlers/mpfshell
    mpfshell -c "open cu.usbserial-1420; put boot.py; put main.py"

#for REPL
    screen /dev/cu.usbserial-1420 115200
    screen /dev/cu.usbmodem-14101 115200



