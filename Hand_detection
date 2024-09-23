import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
mp_draw_styles = mp.solutions.drawing_styles

def process_image(frame, detection):
    frame.flags.writeable = False
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # color conversion
    results = detection.process(frame) # process the image
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)   # color conversion
    frame.flags.writeable = True
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, 
                mp_hands.HAND_CONNECTIONS, 
                mp_draw_styles.get_default_hand_landmarks_style(), 
                mp_draw_styles.get_default_hand_connections_style())
    return frame

def read_webcam(idx=0):
    with mp_hands.Hands() as detection:
        video = cv2.VideoCapture(idx)
        while True:
            state, frame = video.read()
            if not state:
                break
            frame = process_image(frame, detection)
            cv2.imshow('frame', frame)         
            if cv2.waitKey(10) == ord('q'):     
                break                          
        video.release()                        
    cv2.destroyAllWindows()       

# execute outside function
if __name__ == "__main__":
    read_webcam()