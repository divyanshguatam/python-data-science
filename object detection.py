import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

def speech(text):
    print(text)
    language ='en'
    output=gTTS(text=text,lang=language,slow=False)         
    output.save("0")
    playsound("0")


video = cv2.VideoCapture(1)
labels = []

while True:
    ret, frame = video.read()
    bbox, label = conf = cv.detect_common_objects(frame) 
    output_image = draw_bbox(frame,bbox,label,conf)
    cv2.imshow("Object Detecion", output_image)
    
    for item in label:
        if item in labels:
            pass

        else:
            labels.append(item)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

i =0
new_sentence = [] 

for label in labels:
    if i == 0:
        new_sentence.append(f"found a{label}, and,")
    else:
        new_sentence.append(f"a{label}")

    i += 1   

speech(" ".join(new_sentence))



