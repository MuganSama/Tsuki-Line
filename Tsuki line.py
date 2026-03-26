import customtkinter as ctk
from PIL import Image, ImageFilter,ImageDraw, ImageFont
import smtplib
from email.message import EmailMessage
import mysql.connector
from tkcalendar import Calendar
import datetime
from datetime import date
import random
import tempfile
import pygame
from io import BytesIO
import urllib.parse
from selenium import webdriver
import time
import os
from dotenv import load_dotenv

pygame.mixer.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play(-1)

load_dotenv()

buddha=[]  #IDENTITY
hitler=[]  #DATE
tamim=[]   #FROM AND TO
condition=1
pauseim=ctk.CTkImage(dark_image=Image.open("Holy Grail/alu1.jpg"),size=(10,10))
playim=ctk.CTkImage(dark_image=Image.open("Holy Grail/alu.jpg"),size=(10,10))
fim=playim
seat_no=[] #INFO
sql_password = os.getenv('MYSQL_PASSWORD')
email_password = os.getenv('GMAIL_APP_PASSWORD')
l = ["Sealdah Jn", "Pak Circus", "Baligange Jn", "Dhakuria", "Jadavpur", "Baghajatin", "Goria", "Narandrapur",
     "Sonarpur Jn", "Subhashgram", "Malickpur", "Baruipur Jn"]
pn=0

def player_ctrl(x):
    global condition
    global fim
    if x==0:
        pygame.mixer.music.unpause()
        condition=1
        fim=playim
    elif x==1:
        pygame.mixer.music.pause()
        condition=0
        fim=pauseim

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        window_width = 800
        window_height = 550
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        im=ctk.CTkImage(dark_image=Image.open("Holy Grail/logo.png"),size=(800,550))
        bim=ctk.CTkImage(dark_image=Image.open("Holy Grail/steam engine1.png"),size=(140,45))

        self.logo= ctk.CTkLabel(self,image=im,text="")
        self.logo.place(x=0, y=0, relwidth=1, relheight=1)
        self.xp=-300

        self.cont= ctk.CTkButton(self, text="", image=bim, border_color="black", hover_color="#DEDFD3", fg_color="black", command=self.open_Login_screen)
        self.cont.place(x=self.xp,y=495)

        self.xf=640
        self.slide()
    def slide(self):
        if self.xp<self.xf:
            self.xp+=2
            self.cont.place(x=self.xp,y=495)
            self.after(10,self.slide)
        else:
            self.cont.place(x=640, y=495)

    def open_Login_screen(self):
        self.withdraw()
        self.signin_window = Log_in(self)

def frame_crop_log(x, y, w, h):
    img = Image.open("Holy Grail/3.jpg").resize((800, 500)).crop((x+70, y+30, x+70+w,y+30+ h)).filter(ImageFilter.GaussianBlur(radius=3))
    return ctk.CTkImage(dark_image=img,size=(w,h))

def email(x,subject,body):
    msg = EmailMessage()
    msg['From'] = "tsukiline1@gmail.com"
    msg['To'] = x
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        # Send the email using Gmail SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login("tsukiline1@gmail.com", email_password)
            smtp.send_message(msg)
        print("✅ Custom email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)

class Log_in(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__( parent)

        window_width = 800
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        im = ctk.CTkImage(dark_image=Image.open("Holy Grail/3.jpg"), size=(800, 500))

        self.logo = ctk.CTkLabel(self, image=im, text="")
        self.logo.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame= ctk.CTkFrame(self,width=300,border_color="black",border_width=10,height=400)
        self.frame.place(x=70,y=50)

        self.logo = ctk.CTkLabel(self.frame, image=frame_crop_log(0, 0, 300, 400), text="")
        self.logo.place(x=7, y=7,relwidth=0.949, relheight=0.963)

        self.l = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_log(90, 50, 120, 40), text="LOG in..", font=("Algerian", 30, "bold", "underline"), anchor="w", text_color="#00FFFF")
        self.l.place(x=90, y=50)

        self.gm = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_log(10, 110, 100, 30), text="Email Id", font=("Bahnschrift Condensed", 25), anchor="w", text_color="black")
        self.gm.place(x=10, y=110 )

        self.gmi = ctk.CTkEntry(self.frame,width=260,height=30,placeholder_text="Enter your Email")
        self.gmi.place(x=20,y=150)

        self.pas = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_log(20, 190, 100, 30), text="Password", font=("Bahnschrift Condensed", 25), anchor="w", text_color="black")
        self.pas.place(x=20, y=190)

        self.pasi = ctk.CTkEntry(self.frame, width=260, height=30, placeholder_text="Enter your Password")
        self.pasi.place(x=20, y=230)

        self.logb = ctk.CTkButton(self.frame, text="Log in", border_color="black", fg_color="blue",command=self.log_check)
        self.logb.place(x=80, y=270)

        self.nu = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_log(20, 350, 150, 30), text="New User?--->", font=("Bahnschrift Condensed", 25), anchor="w", text_color="#00FFFF")
        self.nu.place(x=20, y=350)

        self.si= ctk.CTkButton(self.frame, text="Sign Up", border_color="black", fg_color="blue", width=120,command=self.open_signin_screen)
        self.si.place(x=160, y=350)

        self.warning_label = ctk.CTkLabel(self, text="", text_color="red", font=("Arial", 14))
        self.warning_label.place(x=650, y=430)

        self.pb=ctk.CTkButton(self,text="", width=10,height=10,image=fim,command=self.playfuc)
        self.pb.place(x=10,y=10)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        self.master.destroy()

    def star_mail(self):
        i=str(self.gmi.get())
        email(i,"🎉 Log in notification","You have successfully logged into your account.")
        print("alu")

    def playfuc(self):
        player_ctrl(condition)
        self.pb.configure(image=fim)

    def open_signin_screen(self):
        self.withdraw()
        self.signin_window = sign_up(self)

    def open_home_screen(self):
        self.withdraw()
        self.home_window = Home(self)

    def log_check(self):
        c=1
        global buddha
        if self.gmi.get()=="" or not self.gmi.get().rstrip().endswith("@gmail.com"):
            self.warning_label.configure(text="Incorrect Email ID")
            c = 0
        elif self.pasi.get()=="":
            self.warning_label.configure(text="Enter Password")
            c = 0

        if c==1:
            db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
            mc = db.cursor()
            J = "SELECT * FROM USER WHERE Email_ID = %s"
            I = (self.gmi.get(),)
            mc.execute(J, I)
            re = mc.fetchone()
            if re is None or re[2] != self.pasi.get():
                self.warning_label.configure(text="Incorrect Email ID or password")
                self.warning_label.place(x=600)
            else:
                self.star_mail()
                buddha = re
                print(buddha)
                self.open_home_screen()


def frame_crop_sign(i,x, y, w, h):
    img = i.crop((x+450, y+55, x+450+w,y+55+ h)).filter(ImageFilter.GaussianBlur(radius=3))
    return ctk.CTkImage(dark_image=img,size=(w,h))

