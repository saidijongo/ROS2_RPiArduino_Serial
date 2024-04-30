
import cv2
from pyzbar.pyzbar import decode

def read_micro_qr_code(image):
    # Decode QR code
    decoded_objects = decode(image)

    if decoded_objects:
        for obj in decoded_objects:
            if obj.type == 'MICROQR':
                print("Micro QR Code Data:", obj.data.decode('utf-8'))
                x, y, w, h = obj.rect
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                return obj.data.decode('utf-8'), image

    print("No micro QR code detected.")
    return None, image

def read_micro_qr_code_from_camera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cv2.imshow('Camera', frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        micro_qr_code_data, frame_with_micro_qr = read_micro_qr_code(gray)

        if micro_qr_code_data:
            print("Micro QR Code Data:", micro_qr_code_data)
            cv2.imshow('Micro QR Code', frame_with_micro_qr)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

read_micro_qr_code_from_camera()


"""


import cv2
from pyzbar.pyzbar import decode

# Function to read QR code from an image
def read_qr_code(image):
    # Decode QR code
    decoded_objects = decode(image)

    # Check if any QR code is detected
    if decoded_objects:
        # Iterate over all decoded objects
        for obj in decoded_objects:
            # Check if the decoded object is a QR code
            if obj.type == 'QRCODE':
                # Print QR code data
                print("QR Code Data:", obj.data.decode('utf-8'))
                # Extract the bounding box coordinates of the QR code
                x, y, w, h = obj.rect
                # Draw a rectangular frame around the detected QR code
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # Return the QR code data
                return obj.data.decode('utf-8'), image

    # If no QR code is detected, print a message
    print("No QR code detected.")
    return None, image

# Function to capture video from camera and process frames
def read_qr_code_from_camera():
    # Create VideoCapture object to access the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the captured frame
        cv2.imshow('Camera', frame)

        # Convert frame to grayscale for QR code detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Call function to read QR code from the frame
        qr_code_data, frame_with_qr = read_qr_code(gray)

        # If QR code data is found, display it
        if qr_code_data:
            print("QR Code Data:", qr_code_data)
            # Display the frame with the detected QR code
            cv2.imshow('QR Code', frame_with_qr)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Call function to read QR code from camera
read_qr_code_from_camera()
"""
