import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import os
import csv
from tkinter import filedialog
import numpy as np


mydata=[]
class Present:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("facesc.ico")
        #==============Variables========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        self.var_atten_status = StringVar()
        
        
        
        
        
        
        # Third Image
        img2=Image.open(r"F:/face_recognition_project-main/college_images/eye.jpg")
        img2=img2.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=0,width=800,height=200)

        # bg image..
        img3=Image.open(r"F:/face_recognition_project-main/college_images/secondd.jpg")
        img3=img3.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        # bg image..
        img4=Image.open(r"F:/face_recognition_project-main/college_images/tech.jpg")
        img4=img4.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="DATA BASE SYSTEM",font=("times new roman",35,"bold"),bg="lightblue",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)
        
        # left Label Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="PersonData Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)
        
        
        
        img_left=Image.open(r"F:/face_recognition_project-main/college_images/nm.jpg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        left_inside_frame=Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=0,y=135,width=720,height=370)
        
        #Labels and Entry..
        #Attendence and id..
        
        #student id
        attendenceId_label=Label(left_inside_frame,text="AttendenceId",font=("times new roman",13,"bold"),bg="white")
        attendenceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendenceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times of roman",13,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        
        #Roll
        rollLabel=Label(left_inside_frame,text="Roll:",font=("comicsansns",11,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font=("comicsansns",11,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)
        
        #Name
        nameLabel=Label(left_inside_frame,text="Name:",font=("comicsansns",11,"bold"),bg="white")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font=("comicsansns",11,"bold"))
        atten_name.grid(row=1,column=1,pady=8)
        
        #Department
        depLabel=Label(left_inside_frame,text="Department:",font=("comicsansns",11,"bold"),bg="white")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font=("comicsansns",11,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)
        
        #Time
        timeLabel=Label(left_inside_frame,text="Time:",font=("comicsansns",11,"bold"),bg="white")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font=("times of roman",11,"bold"))
        atten_time.grid(row=2,column=1,pady=8)
        
        #Date
        dateLabel=Label(left_inside_frame,text="Date:",font=("comicsansns",11,"bold"),bg="white")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font=("times of roman",11,"bold"))
        atten_date.grid(row=2,column=3,pady=8)
        
        #Attencdence
        attendenceLabel=Label(left_inside_frame,text="Entry Status:",font=("comicsansns",11,"bold"),bg="white")
        attendenceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("comicsansns",11 ,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="lightblue",fg="black") # type: ignore
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,width=17,text="Export csv",command=self.exportCsv,font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,width=17,text="Update",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,width=17,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        reset_btn.grid(row=0,column=3)
        
        # Right Label Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="DataBase",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)
        
        #button frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)
        
        #============ScrollBar Table=======
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendaceReportTable=ttk.Treeview(table_frame,columns=("id","Roll","name","department","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)
        
        self.AttendaceReportTable.heading("id",text="Attendance IK")
        self.AttendaceReportTable.heading("Roll",text="Roll")
        self.AttendaceReportTable.heading("name",text="Name")
        self.AttendaceReportTable.heading("department",text="Department")
        self.AttendaceReportTable.heading("time",text="Time")
        self.AttendaceReportTable.heading("date",text="Date")
        self.AttendaceReportTable.heading("status",text="Status")
        
        self.AttendaceReportTable["show"]="headings"
        self.AttendaceReportTable.column("id",width=100)
        self.AttendaceReportTable.column("Roll",width=100)
        self.AttendaceReportTable.column("name",width=100)
        self.AttendaceReportTable.column("department",width=100)
        self.AttendaceReportTable.column("time",width=100)
        self.AttendaceReportTable.column("date",width=100)
        self.AttendaceReportTable.column("status",width=100)
        self.AttendaceReportTable.pack(fill=BOTH,expand=1)
        
       
        self.AttendaceReportTable.unbind("<ButtonRelease-1>")
        self.AttendaceReportTable.bind("<ButtonRelease-1>", self.get_cursor)
        
        
        #=================Fetch Data=============================
        
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)
                
                
                #import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln, mode="r", newline="") as myfile:  # Mode corrected to read mode
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
               messagebox.showerror("No Data", "No Data Found to Export", parent=self.root)
               return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", f"Your data exported to {os.path.basename(fln)} successfully")  # Corrected format string
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def fetchData(self, rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())  # Corrected widget name
        for i in rows:
            self.AttendaceReportTable.insert("", END, values=i)

    # ... your existing code

    # Unbind to avoid multiple bindings

            
    def get_cursor(self,event=""):
        cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(cursor_row)
        row=content["values"]
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_status.set(row[6])
        
        
        
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("")








        
if __name__ == "__main__":
    root=Tk()
    obj=Present(root)
    root.mainloop()
    #35:20
