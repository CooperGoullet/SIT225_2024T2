import serial
import random
import time
from datetime import datetime

# Set the serial port and baud rate
baud_rate = 9600
s = serial.Serial('COM8', baud_rate, timeout=5)  # Change 'COM8' to the correct port for your system

def log_event(event):
    print(f"{datetime.now()}: {event}")

try:
    while True:
        # Send a random number between 1 and 5 to the Arduino
        data_send = random.randint(1, 5)
        s.write(bytes(f"{data_send}\n", 'utf-8'))
        log_event(f"Send >>> {data_send}")
        
        # Wait for the Arduino to respond with a number
        while s.inWaiting() == 0:
            pass
        
        data_received = s.readline().decode().strip()
        log_event(f"Received <<< {data_received}")
        
        # Sleep for the received number of seconds
        sleep_time = int(data_received)
        log_event(f"Sleeping for {sleep_time} seconds")
        time.sleep(sleep_time)
        log_event("Woke up from sleep")

except KeyboardInterrupt:
    log_event("Script interrupted by user")

finally:
    s.close()
    log_event("Closed serial connection")




