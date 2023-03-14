import time
import dht11
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=10000)
 
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.putstr("BEM VINDO")
lcd.move_to(0,1)
lcd.putstr("UABJ-UFRPE")
lcd.backlight_on() #Liga luz de iluminação
lcd.blink_cursor_off() #Mostra o cursor 	

temperatura = 0
umidade = 0 

#Setando o pino de transferência de dados
dht =  dht11.DHT11(16)
time.sleep(1)
dht.measure()
lcd.clear()

while True:
    temperatura = dht.temperature()
    umidade = dht.humidity()
    lcd.move_to(0, 0)
    lcd.putstr("Temp: ")
    lcd.putstr(str(temperatura))
    lcd.putstr("C")
    lcd.move_to(0, 1)
    lcd.putstr("Humi: ")
    lcd.putstr(str(umidade))
    lcd.putstr("%")
    time.sleep(1)
    lcd.clear()