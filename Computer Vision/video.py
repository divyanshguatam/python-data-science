import cv2

def process_something(frame):
    # do whatever u want here
    return frame

def read_video(path):
    video = cv2.VideoCapture(path)
    while True:
        state, frame = video.read()
        if not state:
            break
        frame = process_something(frame)
        cv2.imshow('frame', frame)          # display the frame
        if cv2.waitKey(10) == ord('q'):      # if you pressed 'q', 
            break                           # then quit
    video.release()                         # free the object
    cv2.destroyAllWindows()                 # close the window

# execute outside function
if __name__ == "__main__":
    read_video(r"C:\Users\ZAID\Videos\obama.mp4")   
