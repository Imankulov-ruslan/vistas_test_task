import csv
import tkinter
import graphics
from os import path
from tkinter import messagebox

columns = ['Название',"Цена","Ссылка","Примечание"]
data = []

window = graphics.CreateWindow('WishList')
window.lable('Введите данные в Ваш WishList')
window.lable.pack(fill='both',expand=1)

input_frame = tkinter.LabelFrame(master=window.window,text='Ввод данных',relief="raised")
input_frame.pack(fill='both',expand=1)

wish_list_frame = tkinter.LabelFrame(master=window.window,text='WishList')
wish_list_frame.pack(fill='both',expand=1)

tkinter.Label(master=input_frame, text='Название').grid(row=0,column=0)

name = tkinter.Entry(master=input_frame)
name.grid(row=1,column=0)

tkinter.Label(master=input_frame,text='Цена').grid(row=0,column=1)

cost = tkinter.Entry(master=input_frame)
cost.grid(row=1,column=1)

tkinter.Label(master=input_frame,text='Ссылка').grid(row=0,column=2)

hyperlink = tkinter.Entry(master=input_frame)
hyperlink.grid(row=1,column=2)

tkinter.Label(master=input_frame,text='Примечание').grid(row=0,column=3)

note = tkinter.Entry(master=input_frame)
note.grid(row=1,column=3)

wish_list = tkinter.Listbox(wish_list_frame)
wish_list.pack(side='left',fill='both',expand=1)

scroll = tkinter.Scrollbar(master=wish_list_frame,command=wish_list.yview)
scroll.pack(side='left', fill='y')
wish_list.config(yscrollcommand=scroll.set)

def add_to_wishlist():

    value = {'Название':name.get(), "Цена":cost.get(), "Ссылка":hyperlink.get(), "Примечание":note.get()}
    data.append(value)
    text = ''
    for k,v in value.items():
        if v == "":
            return messagebox.showerror('Ошибка', 'Заполните пустые поля')
        text += f'{k} : {v} '
    wish_list.insert('end',text)

def del_form_wishlist():
    try:
        wish_list.delete(wish_list.curselection())
    except:
        messagebox.showerror('Ошибка', 'Не выбран элемент для удаления')

def add_to_file():
    filename = path.expandvars(r"%HOMEDRIVE%${HOMEPATH}\file.csv")
    with open(filename,'a', newline='') as file:
        writer = csv.DictWriter(file,delimiter=";", fieldnames=columns)
        writer.writeheader()
        for i in data:
            writer.writerow(i)
    messagebox.showinfo('',f'WishList выгружен в файл: {filename}')

btn_frame = tkinter.Frame(master=window.window).pack()

add_btn = tkinter.Button(master=btn_frame,command=add_to_wishlist, text='Добавить')
add_btn.pack(side='left', fill='x',expand=1)

del_btn = tkinter.Button(master=btn_frame,command=del_form_wishlist, text='Удалить')
del_btn.pack(side='left', fill='x',expand=1)

upload_btn = tkinter.Button(master=btn_frame,command=add_to_file, text='Выгрузить')
upload_btn.pack(side='left', fill='x',expand=1)

window.update_and_show_window()