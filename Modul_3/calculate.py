import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    number_answer.delete(0, 'end')
    number_answer.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=4, height=4, command=add)
button_add.place(x=310, y=200)
button_sub = tk.Button(window, text='-', width=4, height=4, command=sub)
button_sub.place(x=310, y=275)
button_mul = tk.Button(window, text='*', width=4, height=4, command=mul)
button_mul.place(x=310, y=125)
button_div = tk.Button(window, text='/', width=4, height=4, command=div)
button_div.place(x=310, y=50)
number1_entry = tk.Entry(window, width=37)
number1_entry.place(x=60, y=22)
number2_entry = tk.Entry(window, width=37)
number2_entry.place(x=60, y=62)
number_answer = tk.Entry(window, width=37)
number_answer.place(x=60, y=102)
number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=60, y=0)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=60, y=40)
num_answer = tk.Label(window, text='Ответ:')
num_answer.place(x=60, y=80)
window.mainloop()

