import pyfirmata 
import time




led = 13

try:
    port = "COM7"
    board = pyfirmata.Arduino(port)
    print("connected")
except:
    print("failed to connect")

while True:
   board.digital[led].write(1)
    
    

    