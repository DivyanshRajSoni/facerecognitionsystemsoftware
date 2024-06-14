def update_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
         messagebox.showerror("Error","All Fields are Required",parent=self.root)
      else:
            try:
               Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
               if Update>0:
                 conn=mysql.connector.connect(host="localhost",username="root",password="sHj@6378#jw",database="divyanshdb")
                 my_cursor=conn.cursor()
                 my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s  where Student_id=%s",(
                    
                                                                                                                                                                                          self.var_dep.get(),
                                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                          self.var_semester.get(),
                                                                                                                                                            
                                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                                          self.var_div.get(),
                                                                                                                                                                                          self.var_roll.get(),
                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                          self.var_teacher.get(),
                                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                                          self.var_std_id.get()       
                                                                                                                                                                                                               ))
               else:
                  if not Update:
                      return
               
               messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
               conn.commit()
               self.fetch_data()
               conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
