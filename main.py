from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import os
import tkinter
from student import Student
from train import Train
from chatbot import ChatBot
from face_recognition import Face_Recognition
from present import Present
from cardid import CardScanner


class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("facesc.ico")

        # Load Images
        self.photoimg = self.load_image("college_images/to.jpg", 500, 130)
        self.photoimg1 = self.load_image("college_images/do.jpg", 500, 130)
        self.photoimg2 = self.load_image("college_images/co.jpg", 550, 130)
        self.photoimg3 = self.load_image("college_images/tee.png", 1530, 710)
        self.photoimg4 = self.load_image("college_images/student.jpg", 220, 220)
        self.photoimg5 = self.load_image("college_images/dec.jpg", 220, 220)
        self.photoimg6 = self.load_image("college_images/report.jpg", 220, 220)
        self.photoimg7 = self.load_image("college_images/bh.png", 220, 220)
        self.photoimg8 = self.load_image("college_images/rig.jpg", 220, 220)
        self.photoimg9 = self.load_image("college_images/face_det.png", 220, 220)
        self.photoimg10 = self.load_image("college_images/softdeveloper.jpg", 220, 220)
        self.photoimg11 = self.load_image("college_images/exi.png", 220, 220)

        # Set up UI
        self.setup_ui()

    def load_image(self, path, width, height):
        img = Image.open(path)
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)

    def setup_ui(self):
        # First Image
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=500, height=130)

        # Second Image
        Label(self.root, image=self.photoimg1).place(x=500, y=0, width=500, height=130)

        # Third Image
        Label(self.root, image=self.photoimg2).place(x=1000, y=0, width=550, height=130)

        # Background Image
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title
        title_lbl = Label(bg_img, text="FACE RECOGNITION SYSTEM SOFTWARE",
        font=("times new roman", 35, "bold"), bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Time Display
        self.update_time(title_lbl)

        # Buttons
        self.create_button(bg_img, self.photoimg4, "Person Details", self.student_details, 200, 100)
        self.create_button(bg_img, self.photoimg5, "Face Detector", self.face_data, 500, 100)
        self.create_button(bg_img, self.photoimg6, "Card Recognition", self.cardid, 800, 100)
        self.create_button(bg_img, self.photoimg7, "ChatBot", self.chatbot, 1100, 100)
        self.create_button(bg_img, self.photoimg8, "Train Data", self.train_data, 200, 380)
        self.create_button(bg_img, self.photoimg9, "Photos", self.open_img, 500, 380)
        self.create_button(bg_img, self.photoimg10, "Data Base", self.present_data, 800, 380)
        self.create_button(bg_img, self.photoimg11, "Exit", self.i_exit, 1100, 380)

    def create_button(self, parent, image, text, command, x, y):
        Button(parent, image=image, cursor="hand2", command=command).place(x=x, y=y, width=220, height=220)
        Button(parent, text=text, cursor="hand2", command=command, font=("times new roman", 15, "bold"), bg="black",
        fg="white").place(x=x, y=y + 200, width=220, height=40)

    def update_time(self, parent):
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(parent, font=('times new roman', 14, 'bold'), background='black', foreground='white')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

    def open_img(self):
        os.startfile("data")

    def i_exit(self):
        if tkinter.messagebox.askyesno("Face Recognition", "Are you sure to exit from Face Recognition System Software?", parent=self.root):
            self.root.destroy()

    def student_details(self):
        self.open_new_window(Student)

    def train_data(self):
        self.open_new_window(Train)

    def face_data(self):
        self.open_new_window(Face_Recognition)

    def present_data(self):
        self.open_new_window(Present)

    def chatbot(self):
        self.open_new_window(ChatBot)

    def cardid(self):
        self.open_new_window(CardScanner)

    def open_new_window(self, _class):
        new_window = Toplevel(self.root)
        _class(new_window)


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