class sign_up(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        window_width = 900
        window_height = 550
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        sim = Image.open("Holy Grail/5.jpg").resize((900, 550))
        imb=ctk.CTkImage(dark_image=sim,size=(900,550))

        self.bgi = ctk.CTkLabel(self, image=imb, text="")
        self.bgi.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame=ctk.CTkFrame(self,width=400,border_color="black",border_width=10,height=450)
        self.frame.place(x=450,y=55)

        self.bg=ctk.CTkLabel(self.frame,image=ctk.CTkImage(dark_image=sim.crop((450, 55, 850,510)).filter(ImageFilter.GaussianBlur(radius=3)),size=(400,450)),text="")
        self.bg.place(x=10, y=7,relwidth=0.949, relheight=0.963)

        self.l = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_sign(sim,135, 20, 120, 40), text="Sign Up",font=("Algerian", 30, "bold", "underline"), anchor="w", text_color="#00FFFF")
        self.l.place(x=135, y=20)

        self.name = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_sign(sim,20, 80, 100, 30), text="Name   ",font=("Bahnschrift Condensed", 25), anchor="w", text_color="#FFC11D")
        self.name.place(x=20, y=80)

        self.namei = ctk.CTkEntry(self.frame, width=340, height=30, placeholder_text="Enter your Name")
        self.namei.place(x=30, y=115)

        self.age = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_sign(sim, 20, 145, 100, 30),
                                 text="Age      ", font=("Bahnschrift Condensed", 25), anchor="w", text_color="#FFC11D")
        self.age.place(x=20, y=145)

        self.agei = ctk.CTkEntry(self.frame, width=340, height=30, placeholder_text="Enter your Age")
        self.agei.place(x=30, y=180)

        self.email = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_sign(sim, 20, 210, 100, 30),
                                 text="Email Id", font=("Bahnschrift Condensed", 25), anchor="w", text_color="#FFC11D")
        self.email.place(x=20, y=210)

        self.emaili = ctk.CTkEntry(self.frame, width=340, height=30, placeholder_text="Enter your Email Id")
        self.emaili.place(x=30, y=245)

        self.passw = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_sign(sim, 20, 275, 100, 30),
                                 text="   Password", font=("Bahnschrift Condensed", 25), anchor="w", text_color="#FFC11D")
        self.passw.place(x=20, y=275)

        self.passwi = ctk.CTkEntry(self.frame, width=340, height=30, placeholder_text="Enter your Password")
        self.passwi.place(x=30, y=310)

        self.si = ctk.CTkButton(self.frame, text="Sign Up", border_color="black", fg_color="blue", width=150,command=self.sign_up_check)
        self.si.place(x=125, y=390)

        self.vari=ctk.StringVar(value="None")
        self.male=ctk.CTkRadioButton(self.frame, text="Male", variable=self.vari, value="1",hover_color="#FFC11D",fg_color="#FFC11D")
        self.male.place(x=100,y=355)

        self.female = ctk.CTkRadioButton(self.frame, text="Female", variable=self.vari, value="2",hover_color="#FFC11D",fg_color="#FFC11D")
        self.female.place(x=200, y=355)

        self.warning_label = ctk.CTkLabel(self, text="", text_color="red", font=("Arial", 14))
        self.warning_label.place(x=30, y=450)

        self.re = ctk.CTkButton(self, text="<", height=20, width=20, command=self.close_window)
        self.re.place(x=5, y=5)

        self.pb = ctk.CTkButton(self, text="", width=20, height=20, image=fim, command=self.playfuc)
        self.pb.place(x=30, y=5)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        root = self.parent
        while root.master is not None:
            root = root.master
        root.destroy()

    def star_mail(self):
        i=str(self.emaili.get())
        email(i,"🎉 Sign up notification","You have successfully Signed up to our site.")
        print("alu")

    def open_home_screen(self):
        self.withdraw()
        self.home_window = Home(self)

    def playfuc(self):
        player_ctrl(condition)
        self.pb.configure(image=fim)

    def sign_up_check(self):
        c = 1
        global buddha
        if self.emaili.get() == "" or not self.emaili.get().rstrip().endswith("@gmail.com"):
            self.warning_label.configure(text="Incorrect Email ID")
            c = 0
        elif self.namei.get() == "":
            self.warning_label.configure(text="Enter Name")
            c = 0
        elif self.agei.get() == "":
            self.warning_label.configure(text="Enter Age")
            c = 0
        elif self.passwi.get() == "":
            self.warning_label.configure(text="Enter Password")
            c = 0
        elif self.vari.get() in ("", "None"):
            self.warning_label.configure(text="Enter Gender")
            c = 0

        if c==1:
            db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
            mc = db.cursor()
            J = "SELECT * FROM USER WHERE Email_ID = %s"
            I = (self.emaili.get(),)
            mc.execute(J, I)
            re = mc.fetchone()
            if re is None:
                J = "insert into USER (Email_ID, PASSWORD, NAME, AGE, GEN) values(%s,%s,%s,%s,%s)"
                gender = self.vari.get()
                if gender == "1":
                    gen = "M"
                elif gender == "2":
                    gen = "F"
                I = (self.emaili.get(), self.passwi.get(), self.namei.get(), self.agei.get(), gen)
                mc.execute(J, I)
                db.commit()
                self.star_mail()
                self.open_home_screen()
                J = "SELECT * FROM USER WHERE Email_ID = %s"
                I = (self.emaili.get(),)
                mc.execute(J, I)
                re = mc.fetchone()
                buddha=I
            else:
                self.warning_label.configure(text="U already have an acc by this Email Id")

    def close_window(self):
        self.destroy()
        self.parent.deiconify()

def frame_crop_Home(i,x, y, w, h):
    img = i.crop((x, y, x + w, y + h))  # .filter(ImageFilter.GaussianBlur(radius=3))
    return ctk.CTkImage(dark_image=img, size=(w, h))

