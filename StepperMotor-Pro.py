from machine import Pin
import time

in1 = Pin(5,Pin.OUT)
in2 = Pin(14,Pin.OUT)
in3 = Pin(18,Pin.OUT)
in4 = Pin(19,Pin.OUT)

seq = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
rev_seq = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

while True:
    for i in range(500):
        for s in seq:
            in1.value(s[0])
            in2.value(s[1])
            in3.value(s[2])
            in4.value(s[3])
            time.sleep_ms(5)
        
    for j in range(500):
        for k in rev_seq:
            in1.value(k[0])
            in2.value(k[1])
            in3.value(k[2])
            in4.value(k[3])
            time.sleep_ms(5)
