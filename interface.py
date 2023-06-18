from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


def start1():
    root=Tk()
    root.title("Input image")
    global img
    def finish():
        root.destroy()

    root.geometry("800x600")
    root.filename=filedialog.askopenfilename(initialdir="Images",title="Select a Image")

    img=Image.open(root.filename)
    temp=img.resize((600,400),Image.Resampling.BILINEAR)
    myimage=ImageTk.PhotoImage(temp)
    label=Label(root,text="Input Hazy-Image",image=myimage).pack(pady=20)
    startbtn=Image.open("Interface/start.jpg")
    start=ImageTk.PhotoImage(startbtn)
    btn=Button(root,image=start,command=finish,border=False).pack(pady=20,side="bottom")
    root.mainloop()


def start2():
    root=Tk()
    root.title("Comparision between Input image and Output Image")
    root.attributes("-fullscreen",True)
    def finish():
        root.destroy()

    img1=img
    img11=img1.resize((700,600),Image.Resampling.BILINEAR)
    photo1=ImageTk.PhotoImage(img11)
    label1=Label(root,text="Hazy-Image",image=photo1).pack(side="left")

    img2=Image.open("Results/haze_free.jpg")
    img22=img2.resize((700,600),Image.Resampling.BILINEAR)
    photo2=ImageTk.PhotoImage(img22)
    label2=Label(root,text="Dehazed-Image",image=photo2).pack(side="right")

    closebtn=Image.open("Interface/close.jpg")
    close=ImageTk.PhotoImage(closebtn)
    btn=Button(root,image=close,command=finish,border=False).pack(pady=20,side="bottom")

    root.mainloop()

def start():
    root=Tk()
    root.title("Image Dehazing")
    root.geometry("700x550")
    def begin():
        root.destroy()
        start1()
    
    pic=Image.open("Interface/interface.jpg")
    pic=pic.resize((600,400),Image.Resampling.BILINEAR)
    button=Image.open("Interface/button.jpg")
    pic=ImageTk.PhotoImage(pic)
    button=ImageTk.PhotoImage(image=button)
    label=Label(root,text="Upload an Image",image=pic).pack(pady=10,side="top")
    #blabel=Label(root,image=button).pack(pady=10,side="bottom")
    btn=Button(root,image=button,command=begin,border=False).pack(pady=20,side="bottom")
    root.mainloop()

