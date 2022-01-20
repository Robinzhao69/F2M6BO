import serial.tools.list_ports
import cv2
import time


def processGesture(gesture):
    print(gesture)
    # code



ports = serial.tools.list_ports.comports()

serialInst = serial.Serial()

# array met al mijn usb porten 
portList = []


for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))


# hier kan je de nummer van de COM poort kiezen
val = input("select Port: COM")
gesture = "" # global var

# zoekt in de port array de nummer die je als input heeft aangegeven en dan verbind het met die port
for x in range(0,len(portList)):
    
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

        serialInst.baudrate = 9600
        serialInst.port = portVar
        serialInst.open()

while True:
    gesture = ""
    if serialInst.in_waiting:
        packet = serialInst.readline()
       # print(packet.decode('utf'))
        gesture = packet.decode('utf')
        processGesture(gesture)

        
        


