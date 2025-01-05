import tkinter
import os
from tkinter import filedialog


def file_select():
    file_name = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                           filetypes=(('Текстовый файл', '.txt'),
                                                      ('Все файлы', '*')))
    text['text'] = text['text'] + '' + file_name
    os.stat(file_name)


window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x150')
window.configure(bg='black') # Цвет заднего фона (background)
window.resizable(False, False)
text = tkinter.Label(window, text='Файл', height=5, width=65,
                     background='silver', foreground='blue') # Размер окна с текстом
text.grid(column=1, row=1)
button_select = tkinter.Button(window, text='Выбрать файл', width=20, height=3,
                               background='silver', foreground='red',
                               command=file_select) # Кнопка (активация)
button_select.grid(column=1, row=2, pady=5)
window.mainloop()
