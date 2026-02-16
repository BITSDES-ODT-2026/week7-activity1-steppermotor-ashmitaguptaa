from machine import Pin
import time

in1 = Pin(5,Pin.OUT)
in2 = Pin(14,Pin.OUT)
in3 = Pin(18,Pin.OUT)
in4 = Pin(19,Pin.OUT)

seq = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    for i in seq:
        print(i)
        in1.value(i[0])
        in2.value(i[1])
        in3.value(i[2])
        in4.value(i[3])
        
        time.sleep_ms(5)
