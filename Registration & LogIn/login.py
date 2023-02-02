from tkinter import *
import mysql.connector
from tkinter import messagebox,ttk
class SignIn:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Login Window")
        self.root.config(bg="white")
        frame1=Frame(self.root,bg="lightgreen").place(x=150,y=100,width=400,height=500)
        frame2=Frame(self.root,bg="lightblue")
        frame2.place(x=550,y=100,width=650,height=500)
        flabe=Label(frame2,text="LOGIN HERE",font=("times new roman",30,"bold"),fg="green",bg="lightblue").place(x=90,y=50)
        email_label=Label(frame2,text="Email Id",font=("times new roman",20,"bold"),fg="gray",bg="lightblue").place(x=90,y=120)
        self.email_txt=Entry(frame2,font=("times new roman",13),border=5,relief=SUNKEN)
        self.email_txt.place(x=90,y=170,width=300)
        password_label=Label(frame2,text="Password",font=("times new roman",20,"bold"),fg="gray",bg="lightblue").place(x=90,y=230)

        self.password_txt=Entry(frame2,font=("times new roman",13),border=5,relief=SUNKEN)
        self.password_txt.place(x=90,y=280,width=300)

        login_btn=Button(frame2,text="Sign In",command=self.login,bg="white",font=("times new roman",14,"bold"),cursor="hand2").place(x=90,y=330,width=100)

        register_btn=Button(frame2,text="Click here to register",command=self.registration,font=("times new roman",14,"bold"),cursor="hand2",border=0,bg="lightblue",fg="red").place(x=90,y=390)

        forget_btn=Button(frame2,text="Forget Password?",command=self.forget,font=("times new roman",14,"bold"),cursor="hand2",border=0,bg="lightblue",fg="red").place(x=320,y=390)

    def registration(self):
        self.root.destroy()
        import registration

    def forget(self):
        self.root2=Tk()
        self.root2.geometry("500x400+450+130")
        self.root2.title("forget password?")
        self.root2.config(bg="white")
        self.root2.focus_force()
        self.root2.grab_set()

        flabe=Label(self.root2,text="RESET PASSWORD",font=("times new roman",25,"bold"),fg="red",bg="white").place(x=100,y=20)

        email_label=Label(self.root2,text="Email Id",font=("times new roman",20,"bold"),fg="gray",bg="white").place(x=90,y=90)
        self.email_txt=Entry(self.root2,font=("times new roman",13),bg="lightgray",border=5,relief=SUNKEN)
        self.email_txt.place(x=90,y=170,width=300)

        email_sub_btn=Button(self.root2,text="Submit",command=self.email_submit,font=("times new roman",14,"bold"),cursor="hand2",bg="lightblue",fg="red",relief=GROOVE).place(x=90,y=250)


    def email_submit(self):
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='admin',database='login')
            cur=con.cursor()
            cur.execute('select * from register where email=%s',(self.email_txt.get(),))
            row=cur.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Wrong Email",parent=self.root2)
            else:
                self.security_check()
        except Exception as er:
            messagebox.showerror("Error",f"Error due to {str(er)}",parent=self.root2)


    def security_check(self):
        self.root3=Tk()
        self.root3.geometry("500x400+450+130")
        self.root3.title("Reset Password")
        self.root3.config(bg="white")
        self.root3.focus_force()

        # row ===================
        security_label=Label(self.root3,text="Answer Security Question",font=("times new roman",18,"bold"),bg="white",fg="green").place(x=100,y=10)
        securityQ_label=Label(self.root3,text="Question",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=80,y=50)
        self.nCombobx_text=ttk.Combobox(self.root3,font=("times new roman",13),state="readonly",justify=CENTER)
        self.nCombobx_text['values']=("Select","Name of first school.","Name of childhood friend","Name of birth place","First phone purchased")
        self.nCombobx_text.place(x=80,y=90,width=250)
        self.nCombobx_text.current(0)
        answer_label=Label(self.root3,text="Answer",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=80,y=140)
        self.nanswer_text=Entry(self.root3,bg="lightgray",font=("times new roman",13))
        self.nanswer_text.place(x=80,y=180,width=250)

        seucurity_sub_btn=Button(self.root3,text="Submit",command=self.seq_varification,font=("times new roman",14,"bold"),cursor="hand2",border=0,bg="lightblue",fg="orange").place(x=80,y=240)

    def seq_varification(self):
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='admin',database='login')
            cur=con.cursor()
            cur.execute('select * from register where question=%s and answer=%s',(self.nCombobx_text.get(),self.nanswer_text.get()))
            row=cur.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Security Question and Answer not matched",parent=self.root)
            else:
                messagebox.showinfo("Matched","Security question and answer matched.")
                self.update_new_pass()
        except Exception as er:
            messagebox.showerror("Error",f"Error due to {str(er)}",parent=self.root)

    def update_new_pass(self):
        self.root4=Tk()
        self.root4.geometry("500x400+450+130")
        self.root4.title("Enter New Password")
        self.root4.config(bg="white")
        self.root4.focus_force()


        security_label=Label(self.root4,text="Enter new password",font=("times new roman",18,"bold"),bg="white",fg="green").place(x=100,y=10)

        password_label=Label(self.root4,text="New Password",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=80,y=60)
        self.new_password_text=Entry(self.root4,bg="lightgray",font=("times new roman",13))
        self.new_password_text.place(x=80,y=100,width=250)
        cpassword_label=Label(self.root4,text="Confirm New Password",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=80,y=150)
        self.new_cpassword_text=Entry(self.root4,bg="lightgray",font=("times new roman",13))
        self.new_cpassword_text.place(x=80,y=190,width=250)
    
        submit_btn=Button(self.root4,text="Reset",command=self.sub_new_pass,bg="lightgray",fg="green",font=("times new roman",12,"bold")).place(x=80,y=240)

    def sub_new_pass(self):
        print(self.email_txt.get(),self.nCombobx_text.get(),self.nanswer_text.get())
        
        if self.new_password_text.get()!=self.new_cpassword_text.get():
            messagebox.showerror("Error","Password and confirm Password should be same.",parent=self.root4)
        elif len(self.new_password_text.get())<8:
            messagebox.showerror("Error","Password length should be atleast 8.",parent=self.root4)
        
        else:
            try:
                con=mysql.connector.connect(host='localhost',user='root',password='admin',database='login')
                cur=con.cursor()
                cur.execute('select * from register where email=%s and question=%s and answer=%s',(self.email_txt.get(),self.nCombobx_text.get(),self.nanswer_text.get()))
                row=cur.fetchone()
                if row=="":
                    messagebox.showerror("Error","Enter correct details.",parent=self.root4)
                else:
                    cur.execute("UPDATE `register` SET password=%s WHERE email=%s",(self.new_password_text.get(),self.email_txt.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password reset successfully")
                    self.root2.destroy()
                    self.root3.destroy()
                    self.root4.destroy()

            except Exception as er:
                messagebox.showerror("Error",f"Error due to {str(er)}.",parent=self.root4)

    
    def login(self):
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='admin',database='login')
            cur=con.cursor()
            cur.execute('select * from register where email=%s and password=%s',(self.email_txt.get(),self.password_txt.get()))
            row=cur.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Wrong Email or Password",parent=self.root)
            else:
                messagebox.showinfo("Success","Login Successful",parent=self.root)
                self.root.destroy()
                import employee
        except Exception as er:
            messagebox.showerror("Error",f"Error due to {str(er)}",parent=self.root)

root=Tk()
log=SignIn(root)
root.mainloop()