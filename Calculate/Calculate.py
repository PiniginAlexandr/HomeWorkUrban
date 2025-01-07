import tkinter
from tkinter import Button, Entry


"""
Создание окна
"""
window = tkinter.Tk()
window.title('Calculate')
window.geometry('230x280')
window.configure(bg='black')
window.resizable(False, False)
"""
Переменные для хранения состояния
"""
first_number = None
operation = None
percent_value = None
"""
Контроль ввода
"""
def button_click(value):
    current = result_entry.get()
    result_entry.delete(0, tkinter.END)
    result_entry.insert(0, current + str(value))

def set_operation(op):
    global first_number, operation
    first_number = float(result_entry.get())
    operation = op
    result_entry.delete(0, tkinter.END)
"""
Работа клавиш
"""
def calculate():
    global first_number, operation, percent_value
    if operation == '%':
        percent_value = float(result_entry.get())
        result = (first_number * percent_value) / 100
        result_entry.delete(0, tkinter.END)
        result_entry.insert(0, str(result))
        return

    second_number = float(result_entry.get())
    result = None

    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        if percent_value is not None:
            second_number = (first_number * percent_value) / 100
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        if second_number != 0:
            result = first_number / second_number
        else:
            result = 'Ошибка'

    result_entry.delete(0, tkinter.END)
    result_entry.insert(0, str(result))

    first_number = None
    operation = None
    percent_value = None

"""
Контроль выравнивания колон и строк
"""
for i in range(4):
    window.columnconfigure(i, weight=1)

for i in range(7):
    window.rowconfigure(i, weight=1)
"""
Окно ввода
"""
result_entry = Entry(window, width=20, font=('Arial', 24),
                     justify='right', background='black', foreground='white',
                     bd=0, highlightthickness=0)
result_entry.grid(column=0, row=1, columnspan=4, padx=5, pady=(5, 10))

"""
Создание кнопок(клавиш)
column = Колонна
row = Строка
padx = ось x <--->
pady = ось y |(вверх или вниз)
"""
def create_button(text, row, column, foreground, colspan=1):
    return Button(window, text=text, width=6, height=2,
                  background='black', font=('Arial', 10), foreground=foreground,
                  bd=0, highlightthickness=0,
                  command=lambda:button_click(text)
                  if text not in ['+', '-', '*', '/', '%']
                  else set_operation(text)
                  ).grid(row=row, column=column, columnspan=colspan, padx=1, pady=1)


def button_func(text, row, column, foreground, colspan=1):
    return Button(window, text=text, width=6, height=2, font=('Arial', 10),
                  background='black', foreground=foreground,
                  bd=0, highlightthickness=0).grid(row=row,
                                                   column=column, columnspan=colspan, padx=1, pady=1)
"""
Кнопки управления
"""

button_func('Вид', 0, 0, 'white')
button_func('Справка', 0, 1, 'white')
button_func('C', 2, 0, 'orange')
button_func('⌫', 2, 1, 'orange')
create_button('%', 2, 2, 'orange')
create_button('/', 2, 3, 'orange')
"""
Кнопки операций
"""
create_button('*', 3, 3, 'orange')
create_button('-', 4, 3, 'orange')
create_button('+', 5, 3, 'orange')
equals_button = Button(window, text='=', width=6,height=2,
                       background='black', foreground='orange',
                       bd=0, highlightthickness=0,
                       command=calculate)
equals_button.grid(row=6,column=3,padx=1,pady=1)

"""
Кнопки чисел
"""
create_button('7', 3, 0,'white')
create_button('8', 3, 1,'white')
create_button('9', 3, 2,'white')
create_button('4', 4, 0,'white')
create_button('5', 4, 1,'white')
create_button('6', 4, 2,'white')
create_button('1', 5, 0,'white')
create_button('2', 5, 1,'white')
create_button('3', 5, 2,'white')
create_button('0', 6, 1,'white')
create_button('.', 6, 2,'white')

window.mainloop()