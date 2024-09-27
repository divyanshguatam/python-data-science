import streamlit as st
from collections import defaultdict
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import tempfile
import numpy as np

# Initialize YOLO model and track history
track_history = defaultdict(lambda: [])
model = YOLO("yolov8n-seg.pt")

# Set up Streamlit app layout
st.title("Object Detection and Tracking with YOLOv8")
start_button = st.button("Start Detection")

# Placeholder for the video frames
frame_placeholder = st.empty()

def process_frame(frame, model):
    """
    Process a single frame, run detection and segmentation,
    and return the annotated frame.
    """
    annotator = Annotator(frame, line_width=2)
    
    # Perform object detection and segmentation
    results = model.track(frame, persist=True)

    if results[0].boxes.id is not None and results[0].masks is not None:
        masks = results[0].masks.xy
        track_ids = results[0].boxes.id.int().cpu().tolist()
        class_indices = results[0].boxes.cls.int().cpu().tolist()  # Get class indices

        # Annotate detected objects with bounding boxes and labels
        for mask, track_id, class_idx in zip(masks, track_ids, class_indices):
            color = colors(int(track_id), True)
            txt_color = annotator.get_txt_color(color)
            
            # Get the class name from the model
            class_name = model.names[class_idx]
            
            # Annotate the object with the class name and track ID
            annotator.seg_bbox(mask=mask, mask_color=color, label=f"{class_name} ({track_id})", txt_color=txt_color)

    return annotator.result()

def video_stream():
    # Access the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Failed to access the webcam.")
        return

    # Set up temporary file to save the video
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.avi')
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

    out = cv2.VideoWriter(tmp_file.name, cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))

    # Run the video stream loop
    while start_button:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to read frame from webcam.")
            break

        # Process the frame and get the annotated result
        processed_frame = process_frame(frame, model)
        
        # Write frame to output video
        out.write(processed_frame)

        # Display frame in Streamlit app
        frame_placeholder.image(processed_frame, channels="BGR")

        # Stop video if user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up
    out.release()
    cap.release()

if start_button:
    video_stream()
else:
    st.write("Click the button to start object detection.")

    #streamlit run "object detection.py"