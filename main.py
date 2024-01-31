import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pandas as pd


def phone_model():
    try:
        data = pd.read_csv('file.csv')
        data_file = data.drop(columns=data.columns[2:6])
        data_file = data_file.to_dict()

        data_file.get('PHONE NAME')

        input_model = inputmodelentry.get()
        model_key = [x for x in data_file['PHONE MODEL'].keys() if data_file['PHONE MODEL']
                     [x] == input_model.upper()][0]

        result = (data_file['PHONE NAME'][model_key])

        phonespectext.delete(1.0, END)
        phonespectext.insert(1.0, result)

    except IndexError as err:
        tk.messagebox.showerror('ERROR', 'WRONG MODEL NUMBER')


window = tk.Tk()
window.title('HescayModel')
window.geometry('1200x600')
window.configure(background='gray')
modelframe = Frame(window, background='gray')
modelframe.pack(fill=Y)

samsungButton = Button(modelframe, text="Samsung", bg='gray', fg="coral", font=('bold',), border=5, overrelief=RIDGE,
                       relief=FLAT)
samsungButton.grid(column=0, row=0)

samsungButton = Button(modelframe, text="Tecno", bg='gray', fg="coral", font=("bold",), border=5, overrelief=RIDGE,
                       relief=FLAT)
samsungButton.grid(column=1, row=0)

samsungButton = Button(modelframe, text="Infinix", bg='gray', fg="coral", font=('bold',), border=5, overrelief=RIDGE,
                       relief=FLAT)
samsungButton.grid(column=2, row=0)

samsungButton = Button(modelframe, text="Itel", bg='gray', fg="coral", font=('bold',), border=5, overrelief=RIDGE,
                       relief=FLAT)
samsungButton.grid(column=3, row=0)

samsungButton = Button(modelframe, text="Redmi", bg='gray', fg="coral", font=('bold',), border=5, overrelief=RIDGE,
                       relief=FLAT)
samsungButton.grid(column=4, row=0)

samsungButton = Button(modelframe, text="Oppo", bg='gray', fg="coral", font=('bold',), border=5, overrelief=RIDGE,
                       relief=FLAT)
samsungButton.grid(column=5, row=0)

samsungButton = Button(modelframe, text="Iphone", bg='gray', fg="coral", font=('bold',), border=5, overrelief=RIDGE,
                       relief=FLAT)
samsungButton.grid(column=6, row=0)

samsungButton = Button(modelframe, text="Add model", bg='gray', fg="coral", font=('bold',), border=5, overrelief=RIDGE,
                       relief=FLAT)
samsungButton.grid(column=7, row=0)

phonedetailsframe = Frame(window, background='gray')
phonedetailsframe.pack()

searchframe = LabelFrame(phonedetailsframe, text="SEARCH", bg='gray')
searchframe.grid(column=0, row=0)

inputmodelLabel = Label(searchframe, text="Input Model", width=15, height='3', bg='gray', font=('bold',))
inputmodelLabel.grid(column=0, row=0)

inputmodelentry = Entry(searchframe, font=('bold',), borderwidth=5, border=5)
inputmodelentry.grid(column=0, row=1)

inputmodelbutton = Button(searchframe, text='Search', font=('bold', 15,), relief=GROOVE, overrelief=FLAT, bg='gray',
                          command=phone_model)
inputmodelbutton.grid(column=0, row=2, pady=15)

inputnameLabel = Label(searchframe, text="Input Name", width=10, height="3", bg='gray', font=('bold',))
inputnameLabel.grid(column=0, row=3)

inputnamelentry = Entry(searchframe, font=('bold',), borderwidth=5)
inputnamelentry.grid(column=0, row=4)

inputnamelbutton = Button(searchframe, text='Search', font=('bold', 15,), relief=GROOVE, overrelief=FLAT, bg='gray')
inputnamelbutton.grid(column=0, row=5, pady=15)

phoneinfoframe = LabelFrame(phonedetailsframe, text='PHONEINFO', bg='gray', width='50', height='100')
phoneinfoframe.grid(column=1, row=0)

phone = Label(phoneinfoframe, text='Phone Specifications', font=('times new roman', 10, 'bold'), bd=0)
phone.grid(column=1, row=0)

phone = Label(phoneinfoframe, text='Phone dimensions and image', font=('times new roman', 10, 'bold'), bd=0)
phone.grid(column=2, row=0)

phone = Label(phoneinfoframe, text='Phone screen and L C D types', font=('times new roman', 10, 'bold'), bd=0)
phone.grid(column=3, row=0)

phonespectext = Text(phoneinfoframe, width=20, height=15, borderwidth=10, padx=20, font=('bold',))
phonespectext.grid(column=1, row=1, padx=10)

phonedimtext = Text(phoneinfoframe, width=20, height=15, borderwidth=10, padx=20, font=('bold',))
phonedimtext.grid(column=2, row=1, pady=10)

phonelcdimg = Text(phoneinfoframe, width=20, height=15, borderwidth=10, padx=20, font=('bold',))
phonelcdimg.grid(column=3, row=1, padx=10)

menu_bar = tk.Menu(window)
menu_1 = tk.Menu(menu_bar, tearoff=1)
menu_1.add_command(label="Item1")
menu_1.add_command(label="Item2")
menu_1.add_command(label="Item3")
menu_bar.add_cascade(label="file", menu=menu_1)

window.config(menu=menu_bar, background='gray')
window.mainloop()
