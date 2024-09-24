import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

# Open webcam
webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    status, frame = webcam.read()
    
    if not status:
        break

    # Detect objects in frame
    bbox, label, conf = cv.detect_common_objects(frame)

    # Draw bounding boxes
    output_frame = draw_bbox(frame, bbox, label, conf)

    # Display the output frame
    cv2.imshow("Real-time Object Detection", output_frame)

    # Break the loop with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
webcam.release()
cv2.destroyAllWindows()
