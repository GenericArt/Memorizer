from tkinter import *


def showMoodsScreen(self, root, moodTypes):
    # create welcome frame
    game_frame = Frame(root)
    game_frame.grid(row=0, column=0, sticky=N + S + W + E)
    game_frame.grid_rowconfigure(1, weight=1)
    game_frame.grid_columnconfigure(0, weight=1)
    game_frame.isgridded = True

    # create all of the main containers
    top_frame = Frame(game_frame, width=450, height=50, pady=3)
    center_frame = Frame(game_frame, width=480, height=400, padx=10, pady=3)
    btm_frame1 = Frame(game_frame, width=450, height=45, pady=3)
    btm_frame2 = Frame(game_frame, width=450, height=60, pady=3)
    btm_frame3 = Frame(game_frame, width=450, height=60, pady=3)

    # layout all of the main containers
    top_frame.grid(row=0, sticky="ew")
    center_frame.grid(row=1, sticky="nsew")
    btm_frame1.grid(row=3, sticky="ew")
    btm_frame2.grid(row=4, sticky="ew")
    btm_frame3.grid(row=5, sticky="ew")

    center_frame.grid_columnconfigure(0, weight=1)
    center_frame.grid_columnconfigure(1, weight=1)
    center_frame.grid_columnconfigure(2, weight=1)
    center_frame.grid_columnconfigure(3, weight=1)
    btm_frame3.grid_columnconfigure(2, weight=1)

    row = 0
    column = 0

    for mood in moodTypes:

        btn = Button(center_frame, text=mood, command=lambda x=mood :self.moodTypeSelection(x))
        btn.grid(row=row, column=column, padx=4, pady=7)
        column += 1
        if column >= 3:
            column = 0
            row += 1

    exitBtn = Button(btm_frame3, text="Exit", width=25, height=4,
                     command=lambda: self.screenSwitcher("home"))
    exitBtn.grid(row=0, column=2, pady=20)
