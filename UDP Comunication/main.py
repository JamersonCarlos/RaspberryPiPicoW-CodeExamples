from machine import I2C, Pin, PWM
import network
import socket 
from pico_i2c_lcd import I2cLcd
from random import randint
import authentication as autenticar
import time
from keypad import KeyPad
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=10000)
keyPad = KeyPad(15,14,13,12,11,10,7,6)
 
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.putstr("UABJ-UFRPE")
lcd.backlight_on() #Liga luz de iluminação
lcd.blink_cursor_off() #Mostra o cursor 	

port=10086
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('NameNet', 'password')
while(wlan.isconnected() == False):
    time.sleep(1)
ip = wlan.ifconfig()[0]
print(ip)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
s.bind((ip,port))
print('waiting....')

while True:
    data,addr = s.recvfrom(1024)
    s.sendto(data,addr)
    lcd.clear()
    lcd.putstr(str(data).split("'")[1])
    
    
    


