#importing libraries
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

# create class 
class visitors:
    def __init__(self, window):
        self.window=window
        self.window.geometry("1530x790+0+0") #window creation
        self.window.title("Sir Padampat Singhania University") #title of project

        lbl_title=Label(self.window,text="VISITORS MANAGEMENT SYSTEM", font=("times new roman",37,"bold"),fg="darkblue", bg="white")
        lbl_title.place(x=0, y=0, width=1530,height=50)  # measurement and display on screen 

        img1=Image.open("images/Spsu_logo.jpg")      # logo setting and resizing 
        img1=img1.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img1)

        self.logo=Label(self.window,image=self.photo_logo)
        self.logo.place(x=280,y=0,width=50,height=50)

        # image frame 
        img_frame=Frame(self.window, bd=2,relief=RIDGE, bg="white") 
        img_frame.place(x=0,y=50, width=1530,height=180)

        # 1st image
        img1=Image.open("images/v1.png")      
        img1=img1.resize((540,180),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=180)

         # 2nd image
        img2=Image.open("images/v2.png")      
        img2=img2.resize((540,180),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=180)

        # 3rd image
        img3=Image.open("images/v3.jpg")      
        img3=img3.resize((540,180),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=180)

        #main frame 
        main_frame=Frame(self.window, bd=2,relief=RIDGE, bg="white") 
        main_frame.place(x=10,y=240, width=1500,height=560)

        # upper frame
        upper_frame=LabelFrame(main_frame, bd=2,relief=RIDGE, bg="white",text="Visitors Details",font=("times new roman",11,"bold"),fg="red") 
        upper_frame.place(x=10,y=10, width=1480,height=270)

         # labels and entryfields
        #  department
        lbl_dep=Label(upper_frame,text="Department",font=("arial",11,"bold"), bg="white")
        lbl_dep.grid(row=0,column=0,padx=0,sticky=W)

        Combo_dep=ttk.Combobox(upper_frame,font=("arial",12,),width=17,state="readonly" )
        Combo_dep["value"]=("select departmrnt","School of Engineering","school of Management")
        Combo_dep.current(0)
        Combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # name 
        lbl_name=Label(upper_frame,font=("arial",12,"bold"),text="Name:", bg="white")
        lbl_name.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        
        txt_name=ttk.Entry(upper_frame,width=22,font=("arial",11, "bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #Employee designation whom the client want to meet
        lbl_designation=Label(upper_frame,font=("arial",12,"bold"),text="Emp_Designation:", bg="white")
        lbl_designation.grid(row=1,column=0,padx=2,pady=7,sticky=W)
        
        txt_designation=ttk.Entry(upper_frame,width=22,font=("arial",11, "bold"))
        txt_designation.grid(row=1,column=1,padx=2,pady=7)

        # email
        lbl_email=Label(upper_frame,font=("arial",12,"bold"),text="Email:", bg="white")
        lbl_email.grid(row=3,column=0,padx=2,pady=7,sticky=W)
        
        txt_email=ttk.Entry(upper_frame,width=22,font=("arial",11, "bold"))
        txt_email.grid(row=3,column=1,padx=2,pady=7)

        #address
        lbl_address=Label(upper_frame,font=("arial",12,"bold"),text="Address:", bg="white")
        lbl_address.grid(row=2,column=0,padx=2,pady=7,sticky=W)
        
        txt_address=ttk.Entry(upper_frame,width=22,font=("arial",11, "bold"))
        txt_address.grid(row=2,column=1,padx=2,pady=7)

        # phone number

        lbl_num=Label(upper_frame,font=("arial",12,"bold"),text="Phone NO:", bg="white")
        lbl_num.grid(row=4,column=0,padx=2,pady=7,sticky=W)
        
        txt_num=ttk.Entry(upper_frame,width=22,font=("arial",11, "bold"))
        txt_num.grid(row=4,column=1,padx=2,pady=7)

        # Maritial ststus
        lbl_married=Label(upper_frame,text="Maritial Status:",font=("arial",12,"bold"), bg="white")
        lbl_married.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        Combo_married=ttk.Combobox(upper_frame,font=("arial",12,),width=18,state="readonly" )
        Combo_married["value"]=("select","Married","Unmarried")
        Combo_married.current(0)
        Combo_married.grid(row=1,column=3,padx=2,pady=7,sticky=W)

        # gender
        lbl_gender=Label(upper_frame,text="Gender:",font=("arial",12,"bold"), bg="white")
        lbl_gender.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        Combo_gender=ttk.Combobox(upper_frame,font=("arial",12,),width=18,state="readonly" )
        Combo_gender["value"]=("select","Male","Female","Other")
        Combo_gender.current(0)
        Combo_gender.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        # DOB 
        lbl_dob=Label(upper_frame,font=("arial",12,"bold"),text="DOB:", bg="white")
        lbl_dob.grid(row=3,column=2,padx=2,pady=7,sticky=W)
        
        txt_dob=ttk.Entry(upper_frame,width=22,font=("arial",11, "bold"))
        txt_dob.grid(row=3,column=3,padx=2,pady=7)

        # id proof
        lbl_ip=Label(upper_frame,text="ID Proof:",font=("arial",12,"bold"), bg="white")
        lbl_ip.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        Combo_ip=ttk.Combobox(upper_frame,font=("arial",12,),width=18,state="readonly" )
        Combo_ip["value"]=("select","pan","Aadhar","driving lisence","voter id")
        Combo_ip.current(0)
        Combo_ip.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        # purpose
        lbl_pr=Label(upper_frame,font=("arial",12,"bold"),text="Purpose:", bg="white")
        lbl_pr.grid(row=0,column=4,padx=2,pady=7,sticky=W)
        
        txt_pr=ttk.Entry(upper_frame,width=22,font=("arial",11, "bold"))
        txt_pr.grid(row=0,column=5,padx=2,pady=7)

        # head count
        lbl_hc=Label(upper_frame,font=("arial",12,"bold"),text="Head Count:", bg="white")
        lbl_hc.grid(row=1,column=4,padx=2,pady=7,sticky=W)
        
        txt_hc=ttk.Entry(upper_frame,width=22,font=("arial",11, "bold"))
        txt_hc.grid(row=1,column=5,padx=2,pady=7)

        # country
        lbl_ct=Label(upper_frame,font=("arial",12,"bold"),text="Country:", bg="white")
        lbl_ct.grid(row=2,column=4,padx=2,pady=7,sticky=W)
        
        txt_ct=ttk.Entry(upper_frame,width=22,font=("arial",11, "bold"))
        txt_ct.grid(row=2,column=5,padx=2,pady=7)

        # mask image 
        img4=Image.open("images/v4.jfif")      
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img4)

        self.img_4=Label(upper_frame,image=self.photo4)
        self.img_4.place(x=1000,y=0,width=220,height=220)

        # button frame
        button_frame=Frame(upper_frame, bd=2,relief=RIDGE, bg="white") 
        button_frame.place(x=1290,y=10, width=170,height=210)

        # adding buttons

        btn_add=Button(button_frame,text="Save",font=("arial",15, "bold"),width=13,bg="blue",fg="white")
        btn_add.grid(row=0, column=0,padx=1,pady=5)

        btn_update=Button(button_frame,text="Update",font=("arial",15, "bold"),width=13,bg="blue",fg="white")
        btn_update.grid(row=1, column=0,padx=1,pady=5)

        btn_delete=Button(button_frame,text="Delete",font=("arial",15, "bold"),width=13,bg="blue",fg="white")
        btn_delete.grid(row=2, column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,text="Clear",font=("arial",15, "bold"),width=13,bg="blue",fg="white")
        btn_clear.grid(row=3, column=0,padx=1,pady=5)



       # down frame
        down_frame=LabelFrame(main_frame, bd=2,relief=RIDGE, bg="white",text="Visitors Details table",font=("times new roman",11,"bold"),fg="red") 
        down_frame.place(x=10,y=280, width=1480,height=270)

       # search frame
        search_frame=LabelFrame(down_frame, bd=2,relief=RIDGE, bg="white",text="Search about visitor",font=("times new roman",11,"bold"),fg="blue") 
        search_frame.place(x=0,y=0, width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",fg="white", bg="red")
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        # search
        Combo_ts=ttk.Combobox(search_frame,font=("arial",12,),width=18,state="readonly" )
        Combo_ts["value"]=("select option","name","phone")
        Combo_ts.current(0)
        Combo_ts.grid(row=0,column=1,padx=5,sticky=W)

        txt_search=ttk.Entry(search_frame,width=22,font=("arial",11, "bold"))  #entry field
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text="search",font=("arial",11, "bold"),width=14, fg="white",bg="blue")
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(search_frame,text="Show all",font=("arial",11, "bold"),width=14,bg="blue",fg="white")
        btn_ShowAll.grid(row=0,column=4,padx=5)

        welcome=Label(search_frame,text="WELCOME TO SPSU",font=("Times new roman",15, "bold"),fg="green")
        welcome.place(x=780,y=0,width=600,height=30)

        # data table of visitor
        # table frame
        table_frame=Frame(down_frame, bd=3,relief=RIDGE) 
        table_frame.place(x=0,y=60, width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.visitors_table=ttk.Treeview(table_frame,column=("dep","empd","addres","email","phone","name","married","gender","dob","idp","purpose","hdc","cntry"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.visitors_table.xview)
        scroll_y.config(command=self.visitors_table.yview)

        self.visitors_table.heading("dep",text="Department")
        self.visitors_table.heading("empd",text="Emp_designation")
        self.visitors_table.heading("addres",text="Address")
        self.visitors_table.heading("email",text="Email")
        self.visitors_table.heading("phone",text="Phone no.")
        self.visitors_table.heading("name",text="Name")
        self.visitors_table.heading("married",text="Maritial Status")
        self.visitors_table.heading("gender",text="Gender")
        self.visitors_table.heading("dob",text="DOB")
        self.visitors_table.heading("idp",text="ID Proof")
        self.visitors_table.heading("purpose",text="Purpose")
        self.visitors_table.heading("hdc",text="Head count")
        self.visitors_table.heading("cntry",text="Country")

        self.visitors_table["show"]="headings"
        self.visitors_table.column("empd",width=120)
        self.visitors_table.column("addres",width=100)
        self.visitors_table.column("email",width=150)
        self.visitors_table.column("phone",width=100)
        self.visitors_table.column("name",width=100)
        self.visitors_table.column("married",width=100)
        self.visitors_table.column("gender",width=100)
        self.visitors_table.column("dob",width=100)
        self.visitors_table.column("idp",width=100)
        self.visitors_table.column("purpose",width=100)
        self.visitors_table.column("hdc",width=100)
        self.visitors_table.column("cntry",width=100)
        self.visitors_table

        self.visitors_table.pack(fill=BOTH,expand=1)


        

        

        












        
        




#closing window
if __name__=="__main__":  
    window=Tk()
    obj = visitors(window)
    window.mainloop()