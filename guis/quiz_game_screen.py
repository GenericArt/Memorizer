from tkinter import *
from random import shuffle
from tkinter import ttk


def gameScreen(self, root, selectedQuestion):
    # create welcome frame
    game_frame = Frame(root)
    game_frame.grid(row=0, column=0, sticky=N + S + W + E)
    game_frame.grid_rowconfigure(1, weight=1)
    game_frame.grid_columnconfigure(0, weight=1)
    game_frame.isgridded = True

    # create all of the main containers
    top_frame = Frame(game_frame, width=450, height=50, pady=3)
    center_frame = Frame(game_frame, width=50, height=40, padx=3, pady=3)
    btm_frame1 = Frame(game_frame, width=450, height=45, pady=3)
    btm_frame2 = Frame(game_frame, width=450, height=60, pady=3)
    btm_frame3 = Frame(game_frame, width=450, height=60, pady=3)

    # layout all of the main containers
    top_frame.grid(row=0, sticky="ew")
    center_frame.grid(row=1, sticky="nsew")
    btm_frame1.grid(row=3, sticky="ew")
    btm_frame2.grid(row=4, sticky="ew")
    btm_frame3.grid(row=5, sticky="ew")

    top_frame.grid_columnconfigure(2, weight=1)
    center_frame.grid_columnconfigure(2, weight=1)

    btm_frame1.grid_columnconfigure(1, weight=1)
    btm_frame1.grid_columnconfigure(2, weight=1)
    btm_frame1.grid_columnconfigure(3, weight=1)

    btm_frame2.grid_columnconfigure(1, weight=1)
    btm_frame2.grid_columnconfigure(2, weight=1)
    btm_frame2.grid_columnconfigure(3, weight=1)

    btm_frame3.grid_columnconfigure(1, weight=1)
    btm_frame3.grid_columnconfigure(2, weight=1)
    btm_frame3.grid_columnconfigure(3, weight=1)

    ## creating various labels and gui items

    instuctLabel = Label(top_frame, text="Answer the question before time runs out!")
    instuctLabel.grid(row=0, column=2)

    verseLabel = Message(center_frame, text=selectedQuestion["question"])
    verseLabel.config(font=("helvetica", 20), aspect=300)
    verseLabel.grid(row=1, column=2, sticky=N + S + W + E)

    sep = ttk.Separator(center_frame)
    sep.grid(row=2, column=2, sticky=W + E, pady=20)



    possibleAnswers = [selectedQuestion['answer'], selectedQuestion['decoyone'], selectedQuestion['decoytwo'], selectedQuestion['decoythree']]
    shuffle(possibleAnswers)

    userVar = StringVar()
    userVar.set("None")

    row = 0
    column = 1

    for answer in possibleAnswers:

        button = Radiobutton(btm_frame1, text=answer, indicatoron=0, value=answer, variable=userVar, width=20, height=1)
        button.grid(row=row, column=column, pady=10, padx=5)

        column += 1

        if column >= 3:
            column = 1
            row += 1


    okBtn = Button(btm_frame2, text="Check Answer", width=25, height=4,
                   command=lambda: self.quizCheckAnswer(userVar, selectedQuestion))
    okBtn.grid(row=0, column=2, pady=20)

    exitBtn = Button(btm_frame3, text="Quit", width=25, height=4,
                     command=lambda: self.screenSwitcher("home"))
    exitBtn.grid(row=0, column=2, pady=20)






