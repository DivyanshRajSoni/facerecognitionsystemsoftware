import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import concurrent.futures
import threading
import os
import easyocr

# Set the path to the current directory
CURRENT_DIR = r'F:\face_recognition_project-main'

class CardScanner:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("ID Card Scanner")

        title_lbl = Label(self.root, text="ID Card Scanner", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top_path = os.path.join(CURRENT_DIR, "ide.jpg")
        if os.path.isfile(img_top_path):
            img_top = Image.open(img_top_path)
            img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            f_lbl = Label(self.root, image=self.photoimg_top)
            f_lbl.place(x=0, y=55, width=1530, height=325)
        else:
            print(f"Error: Unable to find the file '{img_top_path}'")

        self.b1_1 = Button(self.root, text="SCAN ID CARD", command=self.start_scan_thread, cursor="hand2", font=("times new roman", 30, "bold"), bg="black", fg="white")
        self.b1_1.place(x=0, y=380, width=1530, height=60)

        img_bottom_path = os.path.join(CURRENT_DIR, "id.jpg")
        if os.path.isfile(img_bottom_path):
            img_bottom = Image.open(img_bottom_path)
            img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
            f_lbl = Label(self.root, image=self.photoimg_bottom)
            f_lbl.place(x=0, y=440, width=1530, height=325)
        else:
            print(f"Error: Unable to find the file '{img_bottom_path}'")

        # Initialize EasyOCR Reader
        self.reader = easyocr.Reader(['en'])

    def show_present_message(self):
        present_img = np.zeros((100, 400, 3), dtype=np.uint8)
        cv2.putText(present_img, "Present", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Present Message", present_img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()

    def detect_text(self, roi):
        try:
            # Use EasyOCR to extract text from the ROI
            results = self.reader.readtext(roi)
            text = " ".join([res[1] for res in results])
            return text
        except Exception as e:
            print(f"Error in OCR: {e}")
            return ""

    def scan_id_card(self):
        try:
            cap = cv2.VideoCapture(0)

            if not cap.isOpened():
                print("Error: Could not open camera.")
                return

            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Could not read frame.")
                    break

                # Convert frame to grayscale
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Use adaptive thresholding to convert to binary image
                binary_frame = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

                # Find contours in the binary image
                contours, _ = cv2.findContours(binary_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # Loop through contours to find the ID card
                for contour in contours:
                    area = cv2.contourArea(contour)
                    if area > 10000:  # Adjust this value as needed
                        x, y, w, h = cv2.boundingRect(contour)
                        roi = gray_frame[y:y+h, x:x+w]

                        # Extract text using OCR in a separate thread
                        with concurrent.futures.ThreadPoolExecutor() as executor:
                            text = executor.submit(self.detect_text, roi).result()

                        # Check if the recognized text contains the target keywords
                        if any(keyword in text for keyword in ["CSE-AIML", "0206AL221048", "Session:2022-26", "SUNIL SONI"]):
                            print("Roll Number Found! Present")
                            self.show_present_message()
                            cap.release()
                            cv2.destroyAllWindows()
                            return

                # Display the frame
                cv2.imshow("Camera Feed", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"Error in scan_id_card: {e}")

    def start_scan_thread(self):
        scan_thread = threading.Thread(target=self.scan_id_card)
        scan_thread.start()

if __name__ == "__main__":
    root = Tk()
    obj = CardScanner(root)
    root.mainloop()
