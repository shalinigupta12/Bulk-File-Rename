import os
from tkinter import *

def rename():
    
    folderpath = r''+path.get()
    counter = 1

    for filename in os.listdir(folderpath):
        os.rename(folderpath+'\\'+filename , folderpath+'\\'+word.get()+str(counter)+exe.get())
        counter = counter+1
       
    ent.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)

    
root = Tk()
root.title('RENAMER')
root.geometry('300x300')

path = StringVar()

Label(root, text  = 'PASTE FILE PATH', font=('TIMES NEW ROMAN', 12)).pack()
ent = Entry(root, textvariable = path, font=('TIMES NEW ROMAN', 12))
ent.pack()

word = StringVar()

Label(root, text = 'GIVE ONE WORD', font=('TIMES NEW ROMAN', 12)).pack()
ent2 = Entry(root, textvariable = word, font=('TIMES NEW ROMAN', 12))
ent2.pack()

exe = StringVar()

Label(root, text  = 'ENTER EXTENSION', font=('TIMES NEW ROMAN', 12)).pack()
ent3 = Entry(root, textvariable = exe, font=('TIMES NEW ROMAN', 12))
ent3.pack()



Button(root, text= 'change',command = rename).pack()