class Home(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        window_width = 800
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        im=ctk.CTkImage(dark_image=Image.open("Holy Grail/12.jpg"), size=(800, 500))
        img=Image.open("Holy Grail/12.jpg").resize((800, 500))

        self.bg=ctk.CTkLabel(self,image=im,text="")
        self.bg.place(x=0,y=0)

        self.head=ctk.CTkLabel(self,text="TSUKI LINE 💫",image=frame_crop_Home(img,240,20,350,55),text_color="#FFC11D",font=("Algerian", 50, "bold", "underline"))
        self.head.place(x=240,y=20)

        #self.book_a_train=ctk.CTkLabel(self,text="Book A Train",font=("Berlin Sans FB", 30),image=frame_crop_Home(img,30,120,200,40),anchor="w",text_color="#C21313")
        self.book_a_train = ctk.CTkButton(self,text="Express Train Ticket",font=("Berlin Sans FB Demi", 30),fg_color="#317CBF",border_color="black",text_color="black",border_width=5,width=280,hover_color="#F1FF49",command=self.book_express)
        self.book_a_train.place(x=30,y=120)

        self.local_train = ctk.CTkButton(self,text="Local Trains Ticket",font=("Berlin Sans FB Demi", 30),fg_color="#317CBF",border_color="black",text_color="black",border_width=5,width=280,hover_color="#F1FF49",command=self.book_local)
        self.local_train.place(x=30, y=180)

        self.bookings = ctk.CTkButton(self, text="Your Bookings", font=("Berlin Sans FB Demi", 30), fg_color="#317CBF",border_color="black", text_color="black", border_width=5, width=280,hover_color="#F1FF49", command=self.check_bookings)
        self.bookings.place(x=30, y=240)

        self.cancel_train = ctk.CTkButton(self, text="Cancel Reservation", font=("Berlin Sans FB Demi", 28),fg_color="#317CBF", border_color="black", text_color="black", border_width=5,width=280, hover_color="#F1FF49", height=50, command=self.cancel_booking)
        self.cancel_train.place(x=30, y=300)

        self.re = ctk.CTkButton(self, text="<", height=20, width=20, command=self.close_window)
        self.re.place(x=5, y=5)

        self.pb = ctk.CTkButton(self, text="", width=20, height=20, image=fim, command=self.playfuc)
        self.pb.place(x=30, y=5)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        root = self.parent
        while root.master is not None:
            root = root.master
        root.destroy()

    def playfuc(self):
        player_ctrl(condition)
        self.pb.configure(image=fim)

    def book_express(self):
        self.withdraw()
        self.Book_Express_window = Book_Express(self)

    def book_local(self):
        self.withdraw()
        self.Book_local_window = Local_Train(self)

    def check_bookings(self):
        self.withdraw()
        self.check_bookings_window = bookings(self)

    def cancel_booking(self):
        self.withdraw()
        self.cancel_booking_window = Cancel(self)

    def close_window(self):
        self.destroy()
        self.parent.deiconify()

def frame_crop_book(i,x, y, w, h):
    img = i.crop((x+450, y+50, x+450+w,y+50+ h)).filter(ImageFilter.GaussianBlur(radius=5))
    return ctk.CTkImage(dark_image=img,size=(w,h))

class Book_Express(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        from_station_list=[]
        to_station_list = []

        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor()
        mc.execute("SELECT * FROM TRAIN_SCHEDULE")
        for i in mc:
            if i[2] not in from_station_list:
                from_station_list.append(i[2])
            if i[3] not in to_station_list:
                to_station_list.append(i[3])
        sorted(from_station_list)

        window_width = 800
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        img = ctk.CTkImage(dark_image=Image.open("Holy Grail/10.jpg"), size=(800, 500))
        im = Image.open("Holy Grail/10.jpg").resize((800, 500))

        self.logo = ctk.CTkLabel(self, image=img, text="")
        self.logo.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = ctk.CTkFrame(self, width=300, border_color="black", border_width=10, height=400)
        self.frame.place(x=450, y=50)

        self.bg= ctk.CTkLabel(self.frame,image=ctk.CTkImage(dark_image=im.crop((450, 50, 750,455)).filter(ImageFilter.GaussianBlur(radius=5)),size=(300,400)),text="")#.filter(ImageFilter.GaussianBlur(radius=3))
        self.bg.place(x=8, y=7,relwidth=0.949, relheight=0.963)

        self.find= ctk.CTkLabel(self.frame,image=frame_crop_book(im,50,20,200,40),text="Find Your Train",font=("Brush Script MT", 30, "bold", "underline"), anchor="w",text_color="blue")
        self.find.place(x=50,y=20)

        self.From= ctk.CTkLabel(self.frame,image=frame_crop_book(im,10,70,100,40),text="From",font=("Bauhaus 93",30),text_color="#FFE405")
        self.From.place(x=10,y=70)

        self.fromstation = ctk.CTkComboBox(self.frame,values=sorted(from_station_list),width=200)
        self.fromstation.place(x=25,y=110)
        self.fromstation.set("select Station")

        self.To = ctk.CTkLabel(self.frame, image=frame_crop_book(im, 10, 140, 100, 40), text="To    ",
                                 font=("Bauhaus 93", 30), text_color="#FFE405")
        self.To.place(x=10, y=140)

        self.tostation = ctk.CTkComboBox(self.frame, values=sorted(to_station_list), width=200)
        self.tostation.place(x=25, y=180)
        self.tostation.set("select Station")

        self.Date = ctk.CTkLabel(self.frame, image=frame_crop_book(im, 10, 210, 100, 40), text="Date",font=("Bauhaus 93", 30), text_color="#FFE405")
        self.Date.place(x=10, y=210)

        self.Day = ctk.CTkComboBox(self.frame, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'], width=75)
        self.Day.place(x=25, y=250)
        self.Day.set("Day")

        self.Month = ctk.CTkComboBox(self.frame, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], width=80)
        self.Month.place(x=105, y=250)
        self.Month.set("Month")

        self.Year = ctk.CTkComboBox(self.frame, values=["2025", "2026"], width=100)
        self.Year.place(x=190, y=250)
        self.Year.set("Year")

        self.find=ctk.CTkButton(self.frame,text="Find",border_color="black", fg_color="blue",font=("Bauhaus 93", 30),text_color="#39FF38",command=self.faku_baka)
        self.find.place(x=80,y=310)

        self.re = ctk.CTkButton(self, text="<", height=20, width=20, command=self.close_window)
        self.re.place(x=5, y=5)

        self.pb = ctk.CTkButton(self, text="", width=20, height=20, image=fim, command=self.playfuc)
        self.pb.place(x=30, y=5)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        root = self.parent
        while root.master is not None:
            root = root.master
        root.destroy()

    def playfuc(self):
        player_ctrl(condition)
        self.pb.configure(image=fim)

    def close_window(self):
        self.destroy()
        self.parent.deiconify()

    def faku_baka(self):
        global hitler
        global tamim
        hitler=[int(self.Year.get()),int(self.Month.get()),int(self.Day.get())]
        tamim=[self.fromstation.get(),self.tostation.get()]
        self.withdraw()
        self.Select_Train_window = Select_Train(self)

def frame_crop_select_train(i,x, y, w, h):
    img = i.crop((x+470, y+20, x+470+w,y+20+ h)).filter(ImageFilter.GaussianBlur(radius=3))
    return ctk.CTkImage(dark_image=img,size=(w,h))

raiden=False
class Select_Train(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        window_width = 800
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        im = ctk.CTkImage(dark_image=Image.open("Holy Grail/2.jpg"), size=(800, 500))
        self.imb = Image.open("Holy Grail/2.jpg").resize((800, 500))

        self.logo = ctk.CTkLabel(self, image=im, text="")
        self.logo.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = ctk.CTkFrame(self, width=300, border_color="black", border_width=10, height=450)
        self.frame.place(x=470, y=20)

        self.bg = ctk.CTkLabel(self.frame, image=ctk.CTkImage(
            dark_image=self.imb.crop((470, 20, 770, 470)).filter(ImageFilter.GaussianBlur(radius=3)), size=(300, 450)),
                               text="")
        self.bg.place(x=7, y=7, relwidth=0.949, relheight=0.963)

        self.l = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_select_train(self.imb, 45, 20, 215, 40),
                              text="Select Train", font=("Algerian", 30, "bold", "underline"), anchor="w",
                              text_color="#00FFFF")
        self.l.place(x=45, y=20)

        self.cal = Calendar(self, selectmode="day", date_pattern="dd-mm-yyyy",year=hitler[0],month=hitler[1],day=hitler[2])
        self.cal.place(x=15,y=40)
        self.cal.bind("<<CalendarSelected>>", self.recalculate)

        self.age = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_select_train(self.imb, 20, 60, 250, 30),
                                text="Trains available on the selected day", font=("Bahnschrift Condensed", 20), anchor="w", text_color="#FFC11D")
        self.age.place(x=20, y=60)

        date_obj = datetime.date(hitler[0], hitler[1], hitler[2])
        day_name = date_obj.strftime("%A")
        day_name=day_name[0:3].upper()

        l=[]
        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor()
        J = f"SELECT * FROM TRAIN_SCHEDULE WHERE `FROM` = %s AND `TO`=%s AND {day_name} = 1"
        I = (tamim[0], tamim[1])
        mc.execute(J, I)
        l = []
        for i in mc:
            l.append(i[1])

        self.trainonday = ctk.CTkComboBox(self.frame, values=l, width=200,command=self.days)
        self.trainonday.place(x=25, y=90)

        self.age = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_select_train(self.imb, 20, 120, 100, 30),
                                text="All trains     ", font=("Bahnschrift Condensed", 20),
                                anchor="w", text_color="#FFC11D")
        self.age.place(x=20, y=120)

        li=[]
        db = mysql.connector.connect(host="localhost", user="root", password="Waifus24/7", database="TSUKI_LINE")
        mc = db.cursor()
        J = "SELECT * FROM TRAIN_SCHEDULE WHERE `FROM` = %s AND `TO`=%s"
        I = (tamim[0], tamim[1])
        mc.execute(J, I)
        for i in mc:
            li.append(i[1])

        self.trainall = ctk.CTkComboBox(self.frame, values=li, width=200, command=self.days)
        self.trainall.place(x=25, y=150)
        self.trainall.set("All trains")

        self.age = ctk.CTkLabel(self.frame, width=100, height=30, image=frame_crop_select_train(self.imb, 20, 260, 100, 30),
                                text="Final choice    ", font=("Bahnschrift Condensed", 20),
                                anchor="w", text_color="#FFC11D")
        self.age.place(x=20, y=260)

        self.final = ctk.CTkComboBox(self.frame, values=l, width=200, command=self.COACH)
        self.final.place(x=25, y=290)
        if l == []:
            self.trainonday.set("No trains on the day")
            self.final.set("No trains on the day")
        else:
            self.trainonday.set("Select Train")
            self.final.set("Select Train")

        self.age = ctk.CTkLabel(self.frame, width=100, height=30,image=frame_crop_select_train(self.imb, 20, 320, 110, 30),
                                text="Select Coach     ", font=("Bahnschrift Condensed", 20),
                                anchor="w", text_color="blue")
        self.age.place(x=20, y=320)

        self.coach = ctk.CTkComboBox(self.frame, values=[], width=100, command=self.days)
        self.coach.place(x=20, y=350)
        self.coach.set("select train first")

        self.age = ctk.CTkLabel(self.frame, width=100, height=30,
                                image=frame_crop_select_train(self.imb, 20, 320, 110, 30),
                                text="Select Coach     ", font=("Bahnschrift Condensed", 20),
                                anchor="w", text_color="blue")
        self.age.place(x=20, y=320)

        self.coach = ctk.CTkComboBox(self.frame, values=[], width=130)
        self.coach.place(x=20, y=350)
        self.coach.set("select train first")

        self.finalyyyyy=ctk.CTkButton(self.frame, text="Book", border_color="black", fg_color="blue", width=120,command=self.finally_bookingT_T)
        self.finalyyyyy.place(x=90, y=400)

        self.re = ctk.CTkButton(self, text="<", height=20, width=20, command=self.close_window)
        self.re.place(x=5, y=5)

        self.pb = ctk.CTkButton(self, text="", width=20, height=20, image=fim, command=self.playfuc)
        self.pb.place(x=30, y=5)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        root = self.parent
        while root.master is not None:
            root = root.master
        root.destroy()

    def close_window(self):
        self.destroy()
        self.parent.deiconify()

    def playfuc(self):
        player_ctrl(condition)
        self.pb.configure(image=fim)

    def COACH(self,a):
        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor()
        mc.execute("SHOW COLUMNS FROM COST;")
        l = mc.fetchone()
        li=[]
        lis=[]
        for i in mc:
            lis.append(i[0])
        J = "SELECT T.TRAIN_NAME,C.* FROM TRAIN_SCHEDULE T JOIN COST C ON T.TRAIN_NO=C.TRAIN_NO WHERE T.TRAIN_NAME=%s"
        I = (a,)
        mc.execute(J, I)
        l=mc.fetchone()
        for i in range(2,len(l)-1):
            if None != l[i]:
                li.append(lis[i-2] + "   ₹ " + str(l[i]))
        self.coach.configure(values=li)
        self.coach.set("select")

    def days(self,choice):
        days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for j, day in enumerate(days):
            header = ctk.CTkLabel(self.frame, text=day, font=("Arial", 14, "bold"),width=20)
            header.place(x=20+40*j,y=190)

        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor()
        J = "SELECT * FROM TRAIN_SCHEDULE WHERE TRAIN_NAME=%s"
        I = (choice,)
        mc.execute(J, I)
        l=mc.fetchone()
        for i in range(6,13):
            if l[i]==1:
                tick = ctk.CTkLabel(self.frame, text="✓", font=("Arial", 14, "bold"), width=20)
            else:
                tick = ctk.CTkLabel(self.frame, text="-", font=("Arial", 14, "bold"), width=20)
            tick.place(x=20 + 40 * (i-6), y=230)

    def recalculate(self,event=None):
        day,mo,yr=self.cal.get_date().split("-")
        date_obj = datetime.date(int(yr), int(mo), int(day))
        day_name = date_obj.strftime("%A")
        day_name = day_name[0:3].upper()
        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor()
        J = f"SELECT * FROM TRAIN_SCHEDULE WHERE `FROM` = %s AND `TO`=%s AND {day_name} = 1"
        I = (tamim[0], tamim[1])
        mc.execute(J, I)
        l = []
        for i in mc:
            l.append(i[1])
        self.trainonday.configure(values=l)
        self.final.configure(values=l)
        if not l:
            self.trainonday.set("No trains on the day")
            self.final.set("No trains on the day")
        else:
            self.trainonday.set("Select Train")
            self.final.set("Select Train")

    def finally_bookingT_T(self):
        global seat_no
        global hitler
        global raiden
        date = self.cal.get_date()
        hitler=self.cal.get_date().split("-")
        hitler=hitler[2]+"-"+hitler[1]+"-"+hitler[0]
        if self.coach.get() != "":
            db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
            mc = db.cursor(buffered=True)
            J = f"CREATE TABLE IF NOT EXISTS `{self.final.get().replace(" ", "_")}{date}`(`NO` INT,`SL` INT,`1A` INT,`2A` INT,`3A` INT,`3E` INT,`CC` INT);"
            mc.execute(J)
            J = f'SELECT * FROM `{self.final.get().replace(" ", "_")}{date}`;'
            mc.execute(J)
            if mc.fetchone() is None:
                for i in range(1, 11):
                    J = f"Insert into `{self.final.get().replace(" ", "_")}{date}` values(%s,NULL,NULL,NULL,NULL,NULL,NULL);"
                    I = (i,)
                    mc.execute(J, I)
            db.commit()
            J = f"SELECT * FROM `{self.final.get().replace(" ", "_")}{date}` WHERE `{self.coach.get().split()[0]}` IS NULL"
            mc.execute(J)
            r = mc.fetchone()
            if r is None:
                raiden=True
            seat_no = [r[0], self.final.get().replace(" ", "_") + date, self.coach.get().split()[0],date,self.final.get()]
            self.withdraw()
            self.conformation_window =conformation(self)

    def cont(self):
        self.destroy()
        self.parent.close_window()

