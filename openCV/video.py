import cv2
import time
from cv2 import add
import serial.tools.list_ports





valid_gestures = ["UP", "DOWN", "LEFT", "RIGHT"]



    
def gestures():  
    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            gesture = packet.decode('utf').strip("\r\n")
            if gesture in valid_gestures:       
                    processGesture(gesture)          
            else:
                print(gesture)



def een():
    input_video_path = 'd:/Ma/Bewijzenmap/leerjaar 2/periode 2/F2M6BO/openCV/video/zeemeermin1_v6.mp4'
    cap = cv2.VideoCapture(input_video_path)

    frame_counter = 0
    while(True):
        # dit zorgt ervoor dat ik de frames van de video een voor een pak
        ret, frame = cap.read()
        frame_counter += 1
        if serialInst.in_waiting:
            packet = serialInst.readline()
            gesture = packet.decode('utf').strip("\r\n")
            if gesture in valid_gestures:       
                    processGesture(gesture)          
            else:
                print(gesture)
        #als het bij de laatste frame is gekomen gaat de programma weer beginnen bij de eerste frame
        if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            frame_counter = 0 
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
        # hier geef ik de frame een kleur
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #namedWindow zoekt de resolutie van je monitor #
        #setWindowProperty zorgt er voor dat de video's op de zelfde resolutie komt te staan als je scherm
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, 1)

        # laat het resultaat zien van de frames
        cv2.imshow('frame',frame) 
        
        cv2.waitKey(6) & 0xFF
        
            

                
def twee():
    input_video_path = 'd:/Ma/Bewijzenmap/leerjaar 2/periode 2/F2M6BO/openCV/video/zeemeermin2_v6.mp4'
    cap = cv2.VideoCapture(input_video_path)

    frame_counter = 0
    while(True):
        # dit zorgt ervoor dat ik de frames van de video een voor een pak
        ret, frame = cap.read()
        frame_counter += 1
        # deze loop zorgt ervoor dat ik in deze loop weer terug naar de gesture read loop ga
        if serialInst.in_waiting:
            packet = serialInst.readline()
            gesture = packet.decode('utf').strip("\r\n")
            if gesture in valid_gestures:       
                    processGesture(gesture)          
            else:
                print(gesture)
        #als het bij de laatste frame is gekomen gaat de programma weer beginnen bij de eerste frame
        if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            frame_counter = 0 
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
            
        # hier geef ik de frame een kleur
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #namedWindow zoekt de resolutie van je monitor #
        #setWindowProperty zorgt er voor dat de video's op de zelfde resolutie komt te staan als je scherm

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, 1)
        # laat het resultaat zien van de frames
        cv2.imshow('frame',frame)
        

        # hier heb ik een command aangemaakt dat ervoor zorgt dat als ik een bepaalde knop druk dat de loop stopt
        cv2.waitKey(6) & 0xFF


def drie():
    input_video_path = 'd:/Ma/Bewijzenmap/leerjaar 2/periode 2/F2M6BO/openCV/video/zeemeermin5_v6.mp4'
    cap = cv2.VideoCapture(input_video_path)

    frame_counter = 0
    while(True):
        # dit zorgt ervoor dat ik de frames van de video een voor een pak
        ret, frame = cap.read()
        frame_counter += 1
        if serialInst.in_waiting:
            packet = serialInst.readline()
            gesture = packet.decode('utf').strip("\r\n")
            if gesture in valid_gestures:       
                    processGesture(gesture)          
            else:
                print(gesture)
        #als het bij de laatste frame is gekomen gaat de programma weer beginnen bij de eerste frame
        if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            frame_counter = 0 
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
            
        # hier geef ik de frame een kleur
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #namedWindow zoekt de resolutie van je monitor #
        #setWindowProperty zorgt er voor dat de video's op de zelfde resolutie komt te staan als je scherm

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, 1)
        # laat het resultaat zien van de frames
        cv2.imshow('frame',frame)
        

        # hier heb ik een command aangemaakt dat ervoor zorgt dat als ik een bepaalde knop druk dat de loop stopt
        cv2.waitKey(6) & 0xFF


def vier():
    input_video_path = 'd:/Ma/Bewijzenmap/leerjaar 2/periode 2/F2M6BO/openCV/video/zeemeermin6_v6.mp4'
    cap = cv2.VideoCapture(input_video_path)

    frame_counter = 0
    while(True):
        # dit zorgt ervoor dat ik de frames van de video een voor een pak
        ret, frame = cap.read()
        frame_counter += 1
        if serialInst.in_waiting:
            packet = serialInst.readline()
            gesture = packet.decode('utf').strip("\r\n")
            if gesture in valid_gestures:       
                    processGesture(gesture)          
            else:
                print(gesture)
        #als het bij de laatste frame is gekomen gaat de programma weer beginnen bij de eerste frame
        if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            frame_counter = 0 
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
            
        # hier geef ik de frame een kleur
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #namedWindow zoekt de resolutie van je monitor #
        #setWindowProperty zorgt er voor dat de video's op de zelfde resolutie komt te staan als je scherm

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, 1)
        # laat het resultaat zien van de frames
        cv2.imshow('frame',frame)
        

        # hier heb ik een command aangemaakt dat ervoor zorgt dat als ik een bepaalde knop druk dat de loop stopt
        cv2.waitKey(6) & 0xFF


 


def processGesture(gesture):   
    if gesture == "DOWN":           
        print("onder")
        een()       
    elif gesture == "UP":
        print("boven")
        twee()
    elif gesture == "LEFT":
        print("links")
        drie()
    elif gesture == "RIGHT":  
        print("rechts")
        vier()

# kijkt naar alle COM porten die beschikbaar zijn
# ports = serial.tools.list_ports.comports()

# maakt verbinding met de serial ports
serialInst = serial.Serial()

# # array met al mijn usb porten 
# portList = []


# for onePort in ports:
#     portList.append(str(onePort))
#     print(str(onePort))


# # hier kan je de nummer van de COM poort kiezen
# val = input("select Port: COM")


# zoekt in de port array de nummer die je als input heeft aangegeven en dan verbind het met die port
# for x in range(0,len(portList)):
    
#     if portList[x].startswith("COM" + str(val)):
portVar = "COM" + str(7)
# print(portList[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
gestures()










        





