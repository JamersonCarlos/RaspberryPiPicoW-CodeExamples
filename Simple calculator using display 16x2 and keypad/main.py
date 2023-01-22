from keypad import KeyPad
from machine import Pin
import time
import os
from machine import I2C, Pin, PWM
from pico_i2c_lcd import I2CLcd

i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=10000)
I2C_ADDR = i2c.scan()[0]
lcd = I2CLcd(i2c, I2C_ADDR, 2, 16)


ledSetValue = Pin(14, Pin.OUT)
keypad = KeyPad(13,12,11,10,9,8,7,6)
listValidValues = ["1","2","3","4","5","6","7","8","9","0","A"]
setOperation = 0
breakValue = 0
keyvalue = ''
keyvalue2 = ''
operand1 = []
operand2 = []


def blinkLedDigit():
    ledSetValue.value(1)
    time.sleep_ms(300)
    ledSetValue.value(0)
    
def printOperations():
    print("Adition        (1)")
    print("Multiplication (2)")
    print("Subtraction    (3)")
    print("Division       (4)")

def calculateResult(operation, x, y):
    if operation == 1: 
        return x + y
    elif operation == 2:
        return x * y
    elif operation == 3:
        return x - y
    elif operation == 4:
        return x / y
    else:
        return False

def returnOperator(operation):
    if operation == 1: 
        return "+"
    elif operation == 2:
        return "*"
    elif operation == 3:
        return "-"
    elif operation == 4:
        return "/"


    
while True:
    stopEnd = 0
    lcd.putstr("number 1: ")
    while breakValue == 0:
        keyvalue = keypad.scan()
        if(keyvalue != None):
            blinkLedDigit()
            if keyvalue == 'A':
                if(operand1):
                    breakValue = 1
                    time.sleep_ms(300)
            elif (keyvalue in listValidValues):
                lcd.putstr(keyvalue)
                operand1.append(str(keyvalue))
                time.sleep_ms(300)
    lcd.move_to(0,1)
    lcd.putstr("number 2: ")
    while breakValue == 1:
        keyvalue = keypad.scan()
        if(keyvalue != None):
            blinkLedDigit()
            if(keyvalue == "A"):
                if(operand2):
                    breakValue = 0
                    time.sleep_ms(300)
            elif (keyvalue in listValidValues):
                lcd.putstr(keyvalue)
                operand2.append(str(keyvalue))
                time.sleep_ms(300)
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("add(1) multi(2)")
    lcd.move_to(0,1)
    lcd.putstr("sub(3) divis(4)")
    time.sleep(5)
    lcd.clear()
    lcd.putstr("+ 1 * 2 - 3 / 4")
    lcd.move_to(0,1)
    lcd.putstr("Set operation: ")
    while breakValue == 0:
        keyvalue = keypad.scan()
        if(keyvalue != None):
            if(int(keyvalue) >= 1 and int(keyvalue) <= 4):
                lcd.putstr(keyvalue)
                setOperation = int(keyvalue)
                breakValue = 1
                time.sleep_ms(300)
                
    operand1 = int(''.join(map(str, operand1)))
    operand2 = int(''.join(map(str, operand2)))
    lcd.clear()
    lcd.putstr(f"{operand1} {returnOperator(setOperation)} {operand2} = {calculateResult(setOperation, operand1, operand2)}\n")
    lcd.move_to(0,1)
    lcd.putstr("success!")
    time.sleep(5)
    lcd.clear()
    lcd.move_to(0,0)
    operand1 = []
    operand2 = []
    setOperation = 0
    
        
            

    
    



