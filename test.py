from machine import Pin
from time import sleep

relay = Pin(26, Pin.OUT) # GPIO18

while True:
    relay.value(0) # Relay ON
    print("Relay ON")
    sleep(2)
    
    relay.value(1) # Relay OFF
    print("Relay OFF")
    sleep(2)