# This Program Has Been Coded By @Q55 <----- At Github
# 2022/24/06
# If the url is long u might have to make the window bigger to show the full qrcode

import time
import qrcode
import pyqrcode
from PIL import ImageTk as itk
from tkinter import ttk
from tkinter import *


window = Tk()

def genrate():
    if len(Subject.get()) != 0:
        global qr, photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data=qr.xbm(scale=8))
        msgbox.place_forget()
    else:
        msgbox.place(x=160, y=375)
    try:
        showcode()
    except:
        pass


def showcode():
    imageLabel.config(image=photo)
    imageLabel.place(x=130, y=260)


Subject = StringVar()

PhotoFrame= PhotoImage(file='Frame1.png')
window.title('Creating QrCode')
window.geometry('500x500')
window.configure(bg='#34495e')
Label(window,image=PhotoFrame).pack()
#window.resizable(False, False)

LinkLabel = Entry(window, textvariable=Subject,  width='50', font = ('calibre',10,'normal'), bg='#2980b9')
LinkLabel.place(x=70,y=165)

sub_btn = Button(window, text='Convert', command=genrate, bg='#816797').place(x=220,y=220)

msgbox = Label(window, width=27, height=7, text="Please Don't Leave The Label Empty !")

imageLabel = Label(window)


window.mainloop()