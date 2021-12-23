import cv2
import time
import sys

def een():
    input_video_path = './video/RocketLeague.mp4'
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
        # Display the resulting frame
        cv2.imshow('video',frame)
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
    input_video_path = './video/test1.mp4'
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
        # Display the resulting frame
        cv2.imshow('video',frame)
        key_pressed = cv2.waitKey(8) & 0xFF
        if key_pressed == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
        

def drie():
    input_video_path = './video/test1.mp4'
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
        # Display the resulting frame
        cv2.imshow('video',gray)
        key_pressed = cv2.waitKey(8) & 0xFF
        if key_pressed == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break


een()



