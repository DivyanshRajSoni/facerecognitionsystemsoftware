import cv2
import numpy as np
import pytesseract

# Set the tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust the path if necessary

# Replace 'your_roll_number' with the actual roll number you are looking for
TARGET_ROLL_NUMBER = "0206AL221048"

def show_present_message():
    # Create a black background image
    present_img = np.zeros((100, 400, 3), dtype=np.uint8)

    # Write "Present" message in red
    cv2.putText(present_img, "Present", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the image
    cv2.imshow("Present Message", present_img)
    cv2.waitKey(3000)  # Display the image for 3 seconds
    cv2.destroyAllWindows()

def scan_roll_number_from_camera():
    # Open the camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(gray, config='--psm 6')

        # Check if the target roll number is found in the detected text
        if TARGET_ROLL_NUMBER in text:
            print("Roll Number Found! Present")
            show_present_message()
            break

        # Display the resulting frame
        cv2.imshow("ID Card Scanner", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_roll_number_from_camera()
