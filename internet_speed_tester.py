from tkinter import *
from speedtest import Speedtest

def speedcheck():
    sp= Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+'Mbs'
    up = str(round(sp.upload()/(10**6),3))+'Mbs'
    lab_down.config(text= down)
    lab_up.config(text=up)



sp=Tk()
sp.title('Internet Speed Test')
sp.geometry('500x650')
sp.config(bg= "blue")



lab = Label(sp,text="Internet Speed test", font=("Time New Roman",20,'bold'),bg='orange',fg='white')
lab.place(x=55,y=40,height=50,width=380)
lab = Label(sp,text="Download Speed test", font=("Time New Roman",20,'bold'),bg='grey',fg='white')
lab.place(x=55,y=130,height=50,width=380)
lab_down= Label(sp,text=" 00", font=("Time New Roman",20,'bold'),bg='blue',fg='white')
lab_down.place(x=55,y=200,height=50,width=380)
lab = Label(sp,text="Upload Speed test", font=("Time New Roman",20,'bold'),bg='grey',fg='white')
lab.place(x=55,y=290,height=50,width=380)
lab_up = Label(sp,text="00", font=("Time New Roman",20,'bold'),bg='blue',fg='white')
lab_up.place(x=55,y=360,height=50,width=380)

button =Button(sp,text="CHECK SPEED",font=("Time New Roman",20,'bold'),relief=RAISED,bg="red",command=speedcheck)
button.place(x=55,y=460,height=50,width=380)

sp.mainloop()

