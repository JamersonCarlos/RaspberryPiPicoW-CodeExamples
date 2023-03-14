import network
import socket
import time
import dht11

from machine import Pin, I2C

temperatura = '0'
umidade = '0'

dht = dht11.DHT11(15)
time.sleep(1)

# Configuração Inicial
led = Pin("LED", Pin.OUT)
html = """<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
        <meta http-equiv="refresh" content="10">
    </head>
    <body> 
        <h1>Monitor do sensor</h1>
        <p>Umidade: %s Temperatura: %s</p>
    </body>
</html>
"""
ssid = 'brisa-2397015'
password = 'wjbegznj'


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
print('listening on', addr)

while True:
    try:
        if dht.measure() == 0:
            print("Sensor Error")
        else:
            temperatura = str(dht.temperature())
            umidade = str(dht.humidity())
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print(request)
        response = html % (umidade, temperatura)
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        time.sleep(1)
    except OSError as e:
        cl.close()
        print('Close Conection')

