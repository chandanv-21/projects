from tkinter import *
from tkinter import messagebox,ttk
import mysql.connector
import time
import os
import tempfile

class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee payroll management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Employee Payroll Management System",font=("times new roman",30,"bold"),bg="gray",anchor="w").place(x=0,y=0,relwidth=1)
        allEmp_btn=Button(self.root,text="All Employees",command=self.all_employees,bd=4,relief=GROOVE,bg="lightblue",fg="black",font=("times new roman",15,"bold")).place(x=1100,y=5)

        #+++++++++++++ Frame1++++++++++++++++++++++++
        #+++++++++++++ Variables ++++++++++++++++++++
        self.var_emp_code=StringVar()
        self.var_emp_designation=StringVar()
        self.var_emp_doj=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_dob=StringVar()
        self.var_emp_age=StringVar()
        self.var_emp_exp=StringVar()
        self.var_emp_gender=StringVar()   
        self.var_emp_ID=StringVar()
        self.var_emp_email=StringVar()
        self.var_emp_contact=StringVar()
        self.var_emp_hireloc=StringVar()
        self.var_emp_status=StringVar()
        # self.var_emp_address=StringVar()
     

        f1=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        f1.place(x=10,y=60,width=600,height=630)
        title=Label(f1,text="Employee Details",font=("times new roman",20,"bold"),bg="lightgray",fg="black",anchor="w").place(x=0,y=0,relwidth=1)
        
        code_lable=Label(f1,text="Employee Code:",bg="white",font=("times new roman",18)).place(x=20,y=70)

        self.code_Entry=Entry(f1,textvariable=self.var_emp_code,bd=3,relief=SUNKEN,font=("times new roman",15))
        self.code_Entry.place(x=200,y=70)

        search_btn=Button(f1,text="Search",command=self.search,bd=4,relief=GROOVE,font=("times new roman",12,"bold")).place(x=430,y=69)

        Design_lable=Label(f1,text="Designation:",bg="white",font=("times new roman",15)).place(x=10,y=120)
        Design_Entry=Entry(f1,textvariable=self.var_emp_designation,bd=3,relief=SUNKEN).place(x=150,y=120)

        DOJ_lable=Label(f1,text="DOJ.:",bg="white",font=("times new roman",15)).place(x=290,y=120)
        DOJ_Entry=Entry(f1,textvariable=self.var_emp_doj,bd=3,relief=SUNKEN).place(x=420,y=120)

        Name_lable=Label(f1,text="Name:",bg="white",font=("times new roman",15)).place(x=10,y=170)
        Name_Entry=Entry(f1,textvariable=self.var_emp_name,bd=3,relief=SUNKEN).place(x=150,y=170)

        DOB_lable=Label(f1,text="DOB.:",bg="white",font=("times new roman",15)).place(x=290,y=170)
        DOB_Entry=Entry(f1,textvariable=self.var_emp_dob,bd=3,relief=SUNKEN).place(x=420,y=170)

        Age_lable=Label(f1,text="Age:",bg="white",font=("times new roman",15)).place(x=10,y=220)
        Age_Entry=Entry(f1,textvariable=self.var_emp_age,bd=3,relief=SUNKEN).place(x=150,y=220)
        Exp_lable=Label(f1,text="Experiance.:",bg="white",font=("times new roman",15)).place(x=290,y=220)
        Exp_Entry=Entry(f1,textvariable=self.var_emp_exp,bd=3,relief=SUNKEN).place(x=420,y=220)

        Gender_lable=Label(f1,text="Gender:",bg="white",font=("times new roman",15)).place(x=10,y=270)
        Gender_Entry=Entry(f1,textvariable=self.var_emp_gender,bd=3,relief=SUNKEN).place(x=150,y=270)
        ID_lable=Label(f1,text="ID Proof:",bg="white",font=("times new roman",15)).place(x=290,y=270)
        ID_Entry=Entry(f1,textvariable=self.var_emp_ID,bd=3,relief=SUNKEN).place(x=420,y=270)

        email_lable=Label(f1,text="Email:",bg="white",font=("times new roman",15)).place(x=10,y=320)
        email_Entry=Entry(f1,textvariable=self.var_emp_email,bd=3,relief=SUNKEN).place(x=150,y=320)
        cont_lable=Label(f1,text="Contact No.:",bg="white",font=("times new roman",15)).place(x=290,y=320)
        cont_Entry=Entry(f1,textvariable=self.var_emp_contact,bd=3,relief=SUNKEN).place(x=420,y=320)


        location_lable=Label(f1,text="Hire Location:",bg="white",font=("times new roman",15)).place(x=10,y=370)
        location_Entry=Entry(f1,textvariable=self.var_emp_hireloc,bd=3,relief=SUNKEN).place(x=150,y=370)
        status_lable=Label(f1,text="Status:",bg="white",font=("times new roman",15)).place(x=290,y=370)
        status_Entry=Entry(f1,textvariable=self.var_emp_status,bd=3,relief=SUNKEN).place(x=420,y=370)

        address_lable=Label(f1,text="Address:",bg="white",font=("times new roman",15)).place(x=10,y=420)
        self.address_entry=Text(f1,bd=3,relief=SUNKEN,font=("times new roman",12),bg="lightyellow")
        self.address_entry.place(x=150,y=420,width=400,height=150)

        #+++++++++++++ Frame2++++++++++++++++++++++++
        #+++++++++++++ Variables ++++++++++++++++++++
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_basic=StringVar()
        self.var_tdays=StringVar()
        self.var_abscent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()   
        self.var_netsal=StringVar()
        
        f2=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        f2.place(x=620,y=60,width=680,height=315)
        title=Label(f2,text="Salary Details",font=("times new roman",20,"bold"),bg="lightgray",fg="black",anchor="w").place(x=0,y=0,relwidth=1)
        month_lable=Label(f2,text="Month:",bg="white",font=("times new roman",15)).place(x=5,y=60)
        month_Entry=Entry(f2,textvariable=self.var_month,bd=3,relief=SUNKEN).place(x=120,y=60,width=100)
        year_lable=Label(f2,text="Year:",bg="white",font=("times new roman",15)).place(x=240,y=60)
        year_Entry=Entry(f2,textvariable=self.var_year,bd=3,relief=SUNKEN).place(x=300,y=60,width=100)
        basicsal_lable=Label(f2,text="Basic Salary:",bg="white",font=("times new roman",15)).place(x=420,y=60)
        basicsal_Entry=Entry(f2,textvariable=self.var_basic,bd=3,relief=SUNKEN).place(x=550,y=60,width=100)

        day_lable=Label(f2,text="Total Days:",bg="white",font=("times new roman",15)).place(x=5,y=110)
        day_Entry=Entry(f2,textvariable=self.var_tdays,bd=3,relief=SUNKEN).place(x=120,y=110)
        abs_lable=Label(f2,text="Abscent:",bg="white",font=("times new roman",15)).place(x=300,y=110)
        abs_Entry=Entry(f2,textvariable=self.var_abscent,bd=3,relief=SUNKEN).place(x=450,y=110)


        med_lable=Label(f2,text="Medical:",bg="white",font=("times new roman",15)).place(x=5,y=160)
        med_Entry=Entry(f2,textvariable=self.var_medical,bd=3,relief=SUNKEN).place(x=120,y=160)
        pf_lable=Label(f2,text="Providet Fund:",bg="white",font=("times new roman",15)).place(x=300,y=160)
        pf_Entry=Entry(f2,textvariable=self.var_pf,bd=3,relief=SUNKEN).place(x=450,y=160)

        conve_lable=Label(f2,text="Convence:",bg="white",font=("times new roman",15)).place(x=5,y=210)
        conve_Entry=Entry(f2,textvariable=self.var_convence,bd=3,relief=SUNKEN).place(x=120,y=210)
        netsal_lable=Label(f2,text="Net Salary:",bg="white",font=("times new roman",15)).place(x=300,y=210)
        netsal_Entry=Entry(f2,textvariable=self.var_netsal,bd=3,relief=SUNKEN).place(x=450,y=210)

        calculate_btn=Button(f2,text="Calculate",command=self.sal_calculate,bd=4,relief=GROOVE,bg="lightgreen",font=("times new roman",15,"bold")).place(x=10,y=260)
        self.generate_slip_btn=Button(f2,text="Generate Slip",command=self.salary_slip,state=DISABLED,bd=4,relief=GROOVE,bg="yellow",font=("times new roman",15,"bold"))
        self.generate_slip_btn.place(x=135,y=260)
        self.update_btn=Button(f2,text="Update",command=self.update,state=DISABLED,bd=4,relief=GROOVE,bg="lightblue",font=("times new roman",15,"bold"))
        self.update_btn.place(x=295,y=260)
        self.save_btn=Button(f2,text="Save",command=self.save_data,bd=4,relief=GROOVE,bg="orange",font=("times new roman",15,"bold"))
        self.save_btn.place(x=400,y=260)
        self.delete_btn=Button(f2,text="Delete",command=self.delete,state=DISABLED,bd=4,relief=GROOVE,bg="brown",font=("times new roman",15,"bold"))
        self.delete_btn.place(x=490,y=260)
        clear_btn=Button(f2,text="Clear",command=self.clear_btn,bd=4,relief=GROOVE,bg="red",font=("times new roman",15,"bold")).place(x=590,y=260)

        

        #+++++++++++++ Frame3++++++++++++++++++++++++
        f3=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        f3.place(x=620,y=378,width=680,height=315)

        #+++++++++++++Calculator frame+++++++++++++++
        self.var_txt=StringVar()
        self.var_oprator=""
        def btn_click(num):
            self.var_oprator=self.var_oprator+str(num)
            self.var_txt.set(self.var_oprator)

        def calculate():
            res=str(eval(self.var_oprator))
            self.var_txt.set(res)
            self.var_oprator=""


        f31=Frame(f3,bd=5,relief=RIDGE,bg="white")
        f31.place(x=0,y=0,width=251,height=306)
        txt_result= Entry(f31,textvariable=self.var_txt,bg="light yellow",font=("times new roman",30,"bold"),justify=RIGHT).place(x=0,y=0,relwidth=1)
        btn_7=Button(f31,text="7",command=lambda:btn_click("7"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=0,y=58,width=60,height=60)
        btn_8=Button(f31,text="8",command=lambda:btn_click("8"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=61,y=58,width=60,height=60)
        btn_9=Button(f31,text="9",command=lambda:btn_click("9"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=122,y=58,width=60,height=60)
        btn_div=Button(f31,text="/",command=lambda:btn_click("/"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=183,y=58,width=60,height=60)

        btn_4=Button(f31,text="4",command=lambda:btn_click("4"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=0,y=118,width=60,height=60)
        btn_5=Button(f31,text="5",command=lambda:btn_click("5"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=61,y=118,width=60,height=60)
        btn_6=Button(f31,text="6",command=lambda:btn_click("6"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=122,y=118,width=60,height=60)
        btn_mul=Button(f31,text="*",command=lambda:btn_click("*"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=183,y=118,width=60,height=60)

        btn_1=Button(f31,text="1",command=lambda:btn_click("1"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=0,y=178,width=60,height=60)
        btn_2=Button(f31,text="2",command=lambda:btn_click("2"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=61,y=178,width=60,height=60)
        btn_3=Button(f31,text="3",command=lambda:btn_click("3"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=122,y=178,width=60,height=60)
        btn_minus=Button(f31,text="-",command=lambda:btn_click("-"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=183,y=178,width=60,height=60)

        btn_point=Button(f31,text=".",command=lambda:btn_click("."),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=0,y=238,width=60,height=60)
        btn_0=Button(f31,text="0",command=lambda:btn_click("0"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=61,y=238,width=60,height=60)
        btn_plus=Button(f31,text="+",command=lambda:btn_click("+"),font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=122,y=238,width=60,height=60)
        btn_equals=Button(f31,text="=",command=calculate,font=("times new roman",20),bg="pink",bd=2,relief=GROOVE).place(x=183,y=238,width=60,height=60)

        #+++++++++++++ Salary Receipt frame ++++++++++++++++
        f32=Frame(f3,bd=5,relief=RIDGE,bg="white")
        f32.place(x=252,y=0,width=418,height=306)

        title=Label(f32,text="Salary Reciept",font=("times new roman",20,"bold"),bg="lightgray",fg="black",anchor="w").place(x=0,y=0,relwidth=1)
        sal_frame=Frame(f32,bg="white",bd=2,relief=RIDGE)
        sal_frame.place(x=0,y=38,relwidth=1,height=225)

        
        self.receipt_sample=f'''\t\tCompany Name, XYZ\n\t\tAddress: XYZ,abc Road
            --------------------------------------------------
            Employee ID\t\t:  -----
            Employee Name\t\t:  -----
            Salary of\t\t:  MM-YYYY
            Generated on\t\t:  DD-MM-YYYY
            --------------------------------------------------
            Total Days\t\t:  -----
            Present Days\t\t:  -----
            Absent Days\t\t:  -----
            Convence\t\t:  -----
            Medical\t\t:  -----
            PF\t\t:  -----
            Gross Payment\t\t:  -----
            Net Salary\t\t:  -----
            --------------------------------------------------
            This is a system generated receipt.
            No signature required.

    '''
        scroly=Scrollbar(sal_frame,orient=VERTICAL)
        scroly.pack(fill=Y,side=RIGHT)

        self.sal_text=Text(sal_frame,font=("times new roman",12),bg="lightyellow",yscrollcommand=scroly.set)
        self.sal_text.pack(fil=BOTH,expand=1)
        scroly.config(command=self.sal_text.yview)
        self.sal_text.insert(END,self.receipt_sample)


        self.print_slip=Button(f32,text="Print",command=self.print,state=DISABLED,bd=4,relief=GROOVE,bg="green",font=("times new roman",12,"bold"))
        self.print_slip.place(x=270,y=263)
        self.check_connection()


    #=============All functions are here ===================

    def sal_calculate(self):
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_basic.get()=='' or self.var_tdays.get()=='' or self.var_abscent.get()=='' or self.var_medical.get()=='' or self.var_pf.get()=='' or self.var_convence.get()=='':
            messagebox.showerror("Error","All fields are required")

        else:
            try:
                perday=int(self.var_basic.get())/int(self.var_tdays.get())
                workday=int(self.var_tdays.get())-int(self.var_abscent.get())
                sal=perday*workday
                deduct=int(int(self.var_medical.get())+int(self.var_pf.get()))
                adds=int(self.var_convence.get())
                netsal=sal+adds-deduct
                self.var_netsal.set(str(round(netsal,2)))
                self.generate_slip_btn.config(state=NORMAL)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to 235 {str(ex)}")


    def salary_slip(self):
        f_receipt=f'''\t\tCompany Name, XYZ\n\t\tAddress: XYZ,abc Road
            --------------------------------------------------
            Employee ID\t\t:  {self.var_emp_code.get()}
            Employee Name\t\t:  {self.var_emp_name.get()}
            Salary of\t\t:  {self.var_month.get()}-{self.var_year.get()}
            Generated on\t\t:  {str(time.strftime("%d-%m-%y"))}
            --------------------------------------------------
            Total Days\t\t:  {self.var_tdays.get()}
            Present Days\t\t:  {str((int(self.var_tdays.get()))-(int(self.var_abscent.get())))}
            Absent Days\t\t:  {self.var_abscent.get()}
            Convence\t\t:  {self.var_convence.get()}
            Medical\t\t:  {self.var_medical.get()}
            PF\t\t:  {self.var_pf.get()}
            Gross Payment\t\t:  {self.var_basic.get()}
            Net Salary\t\t:  {self.var_netsal.get()}
            --------------------------------------------------
            This is a system generated receipt.
            No signature required.

    '''
        self.sal_text.delete('1.0',END)
        self.sal_text.insert(END,f_receipt)
        rec=open(f"salary_receipt/{str(self.var_emp_code.get())}-{self.var_month.get()}.txt","w")
        rec.write(self.sal_text.get('1.0',END)) 
        self.print_slip.config(state=NORMAL)
        rec.close()
        
    def search(self):
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='admin',database='ems')
            cur=con.cursor()
            cur.execute("select * from emp_details where emp_id=%s",(self.var_emp_code.get(),))
            rows=cur.fetchone()
            print(rows)
            if rows==None:
                messagebox.showerror("Error","This user ID is not generated yet.",parent=self.root)

            else:
                self.var_emp_code.set(rows[0])
                self.var_emp_designation.set(rows[1])
                self.var_emp_name.set(rows[2])
                self.var_emp_age.set(rows[3])
                self.var_emp_gender.set(rows[4])
                self.var_emp_email.set(rows[5])
                self.var_emp_hireloc.set(rows[6])
                self.var_emp_doj.set(rows[7]) 
                self.var_emp_dob.set(rows[8])
                self.var_emp_exp.set(rows[9])   
                self.var_emp_ID.set(rows[10])
                self.var_emp_contact.set(rows[11]) 
                self.var_emp_status.set(rows[12])
                self.address_entry.delete('1.0',END)
                self.address_entry.insert(END,rows[13])
                self.var_month.set(rows[14])
                self.var_year.set(rows[15])
                self.var_basic.set(rows[16])
                self.var_tdays.set(rows[17])
                self.var_abscent.set(rows[18])
                self.var_medical.set(rows[19])
                self.var_pf.set(rows[20])
                self.var_convence.set(rows[21])   
                self.var_netsal.set(rows[22])
                file1=open(f"salary_receipt/{str(rows[23])}","r")
                self.sal_text.delete('1.0',END)
                for i in file1:
                    self.sal_text.insert(END,i)
                file1.close()
                self.save_btn.config(state=DISABLED)
                self.update_btn.config(state=NORMAL)
                self.delete_btn.config(state=NORMAL)
                self.code_Entry.config(state='readonly')
                self.print_slip.config(state=NORMAL)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to  313 {str(ex)}")
    #===========Delete Function ==================
    def delete(self):
        if self.var_emp_code.get()=="":
            messagebox.showerror("Error","This ID is not available.")
        else:
            try:
                con=mysql.connector.connect(host='localhost',user='root',password='admin',database='ems')
                cur=con.cursor()
                cur.execute("select * from emp_details  where emp_id=%s",(self.var_emp_code.get(),))
                rows=cur.fetchone()
                # print(rows)
                if rows==None:
                    messagebox.showerror("Error","This ID is not available.",parent=self.root)

                else:
                    op= messagebox.askyesno("Confirm","Do you really want to delete this data?")
                    if op==True:
                        cur.execute("delete from emp_details where emp_id=%s",(self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","Data deleted successfully")

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to 337 {str(ex)}")

    #============== Save Function ==================
    def save_data(self):
        if self.var_emp_code.get()=="" or self.var_emp_name.get()=="" or self.var_month.get()=='' or self.var_year.get()=='' or self.var_basic.get()=='' or self.var_tdays.get()=='' or self.var_abscent.get()=='' or self.var_medical.get()=='' or self.var_pf.get()=='' or self.var_convence.get()=='':
            messagebox.showerror("Error","All fields are required")

        else:
            try:
                con=mysql.connector.connect(host='localhost',user='root',password='admin',database='ems')
                cur=con.cursor()
                cur.execute("select * from emp_details  where emp_id=%s",(self.var_emp_code.get(),))
                rows=cur.fetchone()
                # print(rows)
                if rows!=None:
                    messagebox.showerror("Error","This Employee ID is already available in our record.",parent=self.root)
                else:
                    cur.execute("insert into emp_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (   self.var_emp_code.get(),
                        self.var_emp_designation.get(),
                        self.var_emp_name.get(),
                        self.var_emp_age.get(),
                        self.var_emp_gender.get(),
                        self.var_emp_email.get(),
                        self.var_emp_hireloc.get(),
                        self.var_emp_doj.get(), 
                        self.var_emp_dob.get(),
                        self.var_emp_exp.get(),   
                        self.var_emp_ID.get(),
                        self.var_emp_contact.get(), 
                        self.var_emp_status.get(),
                        self.address_entry.get('1.0',END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_basic.get(),
                        self.var_tdays.get(),
                        self.var_abscent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),   
                        self.var_netsal.get(),
                        f"{str((self.var_emp_code.get()))}-{self.var_month.get()}.txt"
                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Data Added Successfully")
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to 385 {str(ex)}")

    def update(self):
            try:
                con=mysql.connector.connect(host='localhost',user='root',password='admin',database='ems')
                cur=con.cursor()
                cur.execute("select * from emp_details  where emp_id=%s",(self.var_emp_code.get(),))
                rows=cur.fetchone()
                # print(rows)
                if rows==None:
                    messagebox.showerror("Error","This Employee ID is invalid.Try again with valid Employee ID.",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_details` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hire_loc`=%s,`DOJ`=%s,`DOB`=%s,`experience`=%s,`id_proof`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`total_days`=%s,`abscent`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s,`salry_receipt`=%s WHERE `emp_id`=%s",
                    (   self.var_emp_designation.get(),
                        self.var_emp_name.get(),
                        self.var_emp_age.get(),
                        self.var_emp_gender.get(),
                        self.var_emp_email.get(),
                        self.var_emp_hireloc.get(),
                        self.var_emp_doj.get(), 
                        self.var_emp_dob.get(),
                        self.var_emp_exp.get(),   
                        self.var_emp_ID.get(),
                        self.var_emp_contact.get(), 
                        self.var_emp_status.get(),
                        self.address_entry.get('1.0',END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_basic.get(),
                        self.var_tdays.get(),
                        self.var_abscent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),   
                        self.var_netsal.get(),
                        f"{str((self.var_emp_code.get()))}-{self.var_month.get()}.txt",
                        self.var_emp_code.get()
                    )
                    )
                    self.salary_slip()
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Data Updated Successfully")
                    self.print_slip.config(state=NORMAL)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to 430 {str(ex)}")


    def clear_btn(self):
        self.save_btn.config(state=NORMAL)
        self.update_btn.config(state=DISABLED)
        self.delete_btn.config(state=DISABLED)
        self.code_Entry.config(state=NORMAL)
        self.print_slip.config(state=DISABLED)
        
        self.var_emp_code.set('')
        self.var_emp_designation.set('')
        self.var_emp_name.set('')
        self.var_emp_age.set('')
        self.var_emp_gender.set('')
        self.var_emp_email.set('')
        self.var_emp_hireloc.set('')
        self.var_emp_doj.set('') 
        self.var_emp_dob.set('')
        self.var_emp_exp.set('')   
        self.var_emp_ID.set('')
        self.var_emp_contact.set('') 
        self.var_emp_status.set('')
        self.address_entry.delete('1.0',END)
        self.var_month.set('')
        self.var_year.set('')
        self.var_basic.set('')
        self.var_tdays.set('')
        self.var_abscent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')   
        self.var_netsal.set('')
        self.sal_text.delete('1.0',END)
        self.sal_text.insert(END,self.receipt_sample)

    def check_connection(self):
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='admin',database='ems')
            cur=con.cursor()
            cur.execute("select * from emp_details")
            rows=cur.fetchall()
            print("connected")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to 475 {str(ex)}")




    def show_data(self):
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='admin',database='ems')
            cur=con.cursor()
            cur.execute("select * from emp_details")
            rows=cur.fetchall()
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to 493 {str(ex)}")        
    def all_employees(self):
        self.root2=Toplevel(self.root)
        self.root2.title("All Employee Details")
        self.root2.geometry("1200x600+100+100")
        self.root2.config(bg="white")
        title=Label(self.root2,text="All Employee Details",font=("times new roman",20,"bold"),bg="gray",anchor="w").pack(side=TOP,fill=X)
        self.root2.focus_force()
        scrol_y=Scrollbar(self.root2,orient=VERTICAL)
        scrol_x=Scrollbar(self.root2,orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)



        self.employee_tree=ttk.Treeview(self.root2,columns=('emp_id', 'designation', 'name', 'age', 'gender', 'email', 'hire_loc', 'DOJ', 'DOB', 'experience', 'id_proof', 'contact', 'status', 'address', 'month', 'year', 'basic_salary', 'total_days', 'abscent', 'medical', 'pf', 'convence', 'net_salary', 'salry_receipt'),yscrollcommand=scrol_y.set,xscrollcommand=scrol_x.set)
        self.employee_tree.heading('emp_id',text='Emp ID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('DOB',text='D.O.B')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('contact',text='Contact No.')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('hire_loc',text='Hire Location')
        self.employee_tree.heading('DOJ',text='D.O.J.')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('id_proof',text='ID Proof\n(Aadha/PAN/Psssport)')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('basic_salary',text='Gross Salary')
        self.employee_tree.heading('total_days',text='Total Days')
        self.employee_tree.heading('abscent',text='Absent')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='PF')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('net_salary',text='Net Salry')
        self.employee_tree.heading('salry_receipt',text='Salary Receipt')

        self.employee_tree['show']='headings'

        self.employee_tree.column('emp_id',width=100)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('DOB',width=100)
        self.employee_tree.column('age',width=70)
        self.employee_tree.column('gender',width=70)
        self.employee_tree.column('email',width=150)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('address',width=500)
        self.employee_tree.column('hire_loc',width=100)
        self.employee_tree.column('DOJ',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('id_proof',width=200)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('total_days',width=100)
        self.employee_tree.column('abscent',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salry_receipt',width=100)

        scrol_x.config(command=self.employee_tree.xview)
        scrol_y.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show_data()

        self.root2.mainloop()

    def print(self):
        temp_file=tempfile.mktemp('.txt')
        open (temp_file,"w").write(self.sal_text.get('1.0',END))
        print(temp_file +"ABC")
        os.startfile(temp_file,'print')



root=Tk()
EmployeeSystem(root)
root.mainloop()