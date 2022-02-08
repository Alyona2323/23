import tkinter as tk
from tkinter import END, messagebox
import random
from turtle import bgcolor, bgpic

window = tk.Tk()
window["bg"] = "#B0C4DE" 
window.title("Guess the number")
window.geometry("800x600")
number = random.randint(1,101)
tries = 0

label1 = tk.Label(text="Guess the number",
                    bg = "#B0C4DE",
                    foreground= "#8B0000",
                    font= ('Courier New', 22,'bold'),
                    pady="25"
                    )
label1.pack()

label2 = tk.Label(text="Let's test your intuition. \nThe hidden number is in the range from 1 to 100.\n You have 10 tries. \nReady?",
                    bg = "#B0C4DE",
                    foreground= "#191970",
                    font= ('Courier New', 14),
                    pady="20",
                    )
label2.pack()

label3 = tk.Label(text="Enter the hidden number: ",
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
        tk.messagebox.showinfo("Alas :(", "You have used all your attempts")
    guess = int(entry.get())
    if guess == " ":
        tk.messagebox.showerror("ERROR!", "The field cannot be empty!")
    elif guess > number:
        tk.messagebox.showinfo("Try again", "The number must be less!")
    elif guess < number:
        tk.messagebox.showinfo("Try again", "The number should be more!")
    elif guess == number:
        tk.messagebox.showinfo("Bravo!", "That's the RIGHT ANSWER!")
        
        tk.messagebox.showinfo("Congratulations!", "You only spent on guessing" + str(tries) + " attempts\n")
    else:
        tk.messagebox.showerror("ERROR!", "Invalid input!")
    entry.delete(0, END)
    

button = tk.Button(text="Check",
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


button2 = tk.Button(text="Quit the game",
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