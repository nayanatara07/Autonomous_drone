import cv2
import sys
import logging as log
import datetime as dt
from time import sleep

# Load the cascade
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log', level=log.INFO)

# sets the video source to the default webcam, which OpenCV can easily capture.
video_capture = cv2.VideoCapture(0)
anterior = 0
previous_faces = set()

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    unique_faces = set()
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        unique_faces.add((x, y, w, h))

    # Get the count of unique faces detected
    num_unique_faces = len(unique_faces)

    # Display the count of unique faces detected
    cv2.putText(frame, f"Unique Faces Detected: {num_unique_faces}", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    if anterior != num_unique_faces:
        anterior = num_unique_faces
        log.info("Unique faces: " + str(num_unique_faces) + " at " + str(dt.datetime.now()))

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Wait for user input; if the 'q' key is pressed, break the loop
    key = cv2.waitKey(10)
    if key == ord('q') or key == 27:  # 'q' or Esc
        break

# Release the video capture object and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