class conformation(ctk.CTkToplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent

        window_width = 220
        window_height = 150
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.img = ctk.CTkImage(dark_image=Image.open("Holy Grail/sky.jpg"), size=(220, 150))
        self.logo = ctk.CTkLabel(self, image=self.img, text="")
        self.logo.place(x=0, y=0)

        self.a = ctk.CTkLabel(self, text="Are you sure you want to book it?")
        self.a.place(x=15, y=10)

        if raiden:
            db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
            mc = db.cursor(buffered=True)
            J = f"SELECT * FROM EXPRESS_BOOKING WHERE TRAIN={seat_no[4]} AND `DATE`={hitler} AND STATUS='waiting';"
            mc.execute(J)
            r=mc.fetchall()
            self.a.configure(text=f"Do u want to continue with waiting list no. {len(r)+1}")

        self.yes_btn = ctk.CTkButton(self, text="Yes", command=self.confirm_booking)
        self.yes_btn.place(x=40, y=50)

        self.no_btn = ctk.CTkButton(self, text="No", command=self.close_window)
        self.no_btn.place(x=40, y=100)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        root = self.parent
        while root.master is not None:
            root = root.master
        root.destroy()

    def pnrgen(self):
        global pn
        pnr = random.randint(1, 9)
        for i in range(9):
            pnr = pnr * 10 + random.randint(0, 9)

        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor()

        J = "SELECT * FROM EXPRESS_BOOKING WHERE PNR = %s"
        mc.execute(J, (pnr,))
        r = mc.fetchone()

        if r is None:
            pn=pnr
            return pnr
        else:
            return self.pnrgen()

    def confirm_booking(self):
        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor()
        J = "INSERT INTO express_booking (USER_ID, TRAIN, `DATE`, BOOKING_DATE, PNR, STATUS,SEAT)VALUES (%s, %s, %s, %s, %s, %s,%s)"
        if raiden:
            I = (buddha[0], seat_no[4], hitler, date.today(), self.pnrgen(), "waiting", "-")
        else:
            I = (buddha[0], seat_no[4], hitler, date.today(), self.pnrgen(), "confirmed", seat_no[2] + str(seat_no[0]))
            Ji = f"UPDATE `{seat_no[1]}` SET `{seat_no[2]}`= %s WHERE `NO` = {seat_no[0]}"
            Ii = (buddha[0],)
            mc.execute(Ji, Ii)
        mc.execute(J, I)
        db.commit()
        self.withdraw()
        self.map_window =MapsScreenshot(self)

    def close_window(self):
        self.destroy()
        self.parent.deiconify()

    def cont(self):
        self.destroy()
        self.parent.cont()

class MapsScreenshot(ctk.CTkToplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent

        window_width = 1000
        window_height = 550
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.title("Google Maps Train Route")

        im = ctk.CTkImage(dark_image=Image.open("Holy Grail/8.jpg"), size=(400,550))

        self.logo = ctk.CTkLabel(self, image=im, text="")
        self.logo.place(x=0, y=0)

        title = ctk.CTkLabel(self, text=f"Route: {tamim[0]} → {tamim[1]}",font=("Arial", 18, "bold"))
        title.place(x=500,y=30)

        self.status_label = ctk.CTkLabel(self, text="Click button to fetch route",font=("Arial", 12))
        self.status_label.place(x=500,y=60)

        self.image_label = ctk.CTkLabel(self, text="",width=600)
        self.image_label.place(x=400,y=100)

        self.conti = ctk.CTkButton(self, text="Continue",command=self.next)
        self.conti.place(x=630, y=510)

        self.fetch_route()

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        root = self.parent
        while root.master is not None:
            root = root.master
        root.destroy()

    def fetch_route(self):
        self.status_label.configure(text="Opening browser and fetching route...")
        self.update()

        driver = None
        try:
            # Setup Chrome driver in headless mode
            options = webdriver.ChromeOptions()
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)

            driver = webdriver.Chrome(options=options)

            # Build direct Google Maps URL with directions
            self.status_label.configure(text="Loading route...")
            self.update()

            start_encoded = urllib.parse.quote(tamim[0])
            end_encoded = urllib.parse.quote(tamim[1])

            # Direct URL for transit directions
            maps_url = f"https://www.google.com/maps/dir/{start_encoded}/{end_encoded}/data=!3m1!4b1!4m2!4m1!3e3"
            driver.get(maps_url)

            # Wait for page to load properly
            self.status_label.configure(text="Waiting for route to load...")
            self.update()
            time.sleep(15)  # Increased wait time for route to fully render

            # Take screenshot
            self.status_label.configure(text="Taking screenshot...")
            self.update()

            screenshot = driver.get_screenshot_as_png()

            # Display screenshot in CTk
            img = Image.open(BytesIO(screenshot))

            # Crop to remove sidebar (remove left ~490 pixels)
            width, height = img.size
            img = img.crop((490, 0, width, height))

            # Resize image to fit window
            img.thumbnail((750, 400), Image.Resampling.LANCZOS)

            # Convert to CTkImage
            ctk_image = ctk.CTkImage(light_image=img, dark_image=img,size=(img.width, img.height))

            self.image_label.configure(image=ctk_image, text="")
            self.status_label.configure(text="Route fetched successfully!")

        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}")
            print(f"Full error: {e}")

        finally:
            if driver:
                driver.quit()

    def next(self):
        self.withdraw()
        self.express_ticket_gen_window = Express_ticket_gen(self)

    def cont(self):
        self.destroy()
        self.parent.cont()

