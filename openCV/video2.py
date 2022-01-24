import cv2
import time
from pathlib import Path

# Maak een path instance voor de huidige map
path = Path('.')
# Zet om naar absoluut pad
current_folder = str(path.absolute());

def een():
    # Stel het pad samen vanaf de huiidge map: video/ROCKET.mp4 (en dan het absolute/volledige pad)
    input_video_path = str(path.joinpath('video','ROCKET.mp4').absolute())
    cap = cv2.VideoCapture(input_video_path)

    frame_counter = 0
    while(True):
        # dit zorgt ervoor dat ik de frames van de video een voor een pak
        ret, frame = cap.read()
        frame_counter += 1
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
        cv2.imshow('frame',frame) 
        cv2.waitKey(8)
