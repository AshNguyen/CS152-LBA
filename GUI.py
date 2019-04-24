# -*- coding: utf-8 -*-

import csv
import itertools
import tkinter as tk
# from query_KB import query_the_KB
from Prolog import query

##### Constant #####
HEIGHT = 620
WIDTH = 800

COLOR1 = '#cdd3c2'
COLOR2 = '#eee3dd'

BIG_FONT = ("Helvetica", 20)
MEDIUM_FONT = ("Helvetica", 13, 'bold')

QUESTIONS = {
	"food_type":{
    "question": "What type of food do you want?",
    "range": ["Asian", "Italian", "Peruvian", "Argentinian","Contemporary", "Ice-cream", "Cafe"]
    },

    "price":{
    "question": "What price range is acceptable?",
    "range": ["$", "$$", "$$$"]
    },

    "distance":{
    "question": "How far are you willing to travel?",
    "range": ["Close", "Medium", "Far"]
    }
}

def read_data(filename="restaurant_data.csv"):
    res_data = {}
    with open(filename, "r") as f:
        table = csv.reader(f)
        next(table)
        for row in table:
            res_data[str(row[0])] = \
            [ "Price: " + row[9],\
              "Distance: " + row[10],\
              "Type of food: " + row[11],\
              "Address: " + row[1].split(',')[0],
              "Opening hour: \n" + "---------------\n"+ "Monday: " + row[2]+'\nTuesday: '+row[3]+'\nWednesday: '+row[4]+\
              '\nThursday: '+row[5]+'\nFriday: '+row[6]+'\nSaturday: '+row[7]+'\nSunday: '+row[8]]
    return res_data

INFO = read_data()

##### Basic Structure of the GUI #####
root = tk.Tk()
root.title(" Buenos Aires Restaurant Expert System")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.grid()

left_frame = tk.Frame(root, bg=COLOR1)
left_frame.place(relx=0.025, rely=0.025, relwidth=0.45, relheight=0.95)

right_frame = tk.Frame(root, bg=COLOR1)
right_frame.place(relx=0.525, rely=0.025, relwidth=0.45, relheight=0.95)

left_header = tk.Label(left_frame, bg=COLOR1,text='What do you want to have today?', font=BIG_FONT)
left_header.place(relx=0.025, rely=0.01, relwidth=0.95, relheight=0.1)

right_header = tk.Label(right_frame, bg=COLOR1,text='Here is our recommendation!', font=BIG_FONT)
right_header.place(relx=0.025, rely=0.01, relwidth=0.95, relheight=0.1)

question_canvas = tk.Canvas(left_frame, bg=COLOR2, highlightthickness=0)
question_canvas.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

result_canvas = tk.Canvas(right_frame, bg=COLOR2, highlightthickness=0)
result_canvas.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

scrollbar = tk.Scrollbar(result_canvas)
scrollbar.place(relx=0.95, relwidth=0.05, relheight=1)
result_canvas.config(yscrollcommand = scrollbar.set)
scrollbar.config(command=result_canvas.yview)

scroll_frame = tk.Frame(result_canvas, bg=COLOR2)
result_canvas.create_window((5,5), window=scroll_frame, anchor='nw')

##### Display questions and results #####
# Reference: https://www.python-course.eu/tkinter_checkboxes.php

option_vals = {}
option_widgets = {}

for i in QUESTIONS:
    question = tk.Label(question_canvas, bg=COLOR2, fg='black',text= QUESTIONS[i]['question'], font=MEDIUM_FONT)
    question.grid(sticky='w', padx=15, pady=7)
    option_vals[i] = {}
    for option in QUESTIONS[i]["range"]:
        v = tk.IntVar()
        c = tk.Checkbutton(question_canvas, bg=COLOR2, text=option, variable=v)
        c.grid(sticky='w', padx=15, pady=2)
        option_vals[i][option] = v # for accessing user_input
        option_widgets[option] = c #for clearing

result_labels = []

##### Search and show results #####
def parse_input(): 
    user_query = {}
    for question in option_vals:
        user_query[question] = []
        for option in option_vals[question]:
            if option_vals[question][option].get() == 1:
                user_query[question].append(option)
        if user_query[question] == []:
            user_query[question] = QUESTIONS[question]['range']

    user_query = list(itertools.product(*user_query.values()))

    return user_query

def search():
    user_query = parse_input()
    recommendations = query(user_query)
    display_result(recommendations)

def clear():
    if len(result_labels) != 0:
        for result in result_labels:
            result.destroy()

    for option in option_widgets:
        option_widgets[option].deselect()

def display_result(recommendations):
    for recommendation in recommendations:

        name = tk.Label(scroll_frame, text=recommendation, bg=COLOR2, font=MEDIUM_FONT)
        name.grid(sticky='w', padx=15, pady=5)
        result_labels.append(name)

        infos = INFO[recommendation]

        for item in infos:
            info = tk.Label(scroll_frame, text= item, bg=COLOR2, justify=tk.LEFT)
            info.grid(sticky='w', padx=15, pady=2)
            result_labels.append(info)

    result_canvas.configure(scrollregion=(0,0,WIDTH,300*len(recommendations)))

search_button = tk.Button(left_frame, text = "Search", command=search)
search_button.place(relx=0.4, rely=0.925, relwidth=0.2, relheight=0.05)

clear_button = tk.Button(right_frame, text = "Clear", command=clear)
clear_button.place(relx=0.4, rely=0.925, relwidth=0.2, relheight=0.05) 

##### Run the main program #####
root.mainloop()