def ti_email(x,subject,body,img):

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        img.save(tmp.name, "PNG")
        tmp_path = tmp.name

    # Create the email message
    msg = EmailMessage()
    msg['From'] = "tsukiline1@gmail.com"
    msg['To'] = x
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        with open(tmp_path, "rb") as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype="image", subtype="png", filename="ticket.png")
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login("tsukiline1@gmail.com", email_password)
            smtp.send_message(msg)
        print("✅ Custom email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)

class Express_ticket_gen(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        window_width = 1000
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        im = ctk.CTkImage(dark_image=Image.open("Holy Grail/alice.webp"), size=(350, 600))
        img = Image.open("Holy Grail/final ticket.png").convert("RGBA")
        img = img.resize((650, 400))
        draw = ImageDraw.Draw(img)

        draw.text((250,10), "TSUKI LINE", fill="#FFC11D", font=ImageFont.truetype("ALGER.TTF", 25))
        draw.text((150, 50), "Ticket", fill="#00FFFF", font=ImageFont.truetype("ALGER.TTF", 20))
        draw.text((155, 90), ("PNR    :" + str(pn)), fill="white", font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((155, 120), "Name :"+buddha[3], fill="white", font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((155, 150), "From   :"+tamim[0], fill="white", font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((420, 150), "Age:"+str(buddha[4]), fill="white", font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((155, 180), "To        :"+tamim[1], fill="white", font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((420, 180), "Gen:"+buddha[5], fill="white", font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((155, 210), "Date   :"+hitler, fill="white", font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((155, 240), "Train  :"+seat_no[4], fill="white", font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        if raiden:
            draw.text((155, 270), "Seat No.   :" +"-", fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        else:
            draw.text((155, 270), "Seat No.   :" + seat_no[2] + str(seat_no[0]), fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((200, 300), "Certified by the NAZI government", fill="red", font=ImageFont.truetype("ALGER.TTF", 15))

        ti_email(buddha[1], "Ticket", "Your booking has been conformed 👍", img)

        img = ctk.CTkImage(dark_image=img, size=(650, 400))

        self.logo = ctk.CTkLabel(self, image=im, text="")
        self.logo.place(x=0, y=0)

        self.l = ctk.CTkLabel(self, width=100, height=30, text="Your Ticket",
                              font=("Algerian", 40, "bold", "underline"), anchor="w", text_color="#00FFFF")
        self.l.place(x=550, y=20)

        self.logo = ctk.CTkLabel(self, image=img, text="")
        self.logo.place(x=350, y=100)

        self.bo = ctk.CTkButton(self, text="Continue", width=200,height=50,font=("Berlin Sans FB Demi", 30),fg_color="#317CBF",border_color="black",text_color="black",border_width=5,hover_color="#F1FF49",command=self.cont)
        self.bo.place(x=570, y=530)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        root = self.parent
        while root.master is not None:
            root = root.master
        root.destroy()

    def cont(self):
        self.destroy()
        self.parent.cont()


def frame_crop_local(i, x, y, w, h):
    img = i.crop((x + 450, y + 50, x + 450 + w, y + 50 + h)).filter(ImageFilter.GaussianBlur(radius=5))
    return ctk.CTkImage(dark_image=img, size=(w, h))

class Local_Train(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        window_width = 800
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        img = ctk.CTkImage(dark_image=Image.open("Holy Grail/13.jpg"), size=(800, 500))
        im = Image.open("Holy Grail/13.jpg").resize((800, 500))

        self.logo = ctk.CTkLabel(self, image=img, text="")
        self.logo.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = ctk.CTkFrame(self, width=300, border_color="black", border_width=10, height=400)
        self.frame.place(x=450, y=50)

        self.bg = ctk.CTkLabel(self.frame, image=ctk.CTkImage(dark_image=im.crop((450, 50, 750, 455)).filter(ImageFilter.GaussianBlur(radius=5)), size=(300, 400)),text="")  # .filter(ImageFilter.GaussianBlur(radius=3))
        self.bg.place(x=8, y=7, relwidth=0.949, relheight=0.963)

        self.find = ctk.CTkLabel(self.frame, image=frame_crop_local(im, 50, 20, 200, 40), text="Book Train",
                                 font=("Brush Script MT", 30, "bold", "underline"), anchor="w", text_color="white")
        self.find.place(x=50, y=20)

        self.From = ctk.CTkLabel(self.frame, image=frame_crop_local(im, 10, 70, 100, 40), text="From",
                                 font=("Bauhaus 93", 30), text_color="#FFE405")
        self.From.place(x=10, y=70)

        self.fromstation = ctk.CTkComboBox(self.frame, values=l, width=200)
        self.fromstation.place(x=25, y=110)
        self.fromstation.set("select Station")

        self.To = ctk.CTkLabel(self.frame, image=frame_crop_local(im, 10, 170, 100, 40), text="To    ",
                               font=("Bauhaus 93", 30), text_color="#FFE405")
        self.To.place(x=10, y=170)

        self.tostation = ctk.CTkComboBox(self.frame, values=l, width=200)
        self.tostation.place(x=25, y=210)
        self.tostation.set("select Station")

        self.Book = ctk.CTkButton(self.frame, text="Book", border_color="black", fg_color="blue",
                                  font=("Bauhaus 93", 30), text_color="#39FF38",command=self.booking)
        self.Book.place(x=80, y=310)

        self.aluu = ctk.CTkLabel(self, text="", text_color="red", font=("Bauhaus 93", 30))
        self.aluu.place(x=15, y=330)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.re = ctk.CTkButton(self, text="<", height=20, width=20, command=self.close_window)
        self.re.place(x=5, y=5)

        self.pb = ctk.CTkButton(self, text="", width=20, height=20, image=fim, command=self.playfuc)
        self.pb.place(x=30, y=5)

    def on_close(self):
        self.destroy()
        root = self.parent
        while root.master is not None:
            root = root.master
        root.destroy()

    def close_window(self):
        self.destroy()
        self.parent.deiconify()

    def playfuc(self):
        player_ctrl(condition)
        self.pb.configure(image=fim)

    def pnrgen(self):
        global pn
        pnr = random.randint(1, 9)
        for i in range(9):
            pnr = pnr * 10 + random.randint(0, 9)

        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor()

        J = "SELECT * FROM LOCAL_BOOK WHERE PNR = %s"
        mc.execute(J, (pnr,))
        r = mc.fetchone()

        if r is None:
            pn=pnr
            return pnr
        else:
            return self.pnrgen()

    def star_mail(self):
        email(buddha[1], "🎉 Booking Confirmed", "Your ticket has been booked!")
        print("alu")

    def booking(self):
        c = 1
        global buddha
        global tamim

        if self.fromstation.get() not in l or self.tostation.get() not in l:
            self.aluu.configure(text="Incorrect Station")
            c = 0

        if c == 1:
            db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
            mc = db.cursor()
            J = "INSERT INTO LOCAL_BOOK(FROMS, TOS, USER_ID, PNR) VALUES (%s, %s, %s, %s)"
            I = (self.fromstation.get(), self.tostation.get(), buddha[0], self.pnrgen())
            mc.execute(J, I)
            db.commit()
            tamim=[self.fromstation.get(), self.tostation.get()]
            self.withdraw()
            self.tickit_gen_window = tickit_gen(self)

class tickit_gen(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        window_width = 1000
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        im = ctk.CTkImage(dark_image=Image.open("Holy Grail/1.jpg"), size=(350, 600))
        img = Image.open("Holy Grail/final ticket.png").convert("RGBA")
        img = img.resize((650, 400))
        draw = ImageDraw.Draw(img)

        self.logo = ctk.CTkLabel(self, image=im, text="")
        self.logo.place(x=0, y=0)

        self.l = ctk.CTkLabel(self, width=100, height=30, text="Your Ticket",
                              font=("Algerian", 40, "bold", "underline"), anchor="w", text_color="#00FFFF")
        self.l.place(x=550, y=20)

        draw.text((250, 10), "TSUKI LINE", fill="#FFC11D", font=ImageFont.truetype("ALGER.TTF", 25))
        draw.text((150, 50), "Ticket", fill="#00FFFF", font=ImageFont.truetype("ALGER.TTF", 20))
        draw.text((155, 90), ("PNR    :" + str(pn)), fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((155, 120), ("Name :" + buddha[3]), fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((155, 150), ("From   :" + tamim[0]), fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((155, 180), ("To        :" + tamim[1]), fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((155, 210), ("Date   :" + str(datetime.date.today())), fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
        draw.text((200, 270), "Certified by the NAZI government", fill="red", font=ImageFont.truetype("ALGER.TTF", 15))

        ti_email(buddha[1], "Ticket", "Your booking has been conformed 👍", img)

        img = ctk.CTkImage(dark_image=img, size=(650, 400))

        self.logo = ctk.CTkLabel(self, image=img, text="")
        self.logo.place(x=350, y=100)

        self.bo = ctk.CTkButton(self, text="Continue", width=200,height=50,font=("Berlin Sans FB Demi", 30),fg_color="#317CBF",border_color="black",text_color="black",border_width=5,hover_color="#F1FF49",command=self.retur)
        self.bo.place(x=570, y=530)

        self.pb = ctk.CTkButton(self, text="", width=20, height=20, image=fim, command=self.playfuc)
        self.pb.place(x=30, y=5)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        root = self.parent
        while root.master is not None:
            root = root.master
        root.destroy()

    def playfuc(self):
        player_ctrl(condition)
        self.pb.configure(image=fim)

    def retur(self):
        self.destroy()
        self.parent.close_window()

class bookings(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        window_width = 800
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        im = ctk.CTkImage(dark_image=Image.open("Holy Grail/4.jpg"), size=(350, 500))
        img = ctk.CTkImage(dark_image=Image.open("Holy Grail/sky.jpg"), size=(450, 500))

        self.logo = ctk.CTkLabel(self, image=im, text="")
        self.logo.place(x=0, y=0, )
        self.logo = ctk.CTkLabel(self, image=img, text="")
        self.logo.place(x=350, y=0, )

        self.si = ctk.CTkButton(self, text="Local", fg_color="#317CBF", border_color="black", text_color="black",
                                border_width=5, width=120, hover_color="#F1FF49", command=self.local)
        self.si.place(x=40, y=450)
        self.si = ctk.CTkButton(self, text="Express", border_color="black", fg_color="#317CBF", width=120,
                                text_color="black", border_width=5, hover_color="#F1FF49", command=self.express)
        self.si.place(x=170, y=450)

        self.frame = ctk.CTkScrollableFrame(self, label_text="Your Bookings", width=420)
        self.frame.place(x=360, y=0)

        self.logo = ctk.CTkLabel(self.frame, image=img, text="")
        self.logo.place(x=0, y=0, )

        self.re = ctk.CTkButton(self, text="<", height=20, width=20, command=self.close_window)
        self.re.place(x=5, y=5)

        self.pb = ctk.CTkButton(self, text="", width=20, height=20, image=fim, command=self.playfuc)
        self.pb.place(x=30, y=5)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.local()

    def local(self):
        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor()
        J = "SELECT * FROM LOCAL_BOOK WHERE USER_ID = %s"
        I = (buddha[0],)
        mc.execute(J, I)
        re = mc.fetchall()
        self.frame.configure(label_text="Local Train Bookings")
        self.arrange(re)
        yc = 0
        for i in re:
            self.b = ctk.CTkButton(self.frame, text=str(i[0]) + "   " + i[1] + "-" + i[2] + "    " + str(i[4]),
                                   width=410, height=50)
            self.b.pack(pady=5, fill="x")
            yc += 60

    def express(self):
        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor()
        J = "SELECT * FROM EXPRESS_BOOKING WHERE USER_ID = %s and STATUS NOT IN ('canceled')"
        I = (buddha[0],)
        mc.execute(J, I)
        re = mc.fetchall()
        self.frame.configure(label_text="Express Train Bookings")
        self.arrange(re)
        yc = 0
        for i in re:
            self.b = ctk.CTkButton(self.frame, text=str(i[2]) + "   " + str(i[3]) + "   " + i[6] + "    " + (
                        i[7] + "   " + str(i[5])), width=410, height=50)
            self.b.pack(pady=5, fill="x")
            yc += 60

    def arrange(self, re):
        for widget in self.frame.winfo_children():
            widget.destroy()

        if 60 * len(re) < 430:
            h = 60 * len(re)
        else:
            h = 430
        self.frame.configure(height=h)

    def on_close(self):
        self.destroy()
        root = self.parent
        while root.master is not None:
            root = root.master
        root.destroy()

    def close_window(self):
        self.destroy()
        self.parent.deiconify()

    def playfuc(self):
        player_ctrl(condition)
        self.pb.configure(image=fim)

nahida=[]
typee="l"
class Cancel(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        window_width = 800
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        im = ctk.CTkImage(dark_image=Image.open("Holy Grail/15.jpg"), size=(350,500))
        img = ctk.CTkImage(dark_image=Image.open("Holy Grail/sky.jpg"), size=(450, 500))

        self.logo = ctk.CTkLabel(self, image=im, text="")
        self.logo.place(x=0, y=0,)
        self.logo = ctk.CTkLabel(self, image=img, text="")
        self.logo.place(x=350, y=0, )

        self.si = ctk.CTkButton(self, text="Local", fg_color="#317CBF", border_color="black", text_color="black",border_width=5, width=120, hover_color="#F1FF49", command=self.local)
        self.si.place(x=40, y=450)
        self.si = ctk.CTkButton(self, text="Express", border_color="black", fg_color="#317CBF", width=120,text_color="black", border_width=5, hover_color="#F1FF49", command=self.express)
        self.si.place(x=170, y=450)

        self.frame = ctk.CTkScrollableFrame(self, label_text="", width=420,height=100)
        self.frame.place(x=360, y=0)
        self.refresh_bookings()

        self.re = ctk.CTkButton(self, text="<", height=20, width=20, command=self.close_window)
        self.re.place(x=5, y=5)

        self.pb = ctk.CTkButton(self, text="", width=20, height=20, image=fim, command=self.playfuc)
        self.pb.place(x=30, y=5)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        root = self.parent
        while root.master is not None:
            root = root.master
        root.destroy()

    def playfuc(self):
        player_ctrl(condition)
        self.pb.configure(image=fim)

    def refresh_bookings(self):
        if typee == "l":
            self.local()
        else:
            self.express()

    def local(self):
        global typee
        typee = "l"
        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor()
        J = "SELECT * FROM LOCAL_BOOK WHERE USER_ID = %s"
        I = (buddha[0],)
        mc.execute(J, I)
        re = mc.fetchall()
        self.frame.configure(label_text="Local Train Bookings")
        self.arrange(re)
        yc = 0
        for i in re:
            self.b = ctk.CTkButton(self.frame, text=str(i[0]) + "   " + i[1] + "-" + i[2] + "    " + str(i[4]),
                                   width=410, height=50, command=lambda c=i: self.damn_fuck(c))
            self.b.pack(pady=5, fill="x")
            yc += 60

    def express(self):
        global typee
        typee = "e"
        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor()
        J = "SELECT * FROM EXPRESS_BOOKING WHERE USER_ID = %s and STATUS NOT IN ('canceled')"
        I = (buddha[0],)
        mc.execute(J, I)
        re = mc.fetchall()
        self.frame.configure(label_text="Express Train Bookings")
        self.arrange(re)
        yc = 0
        for i in re:
            self.b = ctk.CTkButton(self.frame, text=str(i[2]) + "   " + str(i[3]) + "   " + i[6] + "    " + (i[7] + "   " + str(i[5])), width=410, height=50, command=lambda c=i: self.damn_fuck(c))
            self.b.pack(pady=5, fill="x")
            yc += 60

    def arrange(self, re):
        for widget in self.frame.winfo_children():
            widget.destroy()

        if 60 * len(re) < 430:
            h = 60 * len(re)
        else:
            h = 430
        self.frame.configure(height=h)

    def damn_fuck(self,x):
        global nahida
        nahida=x
        self.withdraw()
        self.shit = cancellation(self)

    def close_window(self):
        self.destroy()
        self.parent.deiconify()

class cancellation(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent   # store reference to main window

        window_width = 220
        window_height = 150
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.img = ctk.CTkImage(dark_image=Image.open("Holy Grail/sky.jpg"), size=(220, 150))
        self.logo = ctk.CTkLabel(self, image=self.img, text="")
        self.logo.place(x=0, y=0)

        self.a = ctk.CTkLabel(self, text="Are you sure you want to cancel it?")
        self.a.place(x=15, y=10)

        self.yes_btn = ctk.CTkButton(self, text="Yes", command=self.confirm_cancel)
        self.yes_btn.place(x=40, y=50)

        self.no_btn = ctk.CTkButton(self, text="No", command=self.close_window)
        self.no_btn.place(x=40, y=100)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        root = self.parent
        while root.master is not None:
            root = root.master
        root.destroy()

    def confirm_cancel(self):
        db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="TSUKI_LINE")
        mc = db.cursor(buffered=True)
        if typee == "l":
            J = "DELETE FROM LOCAL_BOOK WHERE BOOKING_ID = %s"
            I = (nahida[0],)
            mc.execute(J, I)
        else:
            mc.execute("SELECT * FROM express_booking WHERE PNR=%s", (nahida[5],))
            r = mc.fetchone()
            mc.execute("UPDATE express_booking SET STATUS='canceled' WHERE PNR=%s", (nahida[5],))
            mc.execute("SELECT * FROM express_booking WHERE TRAIN=%s AND STATUS='waiting' AND `DATE`=%s",
                       (nahida[2], nahida[3]))
            r = mc.fetchone()
            d = str(nahida[3]).split("-")
            d = d[2] + "-" + d[1] + "-" + d[0]
            seat_table = nahida[2].replace(" ", "_") + d
            seat_col = nahida[7][0:2]  # first two chars (like SL, AC, etc.)
            seat_noo = nahida[7][2:]
            if r:
                mc.execute("UPDATE express_booking SET STATUS='confirmed', SEAT=%s WHERE PNR=%s", (nahida[7], r[5]))
                mc.execute(f"UPDATE `{seat_table}` SET `{seat_col}`=%s WHERE NO=%s", (r[2], seat_noo))
                mc.execute(f"select * from user where USER_ID =%s",(r[1],))
                b=mc.fetchone()
                mc.execute(f"select * from train_schedule where TRAIN =%s", (r[2],))
                c=mc.fetchone()
                img = Image.open("Holy Grail/final ticket.png").convert("RGBA")
                img = img.resize((650, 400))
                draw = ImageDraw.Draw(img)
                draw.text((250, 10), "TSUKI LINE", fill="#FFC11D", font=ImageFont.truetype("ALGER.TTF", 25))
                draw.text((150, 50), "Ticket", fill="#00FFFF", font=ImageFont.truetype("ALGER.TTF", 20))
                draw.text((155, 90), ("PNR    :" + str(r[5])), fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
                draw.text((155, 120), "Name :" + b[3], fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
                draw.text((155, 150), "From   :" + c[2], fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
                draw.text((420, 150), "Age:" + str(b[4]), fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
                draw.text((155, 180), "To        :" + c[3], fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
                draw.text((420, 180), "Gen:" + b[5], fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
                draw.text((155, 210), "Date   :" + str(r[3]), fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
                draw.text((155, 240), "Train  :" + r[2], fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
                draw.text((155, 270), "Seat No.   :" + seat_col + str(seat_noo), fill="white",font=ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF", 20))
                draw.text((200, 300), "Certified by the NAZI government", fill="red",font=ImageFont.truetype("ALGER.TTF", 15))

                ti_email(buddha[1], "Ticket", "Your booking has been conformed 👍", img)
            else:
                mc.execute(f"UPDATE `{seat_table}` SET `{seat_col}`=NULL WHERE NO=%s", (seat_noo,))

            email(buddha[1],"Cancellation","Your booking has been successfully canceled")

        db.commit()
        self.a.configure(text="booking canceled")
        self.a.place(x=50,y=10)
        self.yes_btn.place(x=0,y=200)
        self.no_btn.place(x=0,y=200)
        self.b = ctk.CTkButton(self, text="Continue", command=self.close_window)
        self.b.place(x=40, y=100)

    def close_window(self):
        self.destroy()
        self.parent.deiconify()
        self.parent.refresh_bookings()

def frame_crop_contri(im,x, y, w, h):
    img = im.crop((x+420, y+50, x+420+w,y+50+ h)).filter(ImageFilter.GaussianBlur(radius=3))
    return ctk.CTkImage(dark_image=img,size=(w,h))


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app=App()
app.mainloop()