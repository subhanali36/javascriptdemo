from tkinter import *
from PIL import Image,ImageTk

class SMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Medical Store Management System ")


        self.icon_title=PhotoImage(file="download.jpg")
        title=(Label(self.root,text="Medical Store Management System",image=self.icon_title,font=("times new roman",40,"bold"),bg="Green",fg="white")
               .place(x=0,y=10,relwidth=1,height=60))




root = Tk()
obj = SMS(root)
root.mainloop()
