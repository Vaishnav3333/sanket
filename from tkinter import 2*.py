from tkinter import *
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
   def _init_(se)
       self.root.title("Hospital Mangement System")
       self.root.geometry("1540*800+0+0")
       
      lbl_1=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM", fg="red",bg="white",font="times new roman",50,"bold")
      lbl_1.pack(side=TOP,fill=x)



      #===========DAta frame=================
      Dataframe=Frame(self.root,bd=20,relief=RIDGE)
      Dataframe.place(x=0,y=130,width=1530,height=400)
      
      DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font=("arial",12,"bold"),text="Patient Intake form")
      DataframeLeft.place(x=0,y=5,width=980,height=350)
     
      DataframeRight=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font=("arial",12,"bold"),text="All Patient Information")
      DataframeRight.place(x=990,y=5,width=460,height=350)

      # ==================== BUTTON FRAME=========================


      Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
      Buttonframe.place(X=0,Y=530,width=1530,height=70)

      #====================== Detils======================

      Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
      Detailsframe.place(x=0,y=600,width=1530,height=190)

      # ===================== DataframeLeft ===============

      lbl_DoctorName=Label(DataframeLeft,text="Names of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
      lbl_DoctorName.grid(row=0,column=0,sticky=w)
      comDoctorName=ttk.Combobox(DataframeLeft,state="readonly",font=("arial",12,"bold"),width=33)
      comDoctorName["value"]=("HG PANKAJ GOP P ","HG ADIGOPAL P ","YASH G (Intern)","AYUSH p (Intern)")
      comDoctorName.current(0)
      comDoctorName.grid(row=0,column=1)

      lblWardenName=Label(DataframeLeft,font=("arial",12,"bold"),text="Warden",padx=2,pady=6)
      lblWardenName.grid(row=3,column=0,sticky=w)
      comWardenName=ttk.Combobox(DataframeLeft,state="readonly",font=("arial",12,"bold"),width=33)
      comWardenName["value"]=("SIDDESH P","SURAJ P","NARAYAN P","VIJAY P","KRISHNAKANT P")
      comWardenName.current(0)
      comWardenName.grid(row=3,column=1)

      

      

      lblName=Label(DataframeLeft,font=("arial",12,"bold"),text="Name of Patient",padx=2)
      lblName.grid(row=1,column=0,sticky=w)
      txtName=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
      txtName.grid(row=1,column=1)
      
      lblAge=Label(DataframeLeft,font=("arial",12,"bold"),text="Age of Patient",padx=2,pady=4)
      lblAge.grid(row=2,column=0,sticky=w)
      txtAge=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
      txtAge.grid(row=2,column=1)

      lbl_Sex=Label(DataframeLeft,text="Sex of Patient",font=("times new roman",12,"bold"),padx=2,pady=6)
      lbl_Sex.grid(row=0,column=2,sticky=w)
      comSex=ttk.Combobox(DataframeLeft,state="readonly",font=("arial",12,"bold"),width=33)
      comSex["value"]=("Male","Female","LGBT","Unspecified")
      comSex.current(0)
      comSex.grid(row=0,column=3)

      
      lbl_BloodGroup=Label(DataframeLeft,text="Blood Group",font=("times new roman",12,"bold"),padx=2,pady=6)
      lbl_BloodGroup.grid(row=0,column=0,sticky=w)
      comBloodGroup=ttk.Combobox(DataframeLeft,state="readonly",font=("arial",12,"bold"),width=33)
      comBloodGroup["value"]=("A+","B+","AB+","O+","A-","B-","AB-","O-")
      comBloodGroup.current(0)
      comBloodGroup.grid(row=0,column=5)

      lblDisease=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference no.",padx=2)
      lblDisease.grid(row=4,column=0,sticky=w)
      txtDisease=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
      txtDisease.grid(row=4,column=1)

      
      lbl_Condition=Label(DataframeLeft,text="Sex of Patient",font=("times new roman",12,"bold"),padx=2,pady=6)
      lbl_Condition.grid(row=0,column=2,sticky=w)
      comCondition=ttk.Combobox(DataframeLeft,state="readonly",font=("arial",12,"bold"),width=33)
      comCondition["value"]=("Normal","Critical","Ultra Critical")
      comCondition.current(0)
      comCondition.grid(row=0,column=3)

      #==================DataframeRight=====================

      self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
      self.txtPrescription.grid(row=0,column=0)
      #==================Buttons============================

      btnUpdate=Button(Buttonframe,text="PRESCRIPTION",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
      btnUpdate.grid(row=0 ,column=0)
   
   
      btnUpdate=Button(Buttonframe,text="UPDATE",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
      btnUpdate.grid(row=0 ,column=1)

      btnDelete=Button(Buttonframe,text="DELETE",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
      btnDelete.grid(row=0 ,column=2 )

      btnCLEAR=Button(Buttonframe,text="CLEAR",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
      btnCLEAR.grid(row=0 ,column=2 )

      btnExit=Button(Buttonframe,text="EXIT",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
      btnExit.grid(row=0 ,column=2 )



      #=======================sCROLL BAR  Table===============================================

      scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
      self.hospital_table=ttk.Treeview(FrameDetails("","","","","",),column=)
      




      





      
      
      















