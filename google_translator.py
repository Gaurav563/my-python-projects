from tkinter import *
from tkinter import ttk
from googletrans import Translator ,LANGUAGES
root = Tk()


def change(text='type',src='English',dest='Hindi'):

    text1 = text
    src1 =src
    dest1 =dest
    trans = Translator(service_urls=['translate.googleapis.com'])
    trans1= trans.translate(text,src=src1,dest=dest1)

    return trans1
def data():

    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0 ,END)
    textget = change(text=msg,src=s,dest=d)
    print(type(textget))
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget.text)
  

root.title('Translator')
root.geometry('500x800')
root.config(bg='grey')


lab_txt = Label(root,text = 'Translator',font =('Time New Roman',40,'bold'))
lab_txt.place(x=100,y=40,height=50,width=300)

frane = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text = 'Source Text',font =('Time New Roman',40,'bold'), fg='blue', bg='gray')
lab_txt.place(x=100,y=100,height=50,width=300)

sor_txt = Text(frane,font=('Time New Roman',20,'bold'),wrap=WORD)
sor_txt.place(x=10,y=160,height=200,width=480)

list_txt =list(LANGUAGES.values())

comb_sor = ttk.Combobox(frane,value=list_txt)
comb_sor.place(x=10,y=410,height=40,width=100)
comb_sor.set('english')


button_change = Button(frane,text = 'Translate',relief=RAISED,command=data)
button_change.place(x=140,y=410,height=40,width=100)

comb_dest= ttk.Combobox(frane,value=list_txt)
comb_dest.place(x=300,y=410,height=40,width=100)
comb_dest.set('english')

lab_txt = Label(root,text = 'Dest Text',font =('Time New Roman',40,'bold'), fg='blue', bg='gray')
lab_txt.place(x=100,y=360,height=50,width=300)

dest_txt= Text(frane,font=('Time New Roman',20,'bold'),wrap=WORD)
dest_txt.place(x=10,y=480,height=200,width=480)



root.mainloop()