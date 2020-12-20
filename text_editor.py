import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.messagebox import showerror
from tkinter import messagebox, filedialog

from settings import * # import settings

app = tkinter.Tk() # create a window of our app

text = tkinter.Text(app, width=WIDTH - 50, height=HEIGHT, wrap ='word') # create a text box

class Text_editor():
    def __init__(self):
        self.file_name = tkinter.NONE

    def new_file(self):
        self.file_name = 'Неизвестный'
        text.delete('1.0', tkinter.END)
    
    def open_file(self):
        inp = filedialog.askopenfilename()
        if inp is None:
            return
        text.delete('1.0', tkinter.END)
        f = open(inp, encoding='utf-8')
        data = f.read()
        text.insert('1.0', data)
        f.close()
        
    def save_file(self):
        data = text.get('1.0', tkinter.END)
        output = open(self.file_name, 'w', encoding='utf-8')
        output.write(data)
        output.close()
    
    def save_as_file(self):
        output = asksaveasfile(mode="w", defaultextension="txt")
        data = text.get('1.0', tkinter.END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title="Ошибка!", message="Ошибка при сохранении файла")
    
    def get_info(self):
        messagebox.showinfo('Справка', "Информация о нашем приложении! Спасибо, что его используете :D")