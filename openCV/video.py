import cv2
import time



def een():
    input_video_path = 'D:/Ma/Bewijzenmap/leerjaar 2/periode 2/F2M6BO/openCV/video/ROCKET.mp4'
    cap = cv2.VideoCapture(input_video_path)

    frame_counter = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame_counter += 1
        #If the last frame is reached, reset the capture and the frame_counter
        if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            frame_counter = 0 #Or whatever as long as it is the same as next line
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            cap.release()
            cv2.destroyAllWindows()
            twee()
          
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, 1)

        # Display the resulting frame
        cv2.imshow('frame',frame) 
        key_pressed = cv2.waitKey(8) & 0xFF
        if key_pressed == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            twee()
            break
        if key_pressed == ord('w'):
            cap.release()
            cv2.destroyAllWindows()
            drie()
            break
                
def twee():
    input_video_path = 'D:/Ma/Bewijzenmap/leerjaar 2/periode 2/F2M6BO/openCV/video/onetap.mp4'
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
        # laat het resultaat zien van de frames
        cv2.imshow('frame',frame)

        # hier heb ik een command aangemaakt dat ervoor zorgt dat als ik een bepaalde knop druk dat de loop stopt
        key_pressed = cv2.waitKey(8) & 0xFF
        if key_pressed == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
        

def drie():
    input_video_path = 'D:/Ma/Bewijzenmap/leerjaar 2/periode 2/F2M6BO/openCV/video/yes.mp4'
    cap = cv2.VideoCapture(input_video_path)

    frame_counter = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame_counter += 1
        #If the last frame is reached, reset the capture and the frame_counter
        if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            frame_counter = 0 #Or whatever as long as it is the same as next line
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, 1)
        # Display the resulting frame
        cv2.imshow('frame',gray)
        key_pressed = cv2.waitKey(8) & 0xFF
        if key_pressed == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break


een()



