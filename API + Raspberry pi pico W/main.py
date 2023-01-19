import time
import dht11
import network
import urequests as requests
import ujson

dht = dht11.DHT11(15)
temp = 0
umid = 0

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('brisa-2397015', 'wjbegznj')
ip = wlan.ifconfig()[0]
dht.measure()

print ("Conectando...")
while True:
    if (not wlan.isconnected()):
        time.sleep(1)
    else:
        break
    

if wlan.isconnected(): 
    print ("Conectado")
    print("IP: "+wlan.ifconfig()[0])
    
while True:
    myobj = {'temperature': str(dht.temperature()), 'humidity': str(dht.humidity())}
    res = requests.post("https://apidata.herokuapp.com/codeJava/data-analysis", json = myobj)
    time.sleep(600)
