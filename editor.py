import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.messagebox import showerror
from tkinter import messagebox, filedialog

from settings import * # import settings

from text_editor import *

###app = tkinter.Tk() # create a window of our app
app.title(APP_NAME) # name of our app
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)

###text = tkinter.Text(app, width=WIDTH - 50, height=HEIGHT, wrap ='word') # create a text box
scroll = Scrollbar(app, orient=VERTICAL, command=text.yview) # create scroll
scroll.pack(side="right", fill="y") # locate a scroll
text.configure(yscrollcommand=scroll.set) # link text and scroll
text.pack() # locate text box

menuBar = tkinter.Menu(app)# create main menu

editor = Text_editor()

app_menu = tkinter.Menu(menuBar) # a file drop-down menu
app_menu.add_command(label="Новый файл", command=editor.new_file)
app_menu.add_command(label="Открыть", command=editor.open_file)
app_menu.add_command(label="Сохранить", command=editor.save_file)
app_menu.add_command(label="Сохранить как", command=editor.save_as_file)

reference_menu = tkinter.Menu(menuBar) # a reference drop-down menu
reference_menu.add_command(label="Посмотреть справку")
reference_menu.add_command(label="Отправить отзыв")
reference_menu.add_command(label="О программе", command=editor.get_info)

app.config(menu = menuBar) #  publish a menu

menuBar.add_cascade(label="Файл", menu = app_menu)
menuBar.add_cascade(label="Вид")
menuBar.add_cascade(label="Справка", menu = reference_menu)
menuBar.add_cascade(label="Выход", command = app.quit)



app.mainloop() # infinite loop