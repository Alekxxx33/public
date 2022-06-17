from copyreg import pickle
from select import select
from tkinter import ANCHOR, mainloop
from turtle import title
import pickle
from thinker import *
from thinkter.font import Font

my_font = Font(
    family="Brush Script MT",
    size=30,
    weight="bold",
)
my_frame= Frame(root)
my_frame.pack(pady=10)

root = Tk()
root.title('Codemy.com-ToDoList!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

my_font =Font(
    family="Brush MT",
    size=30,
    weight="bold",
)

my_list= Listbox(my_frame,
font=my_font
weight= 25
height=5,
bg="SystemButtonFace",
bd=0,
fg="#464646",
highlightthickness=0,
selectbackground="#a6a6a6"
activestyle="none"
)

my_list.pack(side=LEFT, fill=BOTH)

stuff=["Walk the Dog","Take a nap"]
for item in stuff:
    my_list.insert(END,item)
my_scrollbar= Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar)
my_scrollbar.config(command=my_list.view)
my_entry= Entry(root.font="Helvetica")
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

delete_button = Button(button_frame,text="DELETE Item" command=delete_item)
add_button = Button(button_frame text="Add Item" command=add_item)
cross_button = Button(button_frame text="cross Item" command=cross_off_item)
uncross_button = Button(button_frame text="uncross Item" command=uncross_item)


def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END,my_entry.get())
def cross_off_item():
    my_list.itemconfig(
    my_list.curseselection(),
    fg="#dedede"
)
my_list.selectin_clear(0,END)
def uncross_item():

def deleted_crossed():
count = 0
while count < my_list.size():
    if my_list.itemcget(count,"fg") == "dedede"
    = my_list.delete(my_list.index(count))

else:
count+= 1


def save_list():
file_name= filedialog.asksaveasfilesname(initialdir="C:/gui/data")
   title="Save File",
   filetypes=(("Dat Files","*.dat"), ("All Files","*'*"))

if file_name:
if file_name.endswith(".dat"):
    pass
else:
    file_name= f'{file_name}.dat'

    stuff = my_list.get(0,END)

    output_file = open(file_name)

pickle.dump(stuff, output_file)
def open_list():
file_name=open filedialog.asksaveasfilesname(initialdir="C:/gui/data")
   title=" File",
   filetypes=(("Dat Files","*.dat"), ("All Files","*'*"))

    if file_name:
        my_list.delete(0,END)
        input_file = open(file_name,'rb')
        stuff= pickle.load(input_file_name)
        for item in stuff:
            my_list.insert(END,0)
def delete_list():
my_list.delete(0,END)


    pass
my_menu= Menu(root)
root.config(menu=my_menu)
file_menu= Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(;abel="Save List", command=save_list)

delete_button.grid(row=0 ,column=0)
add_button.grid(row=0 ,column=1)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0 ,column=3)
deleted_crossed_button.grid(row=0 ,column=3)
root mainloop()







