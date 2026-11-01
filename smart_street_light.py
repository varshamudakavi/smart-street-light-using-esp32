import machine
import time

Define constants

LDR_PIN = 21  # Pin for LDR sensor

IR_PIN1 = 15  # Pin for IR sensor 1
IR_PIN2 = 23  # Pin for IR sensor 2
IR_PIN3 = 4  # Pin for IR sensor 3

LED_PIN1 = 5  # Pin for external LED 1
LED_PIN2 = 19  # Pin for external LED 2
LED_PIN3 = 22  # Pin for external LED 3

Set up pin directions

ldr = machine.Pin(LDR_PIN, machine.Pin.IN)

ir1 = machine.Pin(IR_PIN1, machine.Pin.IN)
ir2 = machine.Pin(IR_PIN2, machine.Pin.IN)
ir3 = machine.Pin(IR_PIN3, machine.Pin.IN)

led1 = machine.Pin(LED_PIN1, machine.Pin.OUT)
led2 = machine.Pin(LED_PIN2, machine.Pin.OUT)
led3 = machine.Pin(LED_PIN3, machine.Pin.OUT)

try:
while True:
# Read LDR sensor value (1 = dark, 0 = light)
ldr_value = ldr.value()

# Read IR sensor values (0 = no object, 1 = object detected)  
    ir_value1 = ir1.value()  
    ir_value2 = ir2.value()  
    ir_value3 = ir3.value()  

    print(f"LDR Value: {ldr_value}")  
    print(f"IR 1 Value: {ir_value1}")  
    print(f"IR 2 Value: {ir_value2}")  
    print(f"IR 3 Value: {ir_value3}")  

    # Turn on LEDs  
    if ldr_value == 1:  
        if ir_value1 == 0:  
            led1.value(1)  
            print("LED 1 turned on")  
        else:  
            led1.value(0)  
            print("LED 1 turned off")  

        if ir_value2 == 0:  
            led2.value(1)  
            print("LED 2 turned on")  
        else:  
            led2.value(0)  
            print("LED 2 turned off")  

        if ir_value3 == 0:  
            led3.value(1)  
            print("LED 3 turned on")  
        else:  
            led3.value(0)  
            print("LED 3 turned off")  
    else:  
        led1.value(0)  
        led2.value(0)  
        led3.value(0)  
        print("All LEDs turned off")  

    # Wait for 0.5 seconds before checking again  
    time.sleep(0.5)

except KeyboardInterrupt:
# Clean up
print("Exiting program.")