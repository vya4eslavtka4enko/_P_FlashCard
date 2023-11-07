import csv
from tkinter import *
from tkinter import Tk
import pandas
import random
import time
from csv import writer

# constants
BACKGROUND_COLOR = "#B1DDC6"
FONT = 'Ariel'
# function
data = pandas.read_csv('data/french_words.csv')
dict_1 = data.to_dict(orient="records")

current_card = {}


def Rotate():
    canvas.create_image(400, 263, image=back_size)
    label_title.config(text="English")
    label_translate.config(text=f'{current_card["English"]}')


def GenereteWord():
    global current_card
    current_card = random.choice(dict_1)
    label_translate.config(text=f'{current_card["French"]}')
    canvas.create_image(400, 263, image=front_size)
    label_title.config(text="French")
    flip_timer = window.after(3000, func=Rotate)


def saveProgress():
    with open("save_progress.json", "a") as progress_file:
        writer_object = writer(progress_file)
        writer_object.writerow(current_card['French'])
        print(current_card)
        GenereteWord()


# interface
window = Tk()
window.minsize(width=850, height=576)
window.config(bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=Rotate)

canvas = Canvas(width=800, height=526)
front_size = PhotoImage(file='images/card_front.png')
back_size = PhotoImage(file='images/card_back.png')
canvas.create_image(400, 263, image=front_size)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR, border=0)
canvas.grid(column=0, row=0, columnspan=2, padx=50, pady=50)

label_title = Label()
label_title.config(text='French', font=(FONT, 45, "italic"), bg="white", fg="black")
label_title.grid(column=0, row=0)
label_title.place(x=400, y=150)

label_translate = Label()
label_translate.config(font=(FONT, 60, "bold"), bg="white", fg="black")
label_translate.grid(column=1, row=1)
label_translate.place(x=400, y=263)

button_right = PhotoImage(file='images/right.png')
button_wrong = PhotoImage(file='images/wrong.png')
button_ok = Button(image=button_right)
button_ok.config(width=100, highlightbackground=BACKGROUND_COLOR, command=saveProgress)
button_ok.grid(column=0, row=2)
button_cancel = Button(image=button_wrong)
button_cancel.config(width=100, highlightbackground=BACKGROUND_COLOR, command=GenereteWord)
button_cancel.grid(column=1, row=2)

GenereteWord()

window.mainloop()
