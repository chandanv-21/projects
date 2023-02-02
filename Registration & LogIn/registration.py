from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
class Registration:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.var_check=IntVar()
        ##=============BackGrounf Image
        self.bg=ImageTk.PhotoImage(file='Images/bg1.jpg')
        bg=Label(self.root, image=self.bg).place(x=200,y=0,relheight=1,relwidth=1)
        self.bg2=ImageTk.PhotoImage(file='Images/bg2.jpg')
        bg2=Label(self.root, image=self.bg2)
        bg2.place(x=80,y=100,height=500,width=478)

        #Form Frame++++++++++++++++++++++++++++++++++++
        formFrame=Frame(self.root,bg="white")
        formFrame.place(x=559,y=100,relwidth=1,height=500)
        form_labe=Label(formFrame,text="REGISTER HERE",bg="white",fg="green",font=("time new roman",25,"bold")).place(x=80,y=30)

        # FormLabel and entries===============
        # row 1 ===================
        fname_label=Label(formFrame,text="First Name",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=80,y=100)
        self.fname_text=Entry(formFrame,bg="lightgray",font=("times new roman",13))
        self.fname_text.place(x=80,y=130,width=250)
        lname_label=Label(formFrame,text="First Name",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=450,y=100)
        self.lname_text=Entry(formFrame,bg="lightgray",font=("times new roman",13))
        self.lname_text.place(x=450,y=130,width=250)

        # row 2 ===================
        contact_label=Label(formFrame,text="Contact No.",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=80,y=170)
        self.contact_text=Entry(formFrame,bg="lightgray",font=("times new roman",13))
        self.contact_text.place(x=80,y=200,width=250)
        Email_label=Label(formFrame,text="Email",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=450,y=170)
        self.Email_text=Entry(formFrame,bg="lightgray",font=("times new roman",13))
        self.Email_text.place(x=450,y=200,width=250)

        # row 3 ===================
        securityQ_label=Label(formFrame,text="Security Question",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=80,y=240)
        self.Combobx_text=ttk.Combobox(formFrame,font=("times new roman",13),state="readonly",justify=CENTER)
        self.Combobx_text['values']=("Select","Name of first school.","Name of childhood friend","Name of birth place","First phone purchased")
        self.Combobx_text.place(x=80,y=270,width=250)
        self.Combobx_text.current(0)
        answer_label=Label(formFrame,text="Answer",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=450,y=240)
        self.answer_text=Entry(formFrame,bg="lightgray",font=("times new roman",13))
        self.answer_text.place(x=450,y=270,width=250)

        # row 4 ===================
        password_label=Label(formFrame,text="Password",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=80,y=310)
        self.password_text=Entry(formFrame,bg="lightgray",font=("times new roman",13))
        self.password_text.place(x=80,y=340,width=250)
        cpassword_label=Label(formFrame,text="Confirm Password",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=450,y=310)
        self.cpassword_text=Entry(formFrame,bg="lightgray",font=("times new roman",13))
        self.cpassword_text.place(x=450,y=340,width=250)
        checkbox=Checkbutton(formFrame,text="I agree with terms and condition.",variable=self.var_check,onvalue=1,offvalue=0,font=("times new roman",12),bg="white").place(x=80,y=380)
        submit_btn=Button(formFrame,text="Register Now →",command=self.register,bg="lightgray",fg="green",font=("times new roman",12,"bold")).place(x=80,y=430)

        login_btn=Button(self.root,text="Sign In",command=self.login,bg="white",font=("times new roman",14,"bold"),cursor="hand2").place(x=260,y=430,width=100)
    def clear(self):
        self.fname_text.delete(0,END)
        self.lname_text.delete(0,END)
        self.contact_text.delete(0,END)
        self.Email_text.delete(0,END)
        self.Combobx_text.current(0)
        self.answer_text.delete(0,END)
        self.password_text.delete(0,END)
        self.cpassword_text.delete(0,END)
        self.var_check.set(0)

    def login(self):
        self.root.destroy()
        import login
        
    def register(self):
        if self.fname_text.get()=="" or self.lname_text.get()=="" or self.contact_text.get()=="" or self.Email_text.get()=="" or self.Combobx_text.get()=="Select" or self.answer_text.get()=="" or self.password_text.get()=="" or self.cpassword_text.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.password_text.get()!=self.cpassword_text.get():
            messagebox.showerror("Error","Password and Confirm  Password must be same",parent=self.root)
        elif len(str(self.password_text.get()))<8:
            messagebox.showerror("Error","Password length should be atleast 8.",parent=self.root)
        elif self.var_check.get()!=1:
            messagebox.showerror("Error","Please Agree to the terms and conditions.",parent=self.root)

        else:
            try:
                con=mysql.connector.connect(host='localhost',user='root',password='admin',database='login')
                cur=con.cursor()
                cur.execute("select * from register where email=%s",(self.Email_text.get(),))
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","User already exists,Please try with another email ID.",parent=self.root)
                else:
                    cur.execute("insert into register (fname,lname,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",(self.fname_text.get(),
                                self.lname_text.get(),
                                self.contact_text.get(),
                                self.Email_text.get(),
                                self.Combobx_text.get(),
                                self.answer_text.get(),
                                self.password_text.get()))
                    con.commit()
                    con.close()

                    messagebox.showinfo("Success","Registration Successful",parent=self.root)
                    self.clear() 
            
            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)





root=Tk()
obj=Registration(root)
root.mainloop()
