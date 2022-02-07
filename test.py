import tkinter as tk
from tkinter import END, messagebox
import random
from turtle import bgcolor, bgpic

window = tk.Tk()
window["bg"] = "#B0C4DE" 
window.title("Угадай число")
window.geometry("800x600")
number = random.randint(1,101)
tries = 0

label1 = tk.Label(text="Угадай число",
                    bg = "#B0C4DE",
                    foreground= "#8B0000",
                    font= ('Courier New', 22,'bold'),
                    pady="25"
                    )
label1.pack()

label2 = tk.Label(text="Давайте проверим Вашу интуицию. \nЗагаданное число находится в диапазоне от 1 до 100. \nУ Вас есть 10 попыток. \nГотовы?",
                    bg = "#B0C4DE",
                    foreground= "#191970",
                    font= ('Courier New', 14),
                    pady="20",
                    )
label2.pack()

label3 = tk.Label(text="Введите загаданное число:",
                    bg = "#B0C4DE",
                    foreground= "#DC143C",
                    font= ('Courier New', 15),
                    pady="5",
                    )
label3.pack()


entry = tk.Entry(width=15,
                font= ('Courier New', 15),
                )
entry.pack()


def compare():
    global tries
    tries += 1
    if tries == 10:
        button.config(state="disabled")
        tk.messagebox.showinfo("Увы :(", "Вы использовали все попытки")
    guess = int(entry.get())
    if guess == " ":
        tk.messagebox.showerror("ОШИБКА!", "Поле не может быть пустым!")
    elif guess > number:
        tk.messagebox.showinfo("Попробуйте еще", "Число должно быть меньше!")
    elif guess < number:
        tk.messagebox.showinfo("Попробуйте еще", "Число должно быть больше!")
    elif guess == number:
        tk.messagebox.showinfo("Урааа!", "Это ПРАВИЛЬНЫЙ ОТВЕТ!")
        
        tk.messagebox.showinfo("Поздравляю!", "Вы затратили на отгадывание всего лишь " + str(tries) + " попыток\n")
    else:
        tk.messagebox.showerror("ОШИБКА!", "Ввод неверный!")
    entry.delete(0, END)
    

button = tk.Button(text="Проверить",
                    command=compare,
                    background="#2E8B57",
                    foreground="#8B0000",
                    width=18, 
                    pady="6",
                    font=("Courier New", 12, 'bold'),
                    activebackground="#F08080",
                    activeforeground="#fff"
                    )          
button.pack(pady="6")


button2 = tk.Button(text="Выйти из игры",
                    command=window.quit, 
                    width=18,  
                    pady="6", 
                    bg="#8B0000", 
                    font=("Courier New", 12, 'bold'), 
                    activebackground="#F08080",
                    activeforeground="#fff"
                    )
button2.pack(pady="35")


window.mainloop()