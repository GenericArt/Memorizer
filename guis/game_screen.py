from tkinter import *
from tkinter import ttk



def multi_choise_screen(self, root, selectedVerse, allDecoyWordsDict):
	pass
	# create welcome frame
	game_frame = Frame(root)
	game_frame.grid(row=0, column=0, sticky=N+S+W+E)
	game_frame.grid_rowconfigure(1, weight=1)
	game_frame.grid_columnconfigure(0, weight=1)
	game_frame.isgridded = True

	# create all of the main containers
	top_frame = Frame(game_frame, width=450, height=50, pady=3)
	center_frame = Frame(game_frame, width=50, height=40, padx=3, pady=3)
	btm_frame1 = Frame(game_frame, width=450, height=45, pady=3)
	btm_frame2 = Frame(game_frame,  width=450, height=60, pady=3)
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

	instuctLabel = Label(top_frame, text="Fill in the blanks!")
	instuctLabel.grid(row=0, column=2)

	verseLabel = Message(center_frame, text=selectedVerse["verse"])
	verseLabel.config(font=("helvetica", 20), aspect=300)
	verseLabel.grid(row=1, column=2, sticky=N+S+W+E)

	sep = ttk.Separator(center_frame)
	sep.grid(row=2, column=2, sticky=W+E, pady=20)




	# creating answer buttons

	row1Var = StringVar()
	row2Var = StringVar()
	row3Var = StringVar()

	row1AnsBtn1 = Radiobutton(btm_frame1, indicatoron=0, highlightcolor="blue", variable=row1Var, width=12, height=2)
	row1AnsBtn1.grid(row=0, column=1)
	row1AnsBtn2 = Radiobutton(btm_frame1, indicatoron=0, variable=row1Var, width=12, height=2)
	row1AnsBtn2.grid(row=0, column=2)
	row1AnsBtn3 = Radiobutton(btm_frame1, indicatoron=0, variable=row1Var, width=12, height=2)
	row1AnsBtn3.grid(row=0, column=3)
	row1Label1 = Label(btm_frame1, text="Answer 1: ")
	row1Label1.grid(row=0, column=0)

	row2AnsBtn1 = Radiobutton(btm_frame1, indicatoron=0, variable=row2Var, width=12, height=2)
	row2AnsBtn1.grid(row=1, column=1)
	row2AnsBtn2 = Radiobutton(btm_frame1, indicatoron=0, variable=row2Var, width=12, height=2)
	row2AnsBtn2.grid(row=1, column=2)
	row2AnsBtn3 = Radiobutton(btm_frame1, indicatoron=0, variable=row2Var, width=12, height=2)
	row2AnsBtn3.grid(row=1, column=3)
	row1Label2 = Label(btm_frame1, text="Answer 2: ")
	row1Label2.grid(row=1, column=0)

	row3AnsBtn1 = Radiobutton(btm_frame1, indicatoron=0, variable=row3Var, width=12, height=2)
	row3AnsBtn1.grid(row=2, column=1)
	row3AnsBtn2 = Radiobutton(btm_frame1, indicatoron=0, variable=row3Var, width=12, height=2)
	row3AnsBtn2.grid(row=2, column=2)
	row3AnsBtn3 = Radiobutton(btm_frame1, indicatoron=0, variable=row3Var, width=12, height=2)
	row3AnsBtn3.grid(row=2, column=3)
	row1Label3 = Label(btm_frame1, text="Answer 3: ")
	row1Label3.grid(row=2, column=0)


	butRow1 = [row1AnsBtn1, row1AnsBtn2, row1AnsBtn3]
	butRow2 = [row2AnsBtn1, row2AnsBtn2, row2AnsBtn3]
	butRow3 = [row3AnsBtn1, row3AnsBtn2, row3AnsBtn3]

	buttonsDict = {"decoy1":butRow1, "decoy2":butRow2, "decoy3":butRow3}

	for key in allDecoyWordsDict.keys():
		words = allDecoyWordsDict[key]
		buttons = buttonsDict[key]
		for word, button in zip(words, buttons):
			button.configure(text=word, value=word)


	userAnswers = {"answer1":row1Var, "answer2":row2Var, "answer3":row3Var}
	okBtn = Button(btm_frame2, text="Check Answer", width=25, height=4,
				   command=lambda: self.verseCheckAnswer(userAnswers, selectedVerse))
	okBtn.grid(row=0, column=2, pady=20)

	exitBtn = Button(btm_frame3, text="Leave", width=25, height=4,
				   command=lambda: self.screenSwitcher("home"))
	exitBtn.grid(row=0, column=3, pady=20)
















