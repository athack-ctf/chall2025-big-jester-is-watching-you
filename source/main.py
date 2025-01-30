import cv2
from pyzbar import pyzbar
import time
import requests

# Function to be executed when a QR code is detected
def execute_function(url):
    print(f"QR Code detected! URL: {url}")
    # Add your custom logic here
    r=requests.get(url, headers={"Content-Type":"ATHACKCTF{Hehehe}"})


index = 0
arr = []
for index in range(10):
    cap = cv2.VideoCapture(index)
    if cap.read()[0]:
        break

# Initialize the webcam
# cap = cv2.VideoCapture(0)

# Delay between QR code detections (in seconds)
delay = 5  # Adjust this value as needed

# Variable to store the last time a QR code was detected
last_detection_time = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale (optional, but can improve QR detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect QR codes in the frame
    qr_codes = pyzbar.decode(gray)

    # Get the current time
    current_time = time.time()

    # Process each detected QR code
    for qr_code in qr_codes:
        # Check if enough time has passed since the last detection
        if current_time - last_detection_time >= delay:
            # Extract the URL from the QR code
            url = qr_code.data.decode("utf-8")
            
            # Execute the function with the detected URL
            execute_function(url)
            
            # Update the last detection time
            last_detection_time = current_time

    # Display the resulting frame (optional)
    cv2.imshow('QR Code Scanner', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()