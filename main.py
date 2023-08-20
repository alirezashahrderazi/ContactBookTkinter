from  tkinter import *
from  tkinter import messagebox
import webbrowser
import os
#pip
import pyperclip

#=======================  Settings  ========================
root=Tk()
root.title('Contact Book')
root.geometry('650x300')
#root.resizable(width=False,height=False)
background='#121212'
root.config(bg=background)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH=os.path.join(BASE_DIR,"data_file.txt")
#=======================  Functions  ========================
def exit():
    choice=messagebox.askquestion('Exit Application','Are you sure want to close the application')
    if choice=='yes':
        root.destroy()

def add_contact():
    contact_string=nameEntry.get()+':'+phoneEntry.get()
    listBox.insert(END,contact_string)
    nameEntry.delete(0,END)        
    phoneEntry.delete(0,END)

def delet_contact():
    listBox.delete(ANCHOR)

def save_list():
    with open(PATH,'w')as f:
        list_tuple=listBox.get(0,END)
        for item in list_tuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item+'\n')

def open_list():
    webbrowser.open(BASE_DIR)

def openDB():
    with open(PATH,'r')as f:
         for line in f:
             listBox.insert(END,line)       
def copy_number():
    select_contact=listBox.get(ANCHOR)
    number=select_contact.split(':')  
    pyperclip.copy(number[1].replace('\n',''))  
#=======================  Entrys And Labels  ========================
nameLable=Label(root,text="Contact Name",background=background,fg='white',font=('calibri',12),anchor='w',justify=LEFT)
nameLable.place(relx=0.1,rely=0.1,anchor='c')
nameEntry=Entry(root,bg='white',fg=background,width=30,borderwidth=2)
nameEntry.place(relx=0.4,rely=0.1,anchor='c')

phoneLable=Label(root,text="  Contact Number",background=background,fg='white',font=('calibri',12),anchor='w',justify=LEFT)
phoneLable.place(relx=0.1,rely=0.2,anchor='c')
phoneEntry=Entry(root,bg='white',fg=background,width=30,borderwidth=2)
phoneEntry.place(relx=0.4,rely=0.2,anchor='c')

#=======================  Button  ========================
addBtn=Button(root,text='Add Contact',bg=background,fg='white',padx=125,command=add_contact)
addBtn.place(relx=0.29,rely=0.35,anchor='c')

saveBtn=Button(root,text='Save List',bg=background,fg='white',padx=135,command=save_list)
saveBtn.place(relx=0.29,rely=0.5,anchor='c')

copyPhoneBtn=Button(root,text='Save List',bg=background,fg='white',borderwidth=3,padx=10)
copyPhoneBtn.place(relx=0.15,rely=0.65,anchor='c')

copyPhoneBtn=Button(root,text='Copy Phone Number',bg=background,fg='white',borderwidth=3,padx=10,command=copy_number)
copyPhoneBtn.place(relx=0.15,rely=0.65,anchor='c')

deletBtn=Button(root,text='  Delet Contact  ',bg=background,fg='white',borderwidth=3,padx=25,command=delet_contact)
deletBtn.place(relx=0.15,rely=0.77,anchor='c')

openSaveBtn=Button(root,text='  Open Save File ',bg=background,fg='white',borderwidth=3,padx=30,command=open_list)
openSaveBtn.place(relx=0.42,rely=0.65,anchor='c')

exitBtn=Button(root,text='Exit App',bg=background,fg='white',borderwidth=3,padx=50,command=exit)
exitBtn.place(relx=0.42,rely=0.77,anchor='c')


listBox=Listbox(root,width=40,height=15)
listBox.place(relx=0.75,rely=0.45,anchor='c')







openDB()
root.mainloop()