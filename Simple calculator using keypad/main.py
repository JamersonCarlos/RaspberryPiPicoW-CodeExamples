from keypad import KeyPad
from machine import Pin
import time
import os


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
    print("Enter first number: ", end=" ")
    while breakValue == 0:
        keyvalue = keypad.scan()
        if(keyvalue != None):
            blinkLedDigit()
            if keyvalue == 'A':
                if(operand1):
                    breakValue = 1
                    time.sleep_ms(300)
            elif (keyvalue in listValidValues):
                print(keyvalue, end="")
                operand1.append(str(keyvalue))
                time.sleep_ms(300)
    print()
    print("Enter second number: ", end=" ")
    while breakValue == 1:
        keyvalue = keypad.scan()
        if(keyvalue != None):
            blinkLedDigit()
            if(keyvalue == "A"):
                if(operand2):
                    breakValue = 0
                    time.sleep_ms(300)
            elif (keyvalue in listValidValues):
                print(keyvalue, end="")
                operand2.append(str(keyvalue))
                time.sleep_ms(300)
    
    print()
    printOperations()
    print()
    print("Set Operation: ", end = "")
    while breakValue == 0:
        keyvalue = keypad.scan()
        if(keyvalue != None):
            if(int(keyvalue) >= 1 and int(keyvalue) <= 4):
                print("(" + keyvalue , end=")")
                setOperation = int(keyvalue)
                breakValue = 1
                time.sleep_ms(300)
    print()
    operand1 = int(''.join(map(str, operand1)))
    operand2 = int(''.join(map(str, operand2)))
    print(f"{operand1} {returnOperator(setOperation)} {operand2} = {calculateResult(setOperation, operand1, operand2)}\n")
    print("stop calculation (1 = Yes, 0 = Not): ", end = "")
    
    while breakValue == 1:
        keyvalue = keypad.scan()
        if(keyvalue != None):
            if (int(keyvalue) == 0):
                print(keyvalue)
                breakValue = 0
                time.sleep_ms(300)
                print("\n\n\n")
            elif (int(keyvalue) == 1):
                print(keyvalue)
                breakValue = 0
                time.sleep_ms(300)
    
    if(keyvalue == 1):
        print("End Calculator!!!")
        break
    print("\n\n\n\n")
    operand1 = []
    operand2 = []
    setOperation = 0
    
        
            

    
    



