import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk,ImageDraw
import pymysql
import datetime as dt
import time
import math as m

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="#021e2f")
        
        #-------Background COlor-----------------#
        left_lbl=tk.Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        
        right_lbl=tk.Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        
        ##Register tk.Frame###
        
        frame1=tk.Frame(self.root,bg="white")
        frame1.place(x=440,y=100,width=800,height=500)
        
        title=tk.Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="green")
        title.place(x=110,y=30)
        
        #----------------ROW 1--------------------------#
        
        #self.var_fname=StringVar()
        f_name=tk.Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray")
        f_name.place(x=110,y=100)
        
        #txt_fname=tk.Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_fname)
        self.txt_fname=tk.Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=110,y=130,width=250)
        
        l_name=tk.Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray")
        l_name.place(x=430,y=100)
        
        self.txt_lname=tk.Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=430,y=130,width=250)
        
        #--------------------ROW 2-----------------------------#
        
        contact=tk.Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray")
        contact.place(x=110,y=170)
        
        self.txt_contact=tk.Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=110,y=200,width=250)
        
        email=tk.Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray")
        email.place(x=430,y=170)
        
        self.txt_email=tk.Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=430,y=200,width=250)
        
        #------------------ROW 3-------------------------------#
        
        question=tk.Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray")
        question.place(x=110,y=240)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=tk.CENTER)
        self.cmb_quest.place(x=110,y=270,width=250)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.current(0)
        
        answer=tk.Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray")
        answer.place(x=430,y=240)
        
        self.txt_answer=tk.Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=430,y=270,width=250)
        
        #--------------------ROW 4-----------------------------#
        
        passwd=tk.Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray")
        passwd.place(x=110,y=310)
        
        self.txt_passwd=tk.Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_passwd.place(x=110,y=340,width=250)
        
        cpasswd=tk.Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray")
        cpasswd.place(x=430,y=310)
        
        self.txt_cpasswd=tk.Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpasswd.place(x=430,y=340,width=250)
        
        #--------Terms---------#
        
        self.var_chk=tk.IntVar()
        chk=tk.Checkbutton(frame1,text="Agree to Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12))
        chk.place(x=110,y=380)
        
        btn_register=tk.Button(frame1,text="Register Now",font=("times new roman",13),bg="green",fg="white",bd=0,cursor="hand2",command=self.register_data)
        btn_register.place(x=110,y=420)
        
        btn_login=tk.Button(self.root,text="Sign In",command=self.signin,font=("times new roman",13),bg="green",fg="white",bd=0,cursor="hand2")
        btn_login.place(x=870,y=520,width=120)
        
        ##-------------Clock------------------##
        
        self.lbl=tk.Label(self.root,text="\nClock",font=("times new roman",25,"bold"),fg="white",compound=tk.BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=380)
        self.working()
        
    def clock_image(self,hr_,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #-----For Clock Image-----------#
        bg=Image.open("images/clock.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        
        #------Hour Line Image----------#
        origin=200,200
        draw.line((origin,200+60*m.sin(m.radians(hr_)),200-60*m.cos(m.radians(hr_))),fill="#DF005e",width=4)
        
        #------Min Line Image----------#
        draw.line((origin,200+80*m.sin(m.radians(min_)),200-80*m.cos(m.radians(min_))),fill="white",width=3)
        
        #------Sec Line Image----------#
        draw.line((origin,200+100*m.sin(m.radians(sec_)),200-100*m.cos(m.radians(sec_))),fill="yellow",width=2)
        
        #-------Ellipse-----------------#
        draw.ellipse((191,191,210,210),fill="#1AD5D5")
    
        clock.save("clock_new.png")
        
    def working(self):
        h=dt.datetime.now().time().hour
        m=dt.datetime.now().time().minute
        s=dt.datetime.now().time().second
        
        hr_=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        self.clock_image(hr_,min_,sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
        
    def signin(self):
        self.root.destroy()
        import login2
        
    def clear(self):
        self.txt_fname.delete(0,tk.END)
        self.txt_lname.delete(0,tk.END)
        self.txt_contact.delete(0,tk.END)
        self.txt_email.delete(0,tk.END)
        self.txt_passwd.delete(0,tk.END)
        self.txt_cpasswd.delete(0,tk.END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,tk.END)
        
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_passwd.get()=="" or self.txt_cpasswd.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_passwd.get()!=self.txt_cpasswd.get() :
            messagebox.showerror("Error","Passwords are not matched",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Terms & Conditions",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="1234",database="registration")
                cur=con.cursor()
                cur.execute("select * from regfields where email=%s",self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User already exists with same email address,Register with another Email address",parent=self.root)
                else:
                    cur.execute("insert into regfields (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",(self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(),self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get(),self.txt_passwd.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registration Sucessful",parent=self.root)  
                    self.clear()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
                
root=tk.Tk()
obj=Register(root)
root.mainloop()